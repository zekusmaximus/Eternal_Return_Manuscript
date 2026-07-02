#!/usr/bin/env python3
"""Manuscript statistics: word counts, scene counts, dialogue ratio, voice share.

Reads every chapter in /manuscript/ (reading order = NN- filename prefix) and
the chapter->voice mapping in bible/structure-map.md, then prints:

  - per-chapter: words, scene count, dialogue ratio
  - per-movement and grand totals
  - per-voice share (archaeologist / algorithm / last-human / merged / pattern)

Scene-break convention (detected from the repo): a `---` horizontal rule on
its own line separates scenes/sections inside M1/M2/M4 chapters; M3 chapters
use `##`/`###` headers instead, so for M3 files sections are counted from
headers. Dialogue ratio = words inside double quotes (straight or curly)
divided by total words -- an estimate, good for comparing chapters.

Usage:
    python scripts/stats.py            # table for all chapters
    python scripts/stats.py --csv      # machine-readable CSV to stdout
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
STRUCTURE_MAP = ROOT / "bible" / "structure-map.md"

DIALOGUE_RE = re.compile(r'"([^"\n]+)"|“([^”\n]+)”')


def load_voice_map() -> dict[str, tuple[str, str]]:
    """Parse the structure-map table -> {filename: (movement, voice)}."""
    if not STRUCTURE_MAP.exists():
        sys.exit(f"ERROR: {STRUCTURE_MAP} not found (stats needs the mapping table)")
    voice_map: dict[str, tuple[str, str]] = {}
    for line in STRUCTURE_MAP.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0].endswith(".md"):
            voice_map[cells[0]] = (cells[1], cells[3])
    if not voice_map:
        sys.exit("ERROR: no rows parsed from structure-map.md table")
    return voice_map


def scene_count(name: str, text: str) -> int:
    if re.match(r"\d{2}-m3-", name):
        headers = re.findall(r"(?m)^#{2,3} ", text)
        return max(len(headers), 1)
    breaks = re.findall(r"(?m)^---\s*$", text)
    return len(breaks) + 1


def dialogue_ratio(text: str) -> float:
    total = len(text.split())
    if not total:
        return 0.0
    quoted = sum(
        len((a or b).split()) for a, b in DIALOGUE_RE.findall(text)
    )
    return quoted / total


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--csv", action="store_true", help="CSV output")
    args = ap.parse_args()

    voice_map = load_voice_map()
    files = sorted(MANUSCRIPT.glob("[0-9][0-9]-*.md"))
    if not files:
        sys.exit(f"ERROR: no chapters in {MANUSCRIPT}")

    rows = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        movement, voice = voice_map.get(f.name, ("?", "?"))
        if movement == "?":
            print(f"WARNING: {f.name} missing from structure-map.md", file=sys.stderr)
        rows.append(
            dict(
                name=f.name,
                movement=movement,
                voice=voice,
                words=len(text.split()),
                scenes=scene_count(f.name, text),
                dialogue=dialogue_ratio(text),
            )
        )

    if args.csv:
        print("file,movement,voice,words,scenes,dialogue_ratio")
        for r in rows:
            print(f"{r['name']},{r['movement']},{r['voice']},{r['words']},{r['scenes']},{r['dialogue']:.3f}")
        return

    total = sum(r["words"] for r in rows)
    print(f"{'Chapter':<44} {'Mv':>2} {'Voice':<14} {'Words':>7} {'Scn':>4} {'Dlg%':>5}")
    print("-" * 82)
    for r in rows:
        print(
            f"{r['name']:<44} {r['movement']:>2} {r['voice']:<14} "
            f"{r['words']:>7,} {r['scenes']:>4} {r['dialogue']*100:>4.1f}%"
        )
    print("-" * 82)

    print("\nBy movement:")
    for mv in sorted({r["movement"] for r in rows}):
        sub = [r for r in rows if r["movement"] == mv]
        w = sum(r["words"] for r in sub)
        print(f"  Movement {mv}: {len(sub):>2} chapters, {w:>7,} words ({w/total*100:.1f}%)")

    print("\nBy voice (page share):")
    for v in sorted({r["voice"] for r in rows}):
        sub = [r for r in rows if r["voice"] == v]
        w = sum(r["words"] for r in sub)
        print(f"  {v:<14} {len(sub):>2} chapters, {w:>7,} words ({w/total*100:.1f}%)")

    print(f"\nTOTAL: {len(rows)} chapters, {total:,} words")


if __name__ == "__main__":
    main()
