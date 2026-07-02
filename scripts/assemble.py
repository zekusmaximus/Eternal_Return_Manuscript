#!/usr/bin/env python3
"""Assemble the canonical manuscript into build/full-manuscript.md.

Concatenates every chapter file in /manuscript/ in reading order (the
zero-padded NN- filename prefix), inserting movement headers, and then
VERIFIES the assembly: the last non-empty line of every source chapter
must appear verbatim in the output. If any chapter's ending is missing,
the script exits non-zero and lists the affected chapters.

That verification exists because the legacy compile (archive/compiled1/)
silently dropped the final line of all four Movement Four sections --
the compiled novel ended "What returns--" without its final word.

Usage:
    python scripts/assemble.py            # writes build/full-manuscript.md
    python scripts/assemble.py --out X.md # custom output path
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"

MOVEMENT_TITLES = {
    "m1": "Movement One: Exposition",
    "m2": "Movement Two: Entanglement",
    "m3": "Movement Three: Recognition",
    "m4": "Movement Four: Affirmation",
}


def chapter_files() -> list[Path]:
    files = sorted(
        p for p in MANUSCRIPT.glob("[0-9][0-9]-*.md") if p.is_file()
    )
    if not files:
        sys.exit(f"ERROR: no chapter files found in {MANUSCRIPT}")
    return files


def movement_of(path: Path) -> str:
    m = re.match(r"\d{2}-(m\d)-", path.name)
    return m.group(1) if m else ""


def last_nonempty_line(text: str) -> str:
    for line in reversed(text.splitlines()):
        stripped = line.strip()
        if stripped and stripped != "---":
            return stripped
    return ""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--out",
        default=str(ROOT / "build" / "full-manuscript.md"),
        help="output path (default: build/full-manuscript.md)",
    )
    args = ap.parse_args()

    files = chapter_files()
    parts: list[str] = ["# The Eternal Return of the Digital Self\n"]
    current_movement = None
    endings: list[tuple[Path, str]] = []

    for f in files:
        text = f.read_text(encoding="utf-8")
        mv = movement_of(f)
        if mv != current_movement:
            current_movement = mv
            title = MOVEMENT_TITLES.get(mv, mv)
            parts.append(f"\n\n# {title}\n")
        parts.append("\n\n" + text.strip() + "\n")
        endings.append((f, last_nonempty_line(text)))

    output = "".join(parts).rstrip() + "\n"

    # --- mandatory verification: every chapter ending must survive assembly
    missing = [
        (f, end) for f, end in endings if end and end not in output
    ]
    empties = [f for f, end in endings if not end]
    if missing or empties:
        print("ASSEMBLY VERIFICATION FAILED", file=sys.stderr)
        for f, end in missing:
            print(f"  MISSING ENDING: {f.name}: {end[:80]!r}", file=sys.stderr)
        for f in empties:
            print(f"  EMPTY CHAPTER: {f.name}", file=sys.stderr)
        sys.exit(1)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")

    words = len(output.split())
    print(f"Assembled {len(files)} chapters -> {out}")
    print(f"Total words: {words:,}")
    print("Verification: all chapter endings present. OK")


if __name__ == "__main__":
    main()
