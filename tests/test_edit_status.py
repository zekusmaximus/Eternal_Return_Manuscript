"""Cross-platform smoke tests for the editorial status command."""
from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "edit_status.py"


class EditStatusSmokeTest(unittest.TestCase):
    def test_status_output_is_utf8_when_parent_requests_cp1252(self) -> None:
        """The Windows CP1252 baseline must not crash on the next-action arrow."""
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "cp1252"
        env["PYTHONUTF8"] = "0"

        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            env=env,
            capture_output=True,
            check=False,
        )

        stdout = result.stdout.decode("utf-8", errors="strict")
        stderr = result.stderr.decode("utf-8", errors="strict")
        self.assertEqual(result.returncode, 0, stderr)
        self.assertIn("NEXT ACTION:", stdout)
        self.assertIn("→", stdout)


if __name__ == "__main__":
    unittest.main()
