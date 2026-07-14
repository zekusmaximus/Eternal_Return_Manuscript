"""Determinism, provenance, and negative-path proofs for literary releases."""

from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

from scripts.export_runtime_source import (
    ExportError,
    build_release,
    canonical_json_bytes,
    parse_structure_map,
    sha256_bytes,
    validate_policy,
    validate_release_document,
    validate_serialized_release,
    verify_recorded_sources,
)

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
POLICY = ROOT / "editorial" / "runtime-release-policy-v1.json"


def manuscript_hashes() -> dict[str, str]:
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(MANUSCRIPT.glob("*.md"))
    }


class RuntimeSourceExporterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.release = build_release(ROOT, "HEAD", "test-literary-release-v1.0.0")
        cls.release_bytes = canonical_json_bytes(cls.release)

    def test_repeated_exports_are_byte_stable_and_non_mutating(self) -> None:
        before = manuscript_hashes()
        repeated = build_release(ROOT, "HEAD", "test-literary-release-v1.0.0")
        after = manuscript_hashes()

        self.assertEqual(canonical_json_bytes(repeated), self.release_bytes)
        self.assertEqual(after, before)
        self.assertEqual(repeated["payload"]["context"]["excerpts"], [])
        self.assertEqual(repeated["payload"]["manifest"]["validation"]["chapterCount"], 28)
        self.assertEqual(
            repeated["payload"]["manifest"]["validation"]["manuscriptFileCount"],
            28,
        )

    def test_every_manuscript_file_is_digest_only(self) -> None:
        manuscript_sources = self.release["payload"]["sourceFiles"]["manuscript"]
        self.assertEqual(len(manuscript_sources), 28)
        self.assertTrue(all(set(record) == {"path", "sha256"} for record in manuscript_sources))
        self.assertNotIn("content", json.dumps(manuscript_sources))

    def test_recorded_source_hashes_verify_against_immutable_commit(self) -> None:
        verify_recorded_sources(ROOT, self.release)

    def test_tampered_payload_is_rejected(self) -> None:
        tampered = copy.deepcopy(self.release)
        tampered["payload"]["context"]["chapters"][0]["title"] = "Tampered"

        with self.assertRaisesRegex(ExportError, "contentSha256"):
            validate_release_document(tampered)

    def test_tampered_source_hash_is_rejected_even_when_payload_hash_is_recomputed(self) -> None:
        tampered = copy.deepcopy(self.release)
        tampered["payload"]["sourceFiles"]["context"][0]["sha256"] = "0" * 64
        tampered["contentSha256"] = sha256_bytes(canonical_json_bytes(tampered["payload"]))
        validate_release_document(tampered)

        with self.assertRaisesRegex(ExportError, "source hash mismatch"):
            verify_recorded_sources(ROOT, tampered)

    def test_noncanonical_json_is_rejected(self) -> None:
        pretty = (json.dumps(self.release, indent=2, ensure_ascii=False) + "\n").encode("utf-8")

        with self.assertRaisesRegex(ExportError, "not canonical"):
            validate_serialized_release(pretty)

    def test_missing_terminal_lf_is_rejected(self) -> None:
        with self.assertRaisesRegex(ExportError, "terminal LF"):
            validate_serialized_release(self.release_bytes.rstrip(b"\n"))

    def test_unknown_schema_is_rejected(self) -> None:
        unknown = copy.deepcopy(self.release)
        unknown["schemaVersion"] = "2.0.0"

        with self.assertRaisesRegex(ExportError, "unsupported literary release schema"):
            validate_release_document(unknown)

    def test_policy_cannot_invent_excerpt_approval(self) -> None:
        policy = json.loads(POLICY.read_text(encoding="utf-8"))
        policy["approvedExcerptMarkers"] = ["invented-marker"]

        with self.assertRaisesRegex(ExportError, "refuses excerpts"):
            validate_policy(policy)

    def test_malformed_structure_map_is_rejected(self) -> None:
        malformed = "| File | Movement | Cycle/Phase | Voice | Timeline | Title |\n"

        with self.assertRaisesRegex(ExportError, "expected 1 structure rows"):
            parse_structure_map(malformed, 1)

    def test_nfc_and_crlf_are_canonicalized(self) -> None:
        raw = canonical_json_bytes({"accent": "e\u0301", "line": "a\r\nb\r"})
        decoded = raw.decode("utf-8")

        self.assertIn("é", decoded)
        self.assertNotIn("\r", decoded)
        self.assertEqual(raw[-1:], b"\n")


if __name__ == "__main__":
    unittest.main()
