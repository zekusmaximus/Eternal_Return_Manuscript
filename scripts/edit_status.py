#!/usr/bin/env python3
"""One-screen editorial session status from editorial/STATE.md.

Reads editorial/STATE.md (the machine-and-human-readable session state kept
by revision sessions) plus the roadmap checklist, and prints: chapters
analyzed, roadmap items open/done by tier, operator decisions, current item,
and the next action.

Usage:
    python scripts/edit_status.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "editorial" / "STATE.md"
ROADMAP = ROOT / "editorial" / "REVISION-ROADMAP.md"
CHAPTER_NOTES = ROOT / "editorial" / "chapters"
MANUSCRIPT = ROOT / "manuscript"


def configure_utf8_output() -> None:
    """Emit stable UTF-8 even when a Windows console defaults to CP1252."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="strict")


def field(text: str, name: str) -> str:
    m = re.search(rf"(?im)^[-*]?\s*\*?\*?{re.escape(name)}\*?\*?\s*:\s*(.+)$", text)
    return m.group(1).strip() if m else "?"


def main() -> None:
    configure_utf8_output()
    print("=" * 62)
    print("  ETERNAL RETURN — editorial status")
    print("=" * 62)

    chapters = len(list(MANUSCRIPT.glob("[0-9][0-9]-*.md")))
    notes = len(list(CHAPTER_NOTES.glob("*.md"))) if CHAPTER_NOTES.exists() else 0
    print(f"Chapters: {chapters} in /manuscript/, {notes} with dev notes in editorial/chapters/")

    if ROADMAP.exists():
        rm = ROADMAP.read_text(encoding="utf-8")
        done = len(re.findall(r"(?m)^\s*- \[x\]", rm, re.I))
        open_ = len(re.findall(r"(?m)^\s*- \[ \]", rm))
        print(f"Roadmap:  {done} done / {open_} open ({done + open_} total)")
        for tier in re.findall(r"(?m)^##+\s+(Tier[^\n]*)", rm):
            print(f"          - {tier.strip()}")
    else:
        print("Roadmap:  editorial/REVISION-ROADMAP.md not found")

    if not STATE.exists():
        print("\nSTATE:    editorial/STATE.md not found — run a Phase 4 session first.")
        sys.exit(1)

    st = STATE.read_text(encoding="utf-8")
    print()
    print(f"Current item:  {field(st, 'Current item')}")
    print(f"Last updated:  {field(st, 'Last updated')}")
    print(f"Items done:    {field(st, 'Items done')}")

    dec = re.search(r"(?ims)^##+\s*Operator decisions\s*$(.*?)(?=^##|\Z)", st)
    if dec:
        rows = [l for l in dec.group(1).splitlines() if l.strip().startswith("|")][2:]
        accepted = sum("accepted" in r.lower() for r in rows)
        rejected = sum("rejected" in r.lower() for r in rows)
        deferred = sum("deferred" in r.lower() for r in rows)
        pending = len(rows) - accepted - rejected - deferred
        print(f"Decisions:     {accepted} accepted, {rejected} rejected, "
              f"{deferred} deferred, {pending} pending")

    print()
    print(f"NEXT ACTION:   {field(st, 'Next action')}")
    print("=" * 62)


if __name__ == "__main__":
    main()
