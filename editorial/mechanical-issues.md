# Mechanical issues log

Defects found in manuscript or infrastructure files that this session is **not permitted to fix in prose** (manuscript files are read-only to editorial sessions). Fix these only inside an approved revision-roadmap item, or as operator one-offs.

> Chapter numbers below are **pre-R-05** numbers (the numbering all Pass A–C records use). R-05 (2026-07-02) renumbered seven M1 files: 03→04, 04→05, 05→11, 09→12, 10→03, 11→09, 12→10 — see the mapping note in `REVISION-ROADMAP.md`. R-04 (same day) then merged original chs. 07+08 and renumbered again — the CUMULATIVE original→current mapping lives in the renumbering notes at the top of `BOOK-MAP.md`.

## In manuscript files (read-only — logged, not fixed)

1. **`manuscript/24-m3-phase-b-simultaneous-narration.md` — passage numbering skips 2.** Headers run "Passage 1: The Breath Releases" → "Passage 3: Transition to Sentence". Ten passages are intended (manifest `passage_count_actual: 10`) but only nine headers exist. Either Passage 2 was silently merged into Passage 1 at drafting time or the headers were misnumbered. Present in the pre-revision compiles too, so it predates Revision One. Decide: renumber headers, or restore/write the missing passage. **Update (R-09, 2026-07-02)**: the file (current name `manuscript/23-m3-phase-b-simultaneous-narration.md`) now also skips 8 — R-09 merged passages 7+8 under the "Passage 7: Fragments" header and, at operator ruling (option (a)), left the "Passage 9"/"Passage 10" headers untouched to keep the protected passage 9 byte-identical. Headers now run 1, 3, 4, 5, 6, 7, 9, 10. Both skips (2 and 8) to be resolved together by R-14's global renumber ruling.
2. **`manuscript/26-m3-convergence.md` is unrevised early prose (2026-01-22)** stitched into the book between Phase C and Movement Four. It predates all of Movements Two–Four's drafting and all revision passes; flagged for developmental review (see DEV-EDIT-REPORT). **RESOLVED by R-06 (2026-07-02)**: the chapter's load-bearing test sequence was folded verbatim into Phase C and the rest retired to `archive/superseded/25-m3-convergence.md`; no unrevised early prose remains in the manuscript.
3. **Drafting-scaffold language leaked into prose** (found during the Pass A read; all need operator decision + roadmap items, never silent fixes):
   - ch. 20 `20-m2-arch-3-the-merge.md`: "The reader should feel: *He's almost gone, but he's still him—for now.*" (staged as intrusive thought, but fourth-wall); "At the threshold now. Movement Three approaching."; "Movement Three will complete it."
   - ch. 23 Section 7 opens "Short. The merge accelerating." (stage direction as prose)
   - ch. 24 Passage 3: bare stage directions ("The Last Human's paragraph begins normally, then breaks—", "The Algorithm picks up the thought…", "The Archaeologist picks up, his syntax contaminated—")
   - ch. 28: "Her farewell to me in Movement Two"; "The handoff that Movement Four requires"
   - ch. 29: "not the unconscious tracing that disturbed me in Movement One"
   (The coda's title echo — "Not the title of a story but the structure of what is" — is the one *earned* meta gesture; these others are unmarked register breaks.)
4. **`manuscript/24-m3-phase-b-simultaneous-narration.md` Passage 4 has no spaces after sentence-ending periods** ("The form holds.I process the holding"). Possibly intentional simultaneity typography, possibly a defect — operator must rule before any fix.
5. **ch. 24: missing "Passage 2" header** — a bare double `---` sits between Passage 1's LH block and the unlabeled Arch/Algo blocks; headers jump 1→3.
6. **ch. 10 `10-m1-lh-1-solitude.md`** (file renamed `03-m1-lh-1-solitude.md` by R-05, 2026-07-02): "the silence is what evolved here, and **I are** the intrusion" — grammatical slip before pronoun instability is established as a device. **RESOLVED by R-01 (2026-07-02)**: fixed to "I am" inside the approved R-01 diff (the roadmap item explicitly includes this fix).
7. **ch. 17**: "Mildred Higgins. Consciousness fragment **7,847,293**" vs. her canonical instance **#2,847,102**; also "The dead **woman** will wake in her substrate" where the extraction is Roberto Martinez (male).
8. **Marcus Wei's instance number differs three times**: #3,102,458 (ch. 09), #3,847,102 (ch. 15), #847,293 (ch. 18); ch. 15 also has a stray "#847,102".
9. **The protocols' timestamp is dated three incompatible ways**: "predates my career by twenty years… my birth by five" (ch. 02), "forty-seven years ago" (ch. 05), "fifteen years before I was born" (chs. 26, 29).
10. **ch. 28**: Mildred's remembered farewell ("You already know what you are, dear…") does not match her actual ch. 21 dialogue; "billions of preserved humans" vs. canonical 4,847,293.
11. **Timeline-months drift**: 63 → 55 (ch. 02) → 57 (ch. 03 price rise) → "fifty-five" (chs. 04–05) → "fifty-three" (ch. 14) → "fifty-two" (ch. 17). The +6% price adjustment (55→57) is never re-reconciled.
12. **ch. 05**: "hands that have spent twenty years learning how to excavate the dead" — he is 34, has been saving 11 years, and the industry appears younger than 20 years.

## In stale builds (archived; informational)

13. **`archive/compiled1/*` and `archive/legacy/compiled/*` truncate every Movement Four section's final line.** The compiled novel ends "What returns—", dropping the final word "*continues.*". The DOCX (`archive/compiled1/entire-manuscript.docx`, added in PR #31) inherits this. **Any copy of that DOCX in circulation is missing the book's last word and contains pre-revision text.**
14. **`archive/compiled1/*` predates Revision One** — contains ~5,000 words that Revision One cut (verified against commit `45996c6`).

## In infrastructure files (fixed or fixable by tooling edits)

15. **`outlines/manifest.json` word counts predate Revision One** (e.g. m2-algo-02 recorded at 4,397 words; actual 2,245). Counts are historical; `python scripts/stats.py` is the live source. A `_note` key records this.
16. **`.gitignore` contained two stray `nul` lines** (Windows redirect artifact) — removed in Phase 1; `build/` and `__pycache__/` added.
17. **`bible/worldbuilding/Pantasm_Reference.png` filename typo** ("Pantasm" for "Phantasm"). Left as-is to avoid breaking external references; rename any time.
18. **`README.md` status/structure sections were frozen mid-draft** (said "drafting Movement Two, 52%") — updated in Phase 1.
19. **Legacy validators (`scripts/*_validator.py` etc.) take explicit file paths** and some docstrings still show `drafts/…` examples; they run fine against `manuscript/…` paths. `scripts/compile_movement.py` is hardcoded to the old layout and is superseded by `scripts/assemble.py` (archived in Phase 2).
