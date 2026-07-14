#!/usr/bin/env python3
"""Build and validate deterministic, non-prose literary releases for Narramorph."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
POLICY_PATH = "editorial/runtime-release-policy-v1.json"
DEFAULT_OUTPUT = ROOT / "build" / "literary-releases"
FORMAT = "eternal-return-literary-release"
SCHEMA_VERSION = "1.0.0"
DO_NOT_EDIT = (
    "Generated from immutable manuscript/editorial Git blobs; do not edit or "
    "treat as manuscript prose."
)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
RELEASE_RE = re.compile(r"^[a-z0-9][a-z0-9.-]{2,63}$")
SOURCE_REF_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$")


class ExportError(ValueError):
    """Raised when source metadata or an artifact violates the release contract."""


def configure_utf8_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="strict")


def normalize(value: Any) -> Any:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n"))
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if isinstance(value, dict):
        return {normalize(str(key)): normalize(item) for key, item in value.items()}
    return value


def canonical_json_bytes(value: Any) -> bytes:
    normalized = normalize(value)
    text = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return (text + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def require_safe_path(value: str) -> str:
    if not value or "\\" in value or ":" in value or value.startswith("/"):
        raise ExportError(f"unsafe repository path: {value!r}")
    path = PurePosixPath(value)
    if any(part in {"", ".", ".."} for part in path.parts):
        raise ExportError(f"unsafe repository path: {value!r}")
    if path.as_posix() != value:
        raise ExportError(f"non-canonical repository path: {value!r}")
    return value


def run_git(repository: Path, *arguments: str) -> bytes:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=repository,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        error = completed.stderr.decode("utf-8", errors="replace").strip()
        raise ExportError(f"git {' '.join(arguments)} failed: {error}")
    return completed.stdout


def resolve_commit(repository: Path, source_ref: str) -> str:
    if not SOURCE_REF_RE.fullmatch(source_ref) or ".." in source_ref:
        raise ExportError(f"unsafe source ref: {source_ref!r}")
    commit = run_git(repository, "rev-parse", "--verify", f"{source_ref}^{{commit}}")
    value = commit.decode("ascii", errors="strict").strip()
    if not COMMIT_RE.fullmatch(value):
        raise ExportError(f"git returned an invalid commit ID: {value!r}")
    return value


def read_blob(repository: Path, commit: str, path: str) -> bytes:
    require_safe_path(path)
    if not COMMIT_RE.fullmatch(commit):
        raise ExportError(f"invalid source commit: {commit!r}")
    return run_git(repository, "show", f"{commit}:{path}")


def read_text_blob(repository: Path, commit: str, path: str) -> str:
    raw = read_blob(repository, commit, path)
    try:
        return raw.decode("utf-8-sig", errors="strict").replace("\r\n", "\n").replace("\r", "\n")
    except UnicodeDecodeError as error:
        raise ExportError(f"{path} is not valid UTF-8") from error


def list_tree_paths(repository: Path, commit: str, prefix: str) -> list[str]:
    require_safe_path(prefix)
    output = run_git(repository, "ls-tree", "-r", "--name-only", commit, "--", prefix)
    paths = [line for line in output.decode("utf-8", errors="strict").splitlines() if line]
    for path in paths:
        require_safe_path(path)
    return sorted(paths)


def commit_epoch(repository: Path, commit: str) -> int:
    output = run_git(repository, "show", "-s", "--format=%ct", commit)
    value = output.decode("ascii", errors="strict").strip()
    if not value.isdigit():
        raise ExportError(f"invalid source commit epoch: {value!r}")
    return int(value)


def slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    result = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    if not result:
        raise ExportError(f"cannot derive identifier from {value!r}")
    return result


def strip_markdown(value: str) -> str:
    result = value.strip()
    result = re.sub(r"\[(.*?)\]\([^)]*\)", r"\1", result)
    result = result.replace("**", "").replace("__", "").replace("`", "")
    result = result.replace("~~", "").replace("*", "").strip()
    return unicodedata.normalize("NFC", result)


def parse_structure_map(text: str, expected_count: int) -> list[dict[str, Any]]:
    chapters: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] == "File" or set(cells[0]) <= {"-", ":"}:
            continue
        match = re.fullmatch(r"(\d{2})-(.+)\.md", cells[0])
        if match is None:
            continue
        ordinal = int(match.group(1))
        chapters.append(
            {
                "chapterId": f"er-chapter-{ordinal:03d}",
                "cycleOrPhase": cells[2],
                "file": require_safe_path(f"manuscript/{cells[0]}"),
                "movement": int(cells[1]),
                "ordinal": ordinal,
                "sourceLine": line_number,
                "sourcePath": "bible/structure-map.md",
                "timeline": cells[4],
                "title": cells[5],
                "voice": cells[3],
            }
        )
    chapters.sort(key=lambda item: item["ordinal"])
    if len(chapters) != expected_count:
        raise ExportError(f"expected {expected_count} structure rows, found {len(chapters)}")
    if [item["ordinal"] for item in chapters] != list(range(1, expected_count + 1)):
        raise ExportError("structure-map chapter ordinals are not contiguous")
    return chapters


def collect_scene_summaries(value: Any, records: list[dict[str, str]]) -> None:
    if isinstance(value, dict):
        if all(isinstance(value.get(key), str) for key in ("id", "title", "notes")):
            records.append(
                {
                    "sourceId": value["id"],
                    "text": value["notes"],
                    "title": value["title"],
                }
            )
        for item in value.values():
            collect_scene_summaries(item, records)
    elif isinstance(value, list):
        for item in value:
            collect_scene_summaries(item, records)


def attach_scene_summaries(chapters: list[dict[str, Any]], outline: Any) -> None:
    records: list[dict[str, str]] = []
    collect_scene_summaries(outline, records)
    used: set[str] = set()
    for chapter in chapters:
        movement_prefix = f"m{chapter['movement']}-"
        candidates = [
            record
            for record in records
            if record["title"] == chapter["title"]
            and record["sourceId"].startswith(movement_prefix)
        ]
        voice_token = {
            "archaeologist": "-arch-",
            "algorithm": "-algo-",
            "last-human": "-lh-",
        }.get(chapter["voice"])
        if voice_token and len(candidates) > 1:
            candidates = [record for record in candidates if voice_token in record["sourceId"]]
        if len(candidates) != 1:
            raise ExportError(
                f"expected one editorial summary for {chapter['chapterId']} "
                f"({chapter['title']}), found {len(candidates)}"
            )
        record = candidates[0]
        if record["sourceId"] in used:
            raise ExportError(f"editorial summary reused: {record['sourceId']}")
        used.add(record["sourceId"])
        chapter["sceneSummary"] = {
            "kind": "editorial-summary-not-manuscript-prose",
            "sourceId": record["sourceId"],
            "sourcePath": "outlines/manifest.json",
            "text": record["text"],
        }


def parse_voice_profiles(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    names = {
        "Archaeologist": "archaeologist",
        "Algorithm": "algorithm",
        "Last Human": "last-human",
    }
    profiles: list[dict[str, Any]] = []
    for index, line in enumerate(lines):
        match = re.fullmatch(r"## (Archaeologist|Algorithm|Last Human)", line)
        if match is None:
            continue
        end = next(
            (position for position in range(index + 1, len(lines)) if lines[position].startswith("## ")),
            len(lines),
        )
        section = lines[index + 1 : end]
        parameters: dict[str, str] = {}
        markers: list[str] = []
        forbidden: list[str] = []
        for section_line in section:
            if section_line.startswith("|"):
                cells = [cell.strip() for cell in section_line.strip().strip("|").split("|")]
                if len(cells) == 2 and "Parameter" not in cells[0] and set(cells[0]) - {"-", ":"}:
                    parameters[slug(strip_markdown(cells[0]))] = strip_markdown(cells[1])
            marker_match = re.fullmatch(r"\*\*Voice Markers\*\*: (.+)", section_line)
            if marker_match:
                markers = [item.strip() for item in marker_match.group(1).split(",") if item.strip()]
            forbidden_match = re.fullmatch(r"\*\*Forbidden\*\*: (.+)", section_line)
            if forbidden_match:
                forbidden = [item.strip() for item in forbidden_match.group(1).split(",") if item.strip()]
        if not parameters or not markers or not forbidden:
            raise ExportError(f"incomplete voice metadata for {match.group(1)}")
        profiles.append(
            {
                "forbidden": forbidden,
                "markers": markers,
                "parameters": parameters,
                "sourceLine": index + 1,
                "sourcePath": "bible/voices/quick-reference.md",
                "voiceId": names[match.group(1)],
            }
        )
    if len(profiles) != 3:
        raise ExportError(f"expected three voice profiles, found {len(profiles)}")
    return sorted(profiles, key=lambda item: item["voiceId"])


def parse_philosophical_constraints(text: str) -> list[dict[str, Any]]:
    category_names = {
        "The Four Shackles": "four-shackles",
        "Key Concepts to Dramatize (Not Explain)": "key-concepts",
        "Forbidden Narrative Moves": "forbidden-moves",
    }
    category: str | None = None
    constraints: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            category = category_names.get(line[3:].strip())
            continue
        if category and line.startswith("### "):
            title = re.sub(r"^\d+\.\s*", "", line[4:].strip())
            constraints.append(
                {
                    "category": category,
                    "constraintId": f"er-philosophy-{category}-{slug(title)}",
                    "sourceLine": line_number,
                    "sourcePath": "bible/philosophy-constraints.md",
                    "title": title,
                }
            )
    if len(constraints) < 10:
        raise ExportError(f"expected at least ten philosophical constraints, found {len(constraints)}")
    return constraints


def parse_chronology(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    phases: list[dict[str, Any]] = []
    for index, line in enumerate(lines):
        match = re.fullmatch(r"## Phase (\d+): (.+)", line)
        if match is None:
            continue
        end = next(
            (position for position in range(index + 1, len(lines)) if lines[position].startswith("## ")),
            len(lines),
        )
        position_text: str | None = None
        for position in range(index + 1, end):
            if lines[position] != "### Timeline Position":
                continue
            position_text = next(
                (candidate.strip() for candidate in lines[position + 1 : end] if candidate.strip()),
                None,
            )
            break
        if not position_text:
            raise ExportError(f"missing timeline position for Phase {match.group(1)}")
        phases.append(
            {
                "chronologyId": f"er-chronology-phase-{int(match.group(1))}",
                "sourceLine": index + 1,
                "sourcePath": "bible/worldbuilding/catastrophe-timeline.md",
                "timelinePosition": strip_markdown(position_text),
                "title": match.group(2),
            }
        )
    if len(phases) != 4:
        raise ExportError(f"expected four chronology phases, found {len(phases)}")
    return phases


def promise_resolution(value: str) -> str:
    upper = strip_markdown(value).upper()
    if "RULING PENDING" in upper or "UNPAID" in upper:
        return "pending"
    if "PARTIALLY PAID" in upper or "WEAK" in upper or "INCONSISTENT" in upper:
        return "partial"
    if "PAID" in upper:
        return "paid"
    return "review-required"


def parse_promise_payoffs(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    start = next(
        (index for index, line in enumerate(lines) if "Promise / payoff ledger" in line),
        None,
    )
    if start is None:
        raise ExportError("promise/payoff ledger heading not found")
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if line.startswith("## "):
            break
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0] == "#" or set(cells[0]) <= {"-", ":"}:
            continue
        promise_ids = re.findall(r"P(?:-?[A-Za-z]+|\d+)", strip_markdown(cells[0]))
        for promise_id in promise_ids:
            if promise_id in seen:
                raise ExportError(f"duplicate promise ID in ledger: {promise_id}")
            seen.add(promise_id)
            records.append(
                {
                    "promiseId": promise_id,
                    "resolution": promise_resolution(cells[2]),
                    "setupReference": strip_markdown(cells[1]),
                    "sourceLine": index + 1,
                    "sourcePath": "editorial/BOOK-MAP.md",
                }
            )
    if len(records) < 20:
        raise ExportError(f"expected at least twenty promise references, found {len(records)}")
    return sorted(records, key=lambda item: item["promiseId"])


def source_file_record(path: str, content: bytes) -> dict[str, str]:
    return {"path": require_safe_path(path), "sha256": sha256_bytes(content)}


def load_json_bytes(raw: bytes, path: str) -> Any:
    try:
        return json.loads(raw.decode("utf-8-sig", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ExportError(f"invalid UTF-8 JSON in {path}: {error}") from error


def validate_policy(policy: Any) -> dict[str, Any]:
    if not isinstance(policy, dict):
        raise ExportError("release policy must be an object")
    required = {
        "approvedExcerptMarkers",
        "characters",
        "contentLicense",
        "contextSources",
        "contractSchemaVersion",
        "expectedChapterCount",
        "glossary",
        "permissionPath",
        "policySchemaVersion",
        "storyId",
        "storyVersion",
        "targetRepository",
        "targetStoryPackage",
    }
    missing = required - set(policy)
    if missing:
        raise ExportError(f"release policy is missing: {', '.join(sorted(missing))}")
    if policy["approvedExcerptMarkers"] != []:
        raise ExportError("v1 refuses excerpts because no pre-existing approval markers exist")
    if policy["policySchemaVersion"] != SCHEMA_VERSION:
        raise ExportError(f"unsupported policy schema: {policy['policySchemaVersion']!r}")
    if policy["storyId"] != "eternal-return":
        raise ExportError(f"unsupported story ID: {policy['storyId']!r}")
    if not isinstance(policy["expectedChapterCount"], int) or policy["expectedChapterCount"] < 1:
        raise ExportError("expectedChapterCount must be a positive integer")
    context_sources = policy["contextSources"]
    if not isinstance(context_sources, list) or not context_sources:
        raise ExportError("contextSources must be a non-empty array")
    for path in context_sources:
        if not isinstance(path, str):
            raise ExportError("contextSources entries must be strings")
        require_safe_path(path)
    if len(context_sources) != len(set(context_sources)):
        raise ExportError("contextSources contains duplicates")
    require_safe_path(policy["permissionPath"])
    return policy


def build_release(repository: Path, source_ref: str, release_id: str) -> dict[str, Any]:
    if not RELEASE_RE.fullmatch(release_id) or ".." in release_id:
        raise ExportError(f"invalid editorial release ID: {release_id!r}")
    commit = resolve_commit(repository, source_ref)
    policy_raw = read_blob(repository, commit, POLICY_PATH)
    policy = validate_policy(load_json_bytes(policy_raw, POLICY_PATH))

    context_paths = sorted({POLICY_PATH, *policy["contextSources"]})
    context_blobs = {path: read_blob(repository, commit, path) for path in context_paths}
    manuscript_paths = [
        path for path in list_tree_paths(repository, commit, "manuscript") if path.endswith(".md")
    ]
    expected_count = policy["expectedChapterCount"]
    if len(manuscript_paths) != expected_count:
        raise ExportError(
            f"expected {expected_count} manuscript files at {commit}, found {len(manuscript_paths)}"
        )
    manuscript_blobs = {path: read_blob(repository, commit, path) for path in manuscript_paths}

    chapters = parse_structure_map(
        context_blobs["bible/structure-map.md"].decode("utf-8-sig", errors="strict"),
        expected_count,
    )
    outline = load_json_bytes(context_blobs["outlines/manifest.json"], "outlines/manifest.json")
    attach_scene_summaries(chapters, outline)
    structure_paths = [chapter["file"] for chapter in chapters]
    if structure_paths != manuscript_paths:
        raise ExportError("structure map and canonical manuscript tree do not contain identical paths")

    epoch = commit_epoch(repository, commit)
    generated_at = datetime.fromtimestamp(epoch, tz=timezone.utc).isoformat().replace("+00:00", "Z")
    context = {
        "chapters": chapters,
        "characters": policy["characters"],
        "chronology": parse_chronology(
            context_blobs["bible/worldbuilding/catastrophe-timeline.md"].decode(
                "utf-8-sig", errors="strict"
            )
        ),
        "excerpts": [],
        "glossary": policy["glossary"],
        "philosophicalConstraints": parse_philosophical_constraints(
            context_blobs["bible/philosophy-constraints.md"].decode("utf-8-sig", errors="strict")
        ),
        "promisePayoffs": parse_promise_payoffs(
            context_blobs["editorial/BOOK-MAP.md"].decode("utf-8-sig", errors="strict")
        ),
        "voices": parse_voice_profiles(
            context_blobs["bible/voices/quick-reference.md"].decode("utf-8-sig", errors="strict")
        ),
    }
    payload = {
        "context": context,
        "doNotEdit": DO_NOT_EDIT,
        "format": FORMAT,
        "manifest": {
            "contentLicense": policy["contentLicense"],
            "contractSchemaVersion": policy["contractSchemaVersion"],
            "editorialReleaseId": release_id,
            "excerptPolicy": {"approvedExcerptCount": 0, "markerRequired": True},
            "generatedAt": generated_at,
            "permission": {
                "approvalRecordRequired": True,
                "path": policy["permissionPath"],
            },
            "policySchemaVersion": policy["policySchemaVersion"],
            "sourceCommit": commit,
            "sourceDateEpoch": epoch,
            "storyId": policy["storyId"],
            "storyVersion": policy["storyVersion"],
            "targetRepository": policy["targetRepository"],
            "targetStoryPackage": policy["targetStoryPackage"],
            "validation": {
                "chapterCount": len(chapters),
                "contextSourceCount": len(context_paths),
                "excerptCount": 0,
                "manuscriptFileCount": len(manuscript_paths),
            },
        },
        "sourceFiles": {
            "context": [source_file_record(path, context_blobs[path]) for path in context_paths],
            "manuscript": [
                source_file_record(path, manuscript_blobs[path]) for path in manuscript_paths
            ],
        },
    }
    document = {
        "contentSha256": sha256_bytes(canonical_json_bytes(payload)),
        "payload": payload,
        "schemaVersion": SCHEMA_VERSION,
    }
    validate_release_document(document)
    return normalize(document)


def validate_source_files(source_files: Any, label: str) -> list[dict[str, str]]:
    if not isinstance(source_files, list) or not source_files:
        raise ExportError(f"sourceFiles.{label} must be a non-empty array")
    paths: list[str] = []
    result: list[dict[str, str]] = []
    for item in source_files:
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            raise ExportError(f"invalid sourceFiles.{label} record")
        path = require_safe_path(item["path"])
        if not SHA256_RE.fullmatch(item["sha256"]):
            raise ExportError(f"invalid SHA-256 for {path}")
        paths.append(path)
        result.append(item)
    if paths != sorted(paths) or len(paths) != len(set(paths)):
        raise ExportError(f"sourceFiles.{label} paths must be unique and sorted")
    return result


def validate_release_document(document: Any) -> None:
    if not isinstance(document, dict) or set(document) != {
        "contentSha256",
        "payload",
        "schemaVersion",
    }:
        raise ExportError("release document has unexpected top-level fields")
    if document["schemaVersion"] != SCHEMA_VERSION:
        raise ExportError(f"unsupported literary release schema: {document['schemaVersion']!r}")
    if not SHA256_RE.fullmatch(document["contentSha256"]):
        raise ExportError("contentSha256 is malformed")
    if document["contentSha256"] != sha256_bytes(canonical_json_bytes(document["payload"])):
        raise ExportError("contentSha256 does not cover the canonical payload")
    payload = document["payload"]
    if not isinstance(payload, dict) or set(payload) != {
        "context",
        "doNotEdit",
        "format",
        "manifest",
        "sourceFiles",
    }:
        raise ExportError("release payload has unexpected fields")
    if payload["format"] != FORMAT or payload["doNotEdit"] != DO_NOT_EDIT:
        raise ExportError("release format or do-not-edit declaration is invalid")
    manifest = payload["manifest"]
    if not isinstance(manifest, dict):
        raise ExportError("manifest must be an object")
    if not RELEASE_RE.fullmatch(manifest.get("editorialReleaseId", "")):
        raise ExportError("manifest editorialReleaseId is invalid")
    if not COMMIT_RE.fullmatch(manifest.get("sourceCommit", "")):
        raise ExportError("manifest sourceCommit is invalid")
    if manifest.get("policySchemaVersion") != SCHEMA_VERSION:
        raise ExportError("manifest policy schema is unsupported")
    if not isinstance(manifest.get("sourceDateEpoch"), int) or manifest["sourceDateEpoch"] < 0:
        raise ExportError("manifest sourceDateEpoch is invalid")
    if not isinstance(manifest.get("contentLicense"), str) or not manifest["contentLicense"]:
        raise ExportError("manifest content license is missing")
    if manifest.get("excerptPolicy") != {"approvedExcerptCount": 0, "markerRequired": True}:
        raise ExportError("v1 excerpt policy must require markers and approve zero excerpts")
    context = payload["context"]
    required_context = {
        "chapters",
        "characters",
        "chronology",
        "excerpts",
        "glossary",
        "philosophicalConstraints",
        "promisePayoffs",
        "voices",
    }
    if not isinstance(context, dict) or set(context) != required_context:
        raise ExportError("release context has unexpected fields")
    if context["excerpts"] != []:
        raise ExportError("v1 artifact cannot contain excerpts")

    source_files = payload["sourceFiles"]
    if not isinstance(source_files, dict) or set(source_files) != {"context", "manuscript"}:
        raise ExportError("sourceFiles must contain context and manuscript arrays")
    context_sources = validate_source_files(source_files["context"], "context")
    manuscript_sources = validate_source_files(source_files["manuscript"], "manuscript")
    validation = manifest.get("validation")
    if not isinstance(validation, dict):
        raise ExportError("manifest validation summary is missing")
    if validation.get("contextSourceCount") != len(context_sources):
        raise ExportError("context source count does not match sourceFiles")
    if validation.get("manuscriptFileCount") != len(manuscript_sources):
        raise ExportError("manuscript file count does not match sourceFiles")
    if validation.get("excerptCount") != 0:
        raise ExportError("excerpt count must be zero")

    chapters = context["chapters"]
    if not isinstance(chapters, list) or len(chapters) != validation.get("chapterCount"):
        raise ExportError("chapter count does not match manifest validation")
    chapter_ids = [chapter.get("chapterId") for chapter in chapters if isinstance(chapter, dict)]
    ordinals = [chapter.get("ordinal") for chapter in chapters if isinstance(chapter, dict)]
    chapter_paths = [chapter.get("file") for chapter in chapters if isinstance(chapter, dict)]
    if len(chapter_ids) != len(chapters) or len(set(chapter_ids)) != len(chapters):
        raise ExportError("chapter IDs must be present and unique")
    if ordinals != list(range(1, len(chapters) + 1)):
        raise ExportError("chapter ordinals must be contiguous and sorted")
    if chapter_paths != [record["path"] for record in manuscript_sources]:
        raise ExportError("chapter paths must equal the hashed manuscript source paths")
    for chapter in chapters:
        if set(chapter.get("sceneSummary", {})) != {"kind", "sourceId", "sourcePath", "text"}:
            raise ExportError(f"chapter {chapter.get('chapterId')} has no structured scene summary")
    for name in ("characters", "chronology", "glossary", "philosophicalConstraints", "promisePayoffs", "voices"):
        if not isinstance(context[name], list) or not context[name]:
            raise ExportError(f"context.{name} must be a non-empty array")

    def check_normalization(value: Any) -> None:
        if isinstance(value, str):
            if value != unicodedata.normalize("NFC", value) or "\r" in value:
                raise ExportError("artifact strings must be NFC and LF-normalized")
        elif isinstance(value, list):
            for item in value:
                check_normalization(item)
        elif isinstance(value, dict):
            for key, item in value.items():
                check_normalization(key)
                check_normalization(item)

    check_normalization(document)


def validate_serialized_release(raw: bytes) -> dict[str, Any]:
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ExportError("artifact must not contain a UTF-8 BOM")
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise ExportError("artifact must contain exactly one terminal LF")
    try:
        document = json.loads(raw.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ExportError(f"artifact is not valid UTF-8 JSON: {error}") from error
    validate_release_document(document)
    if raw != canonical_json_bytes(document):
        raise ExportError("artifact is not canonical JSON")
    return document


def verify_recorded_sources(repository: Path, document: dict[str, Any]) -> None:
    commit = document["payload"]["manifest"]["sourceCommit"]
    resolved = resolve_commit(repository, commit)
    if resolved != commit:
        raise ExportError("source commit did not resolve immutably")
    for group in ("context", "manuscript"):
        for record in document["payload"]["sourceFiles"][group]:
            actual = sha256_bytes(read_blob(repository, commit, record["path"]))
            if actual != record["sha256"]:
                raise ExportError(f"source hash mismatch: {record['path']}")
    epoch = commit_epoch(repository, commit)
    if epoch != document["payload"]["manifest"]["sourceDateEpoch"]:
        raise ExportError("source commit timestamp does not match the artifact")


def require_output_boundary(output: Path) -> None:
    resolved = output.resolve()
    manuscript = (ROOT / "manuscript").resolve()
    try:
        resolved.relative_to(manuscript)
    except ValueError:
        return
    raise ExportError("export output cannot be written beneath manuscript/")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--release", help="editorial release ID to build")
    action.add_argument("--validate", type=Path, help="artifact to validate")
    parser.add_argument("--source-commit", default="HEAD", help="immutable commit or safe ref")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT, help="generated output directory")
    return parser


def main() -> None:
    configure_utf8_output()
    arguments = build_parser().parse_args()
    try:
        if arguments.validate is not None:
            raw = arguments.validate.read_bytes()
            document = validate_serialized_release(raw)
            verify_recorded_sources(ROOT, document)
            print(
                f"Validated {arguments.validate}: "
                f"release={document['payload']['manifest']['editorialReleaseId']} "
                f"contentSha256={document['contentSha256']} "
                f"artifactSha256={sha256_bytes(raw)}"
            )
            return

        output_directory = arguments.out
        require_output_boundary(output_directory)
        document = build_release(ROOT, arguments.source_commit, arguments.release)
        raw = canonical_json_bytes(document)
        validate_serialized_release(raw)
        output_directory.mkdir(parents=True, exist_ok=True)
        output_path = output_directory / f"{arguments.release}.json"
        require_output_boundary(output_path)
        output_path.write_bytes(raw)
        print(
            f"Built {output_path}: release={arguments.release} "
            f"sourceCommit={document['payload']['manifest']['sourceCommit']} "
            f"contentSha256={document['contentSha256']} "
            f"artifactSha256={sha256_bytes(raw)}"
        )
    except (ExportError, OSError) as error:
        raise SystemExit(f"FAILED: {error}") from error


if __name__ == "__main__":
    main()
