"""Regression tests for the accepted canonical Movement Three validator baseline."""

import unittest
from pathlib import Path

from scripts.dissolution_validator import DissolutionValidator
from scripts.rhyme_tracker_m3 import validate_rhymes_m3

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"


class MovementThreeValidatorTests(unittest.TestCase):
    def test_phase_c_dissolution_accepts_canonical_text(self) -> None:
        text = (MANUSCRIPT / "24-m3-phase-c-dissolution.md").read_text(encoding="utf-8")
        report = DissolutionValidator(text).validate()

        self.assertTrue(report["overall_pass"], report["passes"])
        self.assertGreaterEqual(report["rhymes"]["coverage_pct"], 90)

    def test_phase_c_rhyme_drift_is_warning_not_tool_failure(self) -> None:
        report = validate_rhymes_m3(
            str(MANUSCRIPT / "24-m3-phase-c-dissolution.md"), "c"
        )

        self.assertEqual(report["status"], "warn")
        self.assertGreaterEqual(report["summary"]["coverage"], 90)


if __name__ == "__main__":
    unittest.main()
