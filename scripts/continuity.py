#!/usr/bin/env python3
"""Build bible/name-index.md: recurring proper nouns with locations and variants.

Scans every chapter in /manuscript/ for capitalized token runs that are not
sentence-start artifacts, keeps every candidate that appears in 2+ places,
and writes a markdown index: term -> chapters where it appears, plus
near-miss spelling variants flagged via difflib similarity (candidate pairs
like 'Phantasm'/'Pantasm' or inconsistent transliterations).

This is a CANDIDATE GENERATOR for human review, not an authority: it will
include some ordinary capitalized words and may group unrelated near-misses.

Usage:
    python scripts/continuity.py             # writes bible/name-index.md
    python scripts/continuity.py --min 3     # require 3+ occurrences
    python scripts/continuity.py --stdout    # print instead of writing
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
OUT = ROOT / "bible" / "name-index.md"

# Words that begin sentences constantly and are never names in this book.
STOP = {
    "The", "A", "An", "And", "But", "Or", "Not", "No", "Yes", "It", "Its",
    "I", "He", "She", "They", "We", "You", "My", "His", "Her", "Their",
    "Our", "Your", "This", "That", "These", "Those", "There", "Here",
    "What", "When", "Where", "Which", "Who", "Whose", "Why", "How",
    "Then", "Now", "So", "As", "At", "In", "On", "Of", "For", "To", "From",
    "With", "Without", "Into", "Over", "Under", "After", "Before", "Between",
    "Again", "Against", "Through", "Because", "If", "Each", "Every", "All",
    "Some", "Something", "Someone", "Nothing", "Everything", "Anything",
    "Once", "Twice", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "First", "Second", "Third", "Do", "Does", "Did",
    "Is", "Are", "Was", "Were", "Be", "Been", "Being", "Have", "Has", "Had",
    "Will", "Would", "Can", "Could", "Should", "Must", "May", "Might",
    "Let", "Even", "Still", "Just", "Only", "Also", "Perhaps", "Maybe",
    "Instead", "Inside", "Outside", "Beneath", "Above", "Below", "Behind",
    "Around", "Beyond", "Until", "While", "During", "Since", "Both",
    "Neither", "Either", "Another", "Other", "Others", "Same", "Such",
    "Most", "More", "Less", "Least", "Many", "Much", "Few", "Half",
    "Today", "Tomorrow", "Yesterday", "Tonight", "Morning", "Evening",
    "Night", "Day", "Days", "Years", "Hours", "Minutes", "Seconds",
    "Somewhere", "Nowhere", "Everywhere", "Anywhere", "Never", "Always",
    "Sometimes", "Already", "Almost", "Enough", "Too", "Very", "Rather",
    "Except", "Despite", "Although", "Though", "Therefore", "Thus", "Hence",
    "Meanwhile", "Later", "Earlier", "Soon", "Finally", "Suddenly", "Slowly",
    "Nothing", "None", "Any", "Whatever", "Whoever", "However", "Whether",
    "Down", "Up", "Out", "Off", "Back", "Away", "Across", "Along", "Toward",
    "Towards", "Within", "Upon", "About", "Above",
}

# Multi-word run of Capitalized tokens (allows internal hyphen), e.g.
# "Mildred Higgins", "Archive", "Last Human".
TOKEN_RE = re.compile(r"\b([A-Z][a-zA-Z0-9’'-]*(?:\s+[A-Z][a-zA-Z0-9’'-]*)*)\b")


def harvest(text: str) -> list[str]:
    """Candidate proper-noun strings from one chapter."""
    found = []
    for m in TOKEN_RE.finditer(text):
        term = re.sub(r"\s+", " ", m.group(1)).strip()
        words = term.split()
        # strip leading stopwords (sentence starts)
        while words and words[0] in STOP:
            words = words[1:]
        while words and words[-1] in STOP:
            words = words[:-1]
        if not words:
            continue
        term = " ".join(words)
        if len(term) < 3 or term in STOP:
            continue
        found.append(term)
    return found


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--min", type=int, default=2, help="minimum occurrences (default 2)")
    ap.add_argument("--stdout", action="store_true", help="print instead of writing file")
    args = ap.parse_args()

    files = sorted(MANUSCRIPT.glob("[0-9][0-9]-*.md"))
    if not files:
        sys.exit(f"ERROR: no chapters in {MANUSCRIPT}")

    occurrences: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for f in files:
        for term in harvest(f.read_text(encoding="utf-8")):
            occurrences[term][f.name] += 1

    kept = {
        t: locs
        for t, locs in occurrences.items()
        if sum(locs.values()) >= args.min
    }

    # near-miss variants among kept terms (and against dropped singletons)
    names = sorted(kept)
    variants: dict[str, list[str]] = defaultdict(list)
    lower_seen: dict[str, str] = {}
    for t in names:
        key = t.lower()
        if key in lower_seen and lower_seen[key] != t:
            variants[lower_seen[key]].append(t)
        else:
            lower_seen[key] = t
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if a.lower() == b.lower():
                continue
            if abs(len(a) - len(b)) <= 2 and difflib.SequenceMatcher(
                None, a.lower(), b.lower()
            ).ratio() >= 0.86:
                variants[a].append(b)

    lines = [
        "# Name Index (generated)",
        "",
        f"> Generated by `python scripts/continuity.py` over {len(files)} chapters.",
        "> Candidate generator for human review -- NOT an authority. Regenerate after any prose change.",
        "",
        f"{len(kept)} recurring capitalized terms ({args.min}+ occurrences).",
        "",
        "## Near-miss variants (check for inconsistent spellings)",
        "",
    ]
    if variants:
        for a in sorted(variants):
            for b in sorted(set(variants[a])):
                a_n = sum(kept.get(a, {}).values())
                b_n = sum(kept.get(b, {}).values())
                lines.append(f"- **{a}** ({a_n}x) vs **{b}** ({b_n}x)")
    else:
        lines.append("- none detected")
    lines += ["", "## Index", ""]
    for t in sorted(kept, key=lambda x: (-sum(kept[x].values()), x)):
        locs = kept[t]
        total = sum(locs.values())
        chapters = ", ".join(
            f"{name[:2]}({n})" for name, n in sorted(locs.items())
        )
        lines.append(f"- **{t}** — {total}x in: {chapters}")

    out_text = "\n".join(lines) + "\n"
    if args.stdout:
        print(out_text)
    else:
        OUT.write_text(out_text, encoding="utf-8")
        print(f"Wrote {OUT} ({len(kept)} terms, {len(variants)} variant groups)")


if __name__ == "__main__":
    main()
