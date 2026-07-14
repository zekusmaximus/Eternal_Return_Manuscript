"""Assembly integrity regression tests."""

import unittest
from pathlib import Path

from scripts.assemble import last_nonempty_line, verify_endings


class AssemblyVerificationTests(unittest.TestCase):
    def test_truncated_synthetic_ending_is_reported(self) -> None:
        source = "Opening line.\n\nThe synthetic ending must survive.\n"
        chapter = Path("99-m4-synthetic-ending.md")

        missing, empties = verify_endings(
            [(chapter, last_nonempty_line(source))],
            "Opening line.\n",
        )

        self.assertEqual(empties, [])
        self.assertEqual(missing, [(chapter, "The synthetic ending must survive.")])


if __name__ == "__main__":
    unittest.main()
