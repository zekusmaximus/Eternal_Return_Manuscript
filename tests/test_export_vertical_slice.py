"""Determinism, provenance, and negative-path proofs for the vertical slice."""

from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

from scripts.export_runtime_source import ExportError, canonical_json_bytes, sha256_bytes
from scripts.export_vertical_slice import (
    build_vertical_slice,
    validate_serialized_slice,
    validate_slice_document,
    verify_slice_sources,
)

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
RELEASE_ID = "test-literary-release-v1.0.1"
SLICE_ID = "archaeologist-opening-accept"


def manuscript_hashes() -> dict[str, str]:
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(MANUSCRIPT.glob("*.md"))
    }


class VerticalSliceExporterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.release, cls.slice = build_vertical_slice(ROOT, "HEAD", RELEASE_ID, SLICE_ID)
        cls.slice_bytes = canonical_json_bytes(cls.slice)

    def test_repeated_slice_exports_are_byte_stable_and_non_mutating(self) -> None:
        before = manuscript_hashes()
        repeated_release, repeated_slice = build_vertical_slice(
            ROOT, "HEAD", RELEASE_ID, SLICE_ID
        )
        after = manuscript_hashes()

        self.assertEqual(canonical_json_bytes(repeated_release), canonical_json_bytes(self.release))
        self.assertEqual(canonical_json_bytes(repeated_slice), self.slice_bytes)
        self.assertEqual(after, before)

    def test_slice_selects_the_connected_opening_and_acceptance_context(self) -> None:
        payload = self.slice["payload"]

        self.assertEqual(
            [target["passageStableKey"] for target in payload["runtimeTargets"]],
            ["arch-L1", "arch-L2-accept"],
        )
        self.assertEqual(payload["runtimeTargets"][0]["connections"], ["arch-L2-accept"])
        self.assertEqual(
            payload["manifest"]["validation"]["selectedContextCounts"],
            {
                "chapters": 8,
                "chronology": 2,
                "philosophicalConstraints": 4,
                "promisePayoffs": 11,
                "voices": 1,
            },
        )
        self.assertTrue(
            all(mapping["relationship"] == "thematic-derivative" for mapping in payload["mappings"])
        )

    def test_selected_context_is_an_exact_base_release_subset(self) -> None:
        release_context = self.release["payload"]["context"]
        descriptors = {
            "chapters": "chapterId",
            "chronology": "chronologyId",
            "philosophicalConstraints": "constraintId",
            "promisePayoffs": "promiseId",
            "voices": "voiceId",
        }
        for group, id_key in descriptors.items():
            release_by_id = {record[id_key]: record for record in release_context[group]}
            for selected in self.slice["payload"]["context"][group]:
                self.assertEqual(selected, release_by_id[selected[id_key]])

    def test_recorded_release_selection_and_schema_sources_verify(self) -> None:
        verify_slice_sources(ROOT, self.slice, self.release)

    def test_tampered_slice_payload_is_rejected(self) -> None:
        tampered = copy.deepcopy(self.slice)
        tampered["payload"]["manifest"]["rationale"] = "Tampered"

        with self.assertRaisesRegex(ExportError, "contentSha256"):
            validate_slice_document(tampered, self.release)

    def test_unmapped_canonical_claim_is_rejected_with_valid_hash(self) -> None:
        tampered = copy.deepcopy(self.slice)
        tampered["payload"]["mappings"][0]["chapterIds"][0] = "er-chapter-999"
        tampered["contentSha256"] = sha256_bytes(canonical_json_bytes(tampered["payload"]))

        with self.assertRaisesRegex(ExportError, "unmapped canonical claim"):
            validate_slice_document(tampered, self.release)

    def test_disconnected_runtime_targets_are_rejected_with_valid_hash(self) -> None:
        tampered = copy.deepcopy(self.slice)
        tampered["payload"]["runtimeTargets"][0]["connections"] = []
        tampered["contentSha256"] = sha256_bytes(canonical_json_bytes(tampered["payload"]))

        with self.assertRaisesRegex(ExportError, "not connected"):
            validate_slice_document(tampered, self.release)

    def test_noncanonical_slice_json_is_rejected(self) -> None:
        pretty = (json.dumps(self.slice, indent=2, ensure_ascii=False) + "\n").encode("utf-8")

        with self.assertRaisesRegex(ExportError, "not canonical"):
            validate_serialized_slice(pretty, self.release)


if __name__ == "__main__":
    unittest.main()
