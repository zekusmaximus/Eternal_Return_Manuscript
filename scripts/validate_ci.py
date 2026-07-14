#!/usr/bin/env python3
"""Run deterministic clean-clone release checks without changing manuscript prose."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from alternation_validator import validate_alternation
from dissolution_validator import DissolutionValidator, configure_utf8_output
from genre_checker import validate_genre
from philosophy_checker import validate_philosophy
from phrase_tracker import validate_phrases
from rhyme_tracker import validate_rhymes, validate_sequence
from rhyme_tracker_m3 import validate_rhymes_m3
from voice_validator import validate_voice

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"


def run_script(*arguments: str) -> None:
    command = [sys.executable, *arguments]
    completed = subprocess.run(command, cwd=ROOT, text=True, encoding="utf-8")
    if completed.returncode != 0:
        raise SystemExit(f"FAILED ({completed.returncode}): {' '.join(command)}")


def require_nonfailure(label: str, report: dict) -> None:
    status = report.get("status", "error")
    if status in {"error", "fail"}:
        raise SystemExit(f"FAILED: {label} returned {status}")
    print(f"{label}: {status}")


def thread_for(path: Path) -> str:
    if "-arch-" in path.name:
        return "archaeologist"
    if "-algo-" in path.name:
        return "algorithm"
    if "-lh-" in path.name:
        return "last_human"
    raise ValueError(f"Cannot infer thread for {path.name}")


def validate_movement_two() -> None:
    files = sorted(MANUSCRIPT.glob("*-m2-*.md"))
    if len(files) != 9:
        raise SystemExit(f"FAILED: expected 9 Movement Two files, found {len(files)}")

    for path in files:
        thread = thread_for(path)
        require_nonfailure(f"voice {path.name}", validate_voice(str(path), thread))
        require_nonfailure(
            f"philosophy {path.name}", validate_philosophy(str(path), thread)
        )
        require_nonfailure(f"genre {path.name}", validate_genre(str(path), thread))
        require_nonfailure(f"phrases {path.name}", validate_phrases(str(path), thread))
        require_nonfailure(f"rhymes {path.name}", validate_rhymes(str(path)))

    require_nonfailure("Movement Two rhyme sequence", validate_sequence([str(p) for p in files]))


def validate_movement_three() -> None:
    phase_files = {
        "a": MANUSCRIPT / "22-m3-phase-a-accelerating-cuts.md",
        "b": MANUSCRIPT / "23-m3-phase-b-simultaneous-narration.md",
        "c": MANUSCRIPT / "24-m3-phase-c-dissolution.md",
    }
    for phase, path in phase_files.items():
        require_nonfailure(
            f"Movement Three phase {phase} rhymes",
            validate_rhymes_m3(str(path), phase),
        )

    require_nonfailure(
        "Movement Three alternation", validate_alternation(str(phase_files["b"]))
    )

    phase_c_text = phase_files["c"].read_text(encoding="utf-8")
    dissolution = DissolutionValidator(phase_c_text).validate()
    if not dissolution["overall_pass"]:
        raise SystemExit(f"FAILED: Movement Three dissolution {dissolution['passes']}")
    print("Movement Three dissolution: pass")


def main() -> None:
    configure_utf8_output()
    run_script("scripts/stats.py")
    with tempfile.TemporaryDirectory() as temp_dir:
        run_script("scripts/assemble.py", "--out", str(Path(temp_dir) / "manuscript.md"))
    run_script("scripts/continuity.py", "--check")
    run_script("scripts/edit_status.py")
    validate_movement_two()
    validate_movement_three()
    print("All clean-clone manuscript release checks passed. OK")


if __name__ == "__main__":
    main()
