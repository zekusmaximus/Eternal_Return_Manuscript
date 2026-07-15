#!/usr/bin/env python3
"""Build and validate a deterministic, non-prose literary vertical slice."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

try:
    from scripts.export_runtime_source import (
        COMMIT_RE,
        ROOT,
        SCHEMA_VERSION,
        SHA256_RE,
        ExportError,
        build_release,
        canonical_json_bytes,
        configure_utf8_output,
        read_blob,
        require_output_boundary,
        require_safe_path,
        resolve_commit,
        sha256_bytes,
        validate_release_document,
        validate_serialized_release,
        verify_recorded_sources,
    )
except ModuleNotFoundError:
    from export_runtime_source import (  # type: ignore[no-redef]
        COMMIT_RE,
        ROOT,
        SCHEMA_VERSION,
        SHA256_RE,
        ExportError,
        build_release,
        canonical_json_bytes,
        configure_utf8_output,
        read_blob,
        require_output_boundary,
        require_safe_path,
        resolve_commit,
        sha256_bytes,
        validate_release_document,
        validate_serialized_release,
        verify_recorded_sources,
    )

FORMAT = "eternal-return-literary-slice"
DO_NOT_EDIT = (
    "Generated from an immutable literary release and reviewed selection metadata; "
    "do not edit or treat as manuscript prose."
)
SELECTION_DIRECTORY = "editorial/vertical-slices"
SLICE_SCHEMA_PATH = "schemas/literary-slice-v1.schema.json"
DEFAULT_OUTPUT = ROOT / "build" / "literary-releases"
STABLE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
OPAQUE_PASSAGE_ID_RE = re.compile(r"^spv1_psg_[0-9a-f]{24}$")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
RELATIONSHIPS = {
    "direct-adaptation",
    "thematic-derivative",
    "interactive-only-connective",
    "independent-runtime",
}
CONTEXT_IDS = {
    "chapters": "chapterId",
    "chronology": "chronologyId",
    "philosophicalConstraints": "constraintId",
    "promisePayoffs": "promiseId",
    "voices": "voiceId",
}
MAPPING_IDS = {
    "chapterIds": "chapters",
    "chronologyIds": "chronology",
    "philosophicalConstraintIds": "philosophicalConstraints",
    "promiseIds": "promisePayoffs",
    "voiceIds": "voices",
}


def require_stable_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not STABLE_ID_RE.fullmatch(value):
        raise ExportError(f"{label} is not a stable identifier")
    return value


def require_string_array(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ExportError(f"{label} must be a non-empty array")
    result = [require_stable_id(item, label) for item in value]
    if len(result) != len(set(result)):
        raise ExportError(f"{label} contains duplicate IDs")
    return result


def parse_selection(raw: bytes, path: str) -> dict[str, Any]:
    try:
        value = json.loads(raw.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ExportError(f"invalid slice selection JSON at {path}: {error}") from error
    return validate_selection(value, path)


def validate_selection(value: Any, path: str) -> dict[str, Any]:
    expected = {
        "artifactFile",
        "expectedContextCounts",
        "mappings",
        "rationale",
        "runtimeTargets",
        "schemaVersion",
        "sliceId",
        "sliceVersion",
        "storyId",
    }
    if not isinstance(value, dict) or set(value) != expected:
        raise ExportError(f"slice selection has unexpected fields: {path}")
    if value["schemaVersion"] != SCHEMA_VERSION:
        raise ExportError("slice selection schema is unsupported")
    require_stable_id(value["sliceId"], "sliceId")
    require_stable_id(value["storyId"], "storyId")
    if not SEMVER_RE.fullmatch(value["sliceVersion"]):
        raise ExportError("sliceVersion must be semantic")
    artifact_file = require_safe_path(value["artifactFile"])
    if "/" in artifact_file or not artifact_file.endswith(".json"):
        raise ExportError("artifactFile must be a JSON filename")
    if not isinstance(value["rationale"], str) or not value["rationale"].strip():
        raise ExportError("slice rationale is required")

    targets = value["runtimeTargets"]
    if not isinstance(targets, list) or len(targets) != 2:
        raise ExportError("vertical slice must declare exactly two runtime targets")
    target_keys: list[str] = []
    for target in targets:
        if not isinstance(target, dict) or set(target) != {
            "connections",
            "layer",
            "passageId",
            "passageStableKey",
        }:
            raise ExportError("runtime target has unexpected fields")
        stable_key = require_stable_id(target["passageStableKey"], "runtime passage key")
        if not OPAQUE_PASSAGE_ID_RE.fullmatch(target["passageId"]):
            raise ExportError("runtime passage ID is not a Story Package passage ID")
        if target["layer"] not in {1, 2}:
            raise ExportError("vertical slice target layers must be 1 or 2")
        connections = target["connections"]
        if not isinstance(connections, list) or any(
            not isinstance(item, str) or not STABLE_ID_RE.fullmatch(item) for item in connections
        ):
            raise ExportError("runtime target connections are malformed")
        if len(connections) != len(set(connections)):
            raise ExportError("runtime target connections contain duplicates")
        target_keys.append(stable_key)
    if len(set(target_keys)) != 2:
        raise ExportError("runtime target stable keys must be unique")
    if targets[0]["layer"] != 1 or targets[1]["layer"] != 2:
        raise ExportError("vertical slice must be ordered L1 then L2")
    if target_keys[1] not in targets[0]["connections"]:
        raise ExportError("vertical slice runtime targets are not connected")

    mappings = value["mappings"]
    if not isinstance(mappings, list) or len(mappings) != 2:
        raise ExportError("vertical slice must declare exactly two mappings")
    mapped_keys: list[str] = []
    for mapping in mappings:
        if not isinstance(mapping, dict) or set(mapping) != {
            "chapterIds",
            "chronologyIds",
            "passageStableKey",
            "philosophicalConstraintIds",
            "promiseIds",
            "relationship",
            "themeClaims",
            "voiceIds",
        }:
            raise ExportError("slice mapping has unexpected fields")
        mapped_keys.append(require_stable_id(mapping["passageStableKey"], "mapping passage key"))
        if mapping["relationship"] not in RELATIONSHIPS:
            raise ExportError("slice mapping has an unknown relationship")
        for field in (*MAPPING_IDS, "themeClaims"):
            require_string_array(mapping[field], f"mapping {field}")
    if mapped_keys != target_keys:
        raise ExportError("slice mappings must match ordered runtime targets")

    counts = value["expectedContextCounts"]
    if not isinstance(counts, dict) or set(counts) != set(CONTEXT_IDS):
        raise ExportError("expectedContextCounts has unexpected fields")
    if any(not isinstance(count, int) or count < 1 for count in counts.values()):
        raise ExportError("expected context counts must be positive integers")
    return value


def select_context(
    release: dict[str, Any], selection: dict[str, Any]
) -> dict[str, list[dict[str, Any]]]:
    release_context = release["payload"]["context"]
    requested: dict[str, set[str]] = {group: set() for group in CONTEXT_IDS}
    for mapping in selection["mappings"]:
        for field, group in MAPPING_IDS.items():
            requested[group].update(mapping[field])

    result: dict[str, list[dict[str, Any]]] = {}
    for group, id_key in CONTEXT_IDS.items():
        source = release_context[group]
        by_id = {record[id_key]: record for record in source}
        missing = sorted(requested[group] - set(by_id))
        if missing:
            raise ExportError(f"slice selection references unknown {group}: {', '.join(missing)}")
        result[group] = [record for record in source if record[id_key] in requested[group]]
        expected_count = selection["expectedContextCounts"][group]
        if len(result[group]) != expected_count:
            raise ExportError(
                f"slice {group} count mismatch: expected {expected_count}, found {len(result[group])}"
            )
    return result


def build_vertical_slice(
    repository: Path,
    source_ref: str,
    release_id: str,
    slice_id: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    commit = resolve_commit(repository, source_ref)
    selection_path = f"{SELECTION_DIRECTORY}/{slice_id}.json"
    selection_raw = read_blob(repository, commit, selection_path)
    schema_raw = read_blob(repository, commit, SLICE_SCHEMA_PATH)
    selection = parse_selection(selection_raw, selection_path)
    if selection["sliceId"] != slice_id:
        raise ExportError("slice ID does not match its selection document")
    release = build_release(repository, commit, release_id)
    release_manifest = release["payload"]["manifest"]
    if selection["storyId"] != release_manifest["storyId"]:
        raise ExportError("slice story ID does not match the literary release")
    context = select_context(release, selection)
    payload = {
        "baseRelease": {
            "artifactFile": f"{release_id}.json",
            "contentSha256": release["contentSha256"],
            "editorialReleaseId": release_id,
            "schemaVersion": release["schemaVersion"],
            "sourceCommit": commit,
        },
        "context": context,
        "doNotEdit": DO_NOT_EDIT,
        "format": FORMAT,
        "manifest": {
            "contentLicense": release_manifest["contentLicense"],
            "generatedAt": release_manifest["generatedAt"],
            "permission": release_manifest["permission"],
            "rationale": selection["rationale"],
            "schemaSource": {
                "path": SLICE_SCHEMA_PATH,
                "sha256": sha256_bytes(schema_raw),
            },
            "selectionSource": {
                "path": selection_path,
                "sha256": sha256_bytes(selection_raw),
            },
            "sliceId": slice_id,
            "sliceVersion": selection["sliceVersion"],
            "sourceCommit": commit,
            "sourceDateEpoch": release_manifest["sourceDateEpoch"],
            "storyId": release_manifest["storyId"],
            "targetRepository": release_manifest["targetRepository"],
            "targetStoryPackage": release_manifest["targetStoryPackage"],
            "validation": {
                "mappingCount": len(selection["mappings"]),
                "runtimeTargetCount": len(selection["runtimeTargets"]),
                "selectedContextCounts": {
                    group: len(records) for group, records in context.items()
                },
            },
        },
        "mappings": selection["mappings"],
        "runtimeTargets": selection["runtimeTargets"],
    }
    document = {
        "contentSha256": sha256_bytes(canonical_json_bytes(payload)),
        "payload": payload,
        "schemaVersion": SCHEMA_VERSION,
    }
    validate_slice_document(document, release)
    return release, document


def validate_slice_document(document: Any, release: dict[str, Any]) -> None:
    validate_release_document(release)
    if not isinstance(document, dict) or set(document) != {
        "contentSha256",
        "payload",
        "schemaVersion",
    }:
        raise ExportError("slice document has unexpected top-level fields")
    if document["schemaVersion"] != SCHEMA_VERSION:
        raise ExportError("slice schema is unsupported")
    if not isinstance(document["contentSha256"], str) or not SHA256_RE.fullmatch(
        document["contentSha256"]
    ):
        raise ExportError("slice contentSha256 is malformed")
    if document["contentSha256"] != sha256_bytes(canonical_json_bytes(document["payload"])):
        raise ExportError("slice contentSha256 does not cover the canonical payload")
    payload = document["payload"]
    if not isinstance(payload, dict) or set(payload) != {
        "baseRelease",
        "context",
        "doNotEdit",
        "format",
        "manifest",
        "mappings",
        "runtimeTargets",
    }:
        raise ExportError("slice payload has unexpected fields")
    if payload["format"] != FORMAT or payload["doNotEdit"] != DO_NOT_EDIT:
        raise ExportError("slice format or do-not-edit declaration is invalid")

    release_manifest = release["payload"]["manifest"]
    base = payload["baseRelease"]
    expected_base = {
        "artifactFile": f"{release_manifest['editorialReleaseId']}.json",
        "contentSha256": release["contentSha256"],
        "editorialReleaseId": release_manifest["editorialReleaseId"],
        "schemaVersion": release["schemaVersion"],
        "sourceCommit": release_manifest["sourceCommit"],
    }
    if base != expected_base:
        raise ExportError("slice base release identity mismatch")

    manifest = payload["manifest"]
    required_manifest = {
        "contentLicense",
        "generatedAt",
        "permission",
        "rationale",
        "schemaSource",
        "selectionSource",
        "sliceId",
        "sliceVersion",
        "sourceCommit",
        "sourceDateEpoch",
        "storyId",
        "targetRepository",
        "targetStoryPackage",
        "validation",
    }
    if not isinstance(manifest, dict) or set(manifest) != required_manifest:
        raise ExportError("slice manifest has unexpected fields")
    if not COMMIT_RE.fullmatch(manifest["sourceCommit"]):
        raise ExportError("slice source commit is malformed")
    if manifest["sourceCommit"] != release_manifest["sourceCommit"]:
        raise ExportError("slice source commit does not match base release")
    if manifest["contentLicense"] != release_manifest["contentLicense"]:
        raise ExportError("slice content license does not match base release")
    if manifest["permission"] != release_manifest["permission"]:
        raise ExportError("slice permission does not match base release")
    require_stable_id(manifest["sliceId"], "slice manifest ID")
    if not SEMVER_RE.fullmatch(manifest["sliceVersion"]):
        raise ExportError("slice manifest version is invalid")
    for source_name in ("selectionSource", "schemaSource"):
        source = manifest[source_name]
        if not isinstance(source, dict) or set(source) != {"path", "sha256"}:
            raise ExportError(f"slice {source_name} is malformed")
        require_safe_path(source["path"])
        if not SHA256_RE.fullmatch(source["sha256"]):
            raise ExportError(f"slice {source_name} hash is malformed")

    targets = payload["runtimeTargets"]
    mappings = payload["mappings"]
    if not isinstance(targets, list) or not isinstance(mappings, list) or len(targets) != 2:
        raise ExportError("slice targets/mappings are malformed")
    if len(mappings) != len(targets):
        raise ExportError("slice mapping count does not match runtime targets")
    target_keys: list[str] = []
    for target in targets:
        if not isinstance(target, dict) or set(target) != {
            "connections",
            "layer",
            "passageId",
            "passageStableKey",
        }:
            raise ExportError("slice runtime target is malformed")
        target_keys.append(require_stable_id(target["passageStableKey"], "runtime target"))
        if not OPAQUE_PASSAGE_ID_RE.fullmatch(target["passageId"]):
            raise ExportError("slice runtime target passage ID is malformed")
    if targets[0]["layer"] != 1 or targets[1]["layer"] != 2:
        raise ExportError("slice target layers are not L1 then L2")
    if target_keys[1] not in targets[0]["connections"]:
        raise ExportError("slice runtime targets are not connected")
    if len(target_keys) != len(set(target_keys)):
        raise ExportError("slice runtime targets are duplicated")

    context = payload["context"]
    if not isinstance(context, dict) or set(context) != set(CONTEXT_IDS):
        raise ExportError("slice context has unexpected fields")
    context_ids: dict[str, set[str]] = {}
    for group, id_key in CONTEXT_IDS.items():
        records = context[group]
        if not isinstance(records, list) or not records:
            raise ExportError(f"slice context.{group} must be non-empty")
        ids = [record.get(id_key) for record in records if isinstance(record, dict)]
        if len(ids) != len(records) or len(ids) != len(set(ids)):
            raise ExportError(f"slice context.{group} IDs must be present and unique")
        context_ids[group] = set(ids)
        release_by_id = {
            record[id_key]: record for record in release["payload"]["context"][group]
        }
        if any(release_by_id.get(record[id_key]) != record for record in records):
            raise ExportError(f"slice context.{group} is not an exact base-release subset")

    mapped_keys: list[str] = []
    for mapping in mappings:
        if not isinstance(mapping, dict) or set(mapping) != {
            "chapterIds",
            "chronologyIds",
            "passageStableKey",
            "philosophicalConstraintIds",
            "promiseIds",
            "relationship",
            "themeClaims",
            "voiceIds",
        }:
            raise ExportError("slice mapping is malformed")
        mapped_keys.append(require_stable_id(mapping["passageStableKey"], "mapping target"))
        if mapping["relationship"] not in RELATIONSHIPS:
            raise ExportError("slice mapping relationship is unknown")
        require_string_array(mapping["themeClaims"], "mapping themeClaims")
        for field, group in MAPPING_IDS.items():
            ids = require_string_array(mapping[field], f"mapping {field}")
            if any(identifier not in context_ids[group] for identifier in ids):
                raise ExportError(f"slice mapping {field} has an unmapped canonical claim")
    if mapped_keys != target_keys:
        raise ExportError("slice mappings do not match runtime targets")

    validation = manifest["validation"]
    expected_counts = {group: len(records) for group, records in context.items()}
    if validation != {
        "mappingCount": len(mappings),
        "runtimeTargetCount": len(targets),
        "selectedContextCounts": expected_counts,
    }:
        raise ExportError("slice validation summary does not match payload")


def validate_serialized_slice(raw: bytes, release: dict[str, Any]) -> dict[str, Any]:
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ExportError("slice artifact must not contain a UTF-8 BOM")
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise ExportError("slice artifact must contain exactly one terminal LF")
    try:
        document = json.loads(raw.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ExportError(f"slice artifact is not valid UTF-8 JSON: {error}") from error
    validate_slice_document(document, release)
    if raw != canonical_json_bytes(document):
        raise ExportError("slice artifact is not canonical JSON")
    return document


def verify_slice_sources(
    repository: Path, document: dict[str, Any], release: dict[str, Any]
) -> None:
    verify_recorded_sources(repository, release)
    commit = document["payload"]["manifest"]["sourceCommit"]
    if resolve_commit(repository, commit) != commit:
        raise ExportError("slice source commit did not resolve immutably")
    for source_name in ("selectionSource", "schemaSource"):
        source = document["payload"]["manifest"][source_name]
        actual = sha256_bytes(read_blob(repository, commit, source["path"]))
        if actual != source["sha256"]:
            raise ExportError(f"slice source hash mismatch: {source['path']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--slice", help="vertical slice ID to build")
    action.add_argument("--validate", type=Path, help="slice artifact to validate")
    parser.add_argument("--release-id", help="base literary release ID for a build")
    parser.add_argument("--base-release", type=Path, help="base release artifact for validation")
    parser.add_argument("--source-commit", default="HEAD", help="immutable commit or safe ref")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT, help="generated output directory")
    return parser


def main() -> None:
    configure_utf8_output()
    arguments = build_parser().parse_args()
    try:
        if arguments.validate is not None:
            if arguments.base_release is None:
                raise ExportError("--base-release is required with --validate")
            release_raw = arguments.base_release.read_bytes()
            release = validate_serialized_release(release_raw)
            slice_raw = arguments.validate.read_bytes()
            document = validate_serialized_slice(slice_raw, release)
            verify_slice_sources(ROOT, document, release)
            print(
                f"Validated {arguments.validate}: "
                f"slice={document['payload']['manifest']['sliceId']}@"
                f"{document['payload']['manifest']['sliceVersion']} "
                f"baseRelease={document['payload']['baseRelease']['editorialReleaseId']} "
                f"contentSha256={document['contentSha256']} "
                f"artifactSha256={sha256_bytes(slice_raw)}"
            )
            return

        if not arguments.release_id:
            raise ExportError("--release-id is required with --slice")
        require_output_boundary(arguments.out)
        release, document = build_vertical_slice(
            ROOT,
            arguments.source_commit,
            arguments.release_id,
            arguments.slice,
        )
        release_raw = canonical_json_bytes(release)
        slice_raw = canonical_json_bytes(document)
        validate_serialized_release(release_raw)
        validate_serialized_slice(slice_raw, release)
        arguments.out.mkdir(parents=True, exist_ok=True)
        release_path = arguments.out / f"{arguments.release_id}.json"
        selection = parse_selection(
            read_blob(
                ROOT,
                document["payload"]["manifest"]["sourceCommit"],
                document["payload"]["manifest"]["selectionSource"]["path"],
            ),
            document["payload"]["manifest"]["selectionSource"]["path"],
        )
        slice_path = arguments.out / selection["artifactFile"]
        require_output_boundary(release_path)
        require_output_boundary(slice_path)
        release_path.write_bytes(release_raw)
        slice_path.write_bytes(slice_raw)
        print(
            f"Built {release_path}: release={arguments.release_id} "
            f"contentSha256={release['contentSha256']} "
            f"artifactSha256={sha256_bytes(release_raw)}"
        )
        print(
            f"Built {slice_path}: slice={arguments.slice}@{selection['sliceVersion']} "
            f"sourceCommit={document['payload']['manifest']['sourceCommit']} "
            f"contentSha256={document['contentSha256']} "
            f"artifactSha256={sha256_bytes(slice_raw)}"
        )
    except (ExportError, OSError) as error:
        raise SystemExit(f"FAILED: {error}") from error


if __name__ == "__main__":
    main()
