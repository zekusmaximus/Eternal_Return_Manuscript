# Mechanical issues log

Defects found in manuscript or infrastructure files that this session is **not permitted to fix in prose** (manuscript files are read-only to editorial sessions). Fix these only inside an approved revision-roadmap item, or as operator one-offs.

## In manuscript files (read-only — logged, not fixed)

1. **`manuscript/24-m3-phase-b-simultaneous-narration.md` — passage numbering skips 2.** Headers run "Passage 1: The Breath Releases" → "Passage 3: Transition to Sentence". Ten passages are intended (manifest `passage_count_actual: 10`) but only nine headers exist. Either Passage 2 was silently merged into Passage 1 at drafting time or the headers were misnumbered. Present in the pre-revision compiles too, so it predates Revision One. Decide: renumber headers, or restore/write the missing passage.
2. **`manuscript/26-m3-convergence.md` is unrevised early prose (2026-01-22)** stitched into the book between Phase C and Movement Four. It predates all of Movements Two–Four's drafting and all revision passes; flagged for developmental review (see DEV-EDIT-REPORT).

## In stale builds (archived; informational)

3. **`archive/compiled1/*` and `archive/legacy/compiled/*` truncate every Movement Four section's final line.** The compiled novel ends "What returns—", dropping the final word "*continues.*". The DOCX (`archive/compiled1/entire-manuscript.docx`, added in PR #31) inherits this. **Any copy of that DOCX in circulation is missing the book's last word and contains pre-revision text.**
4. **`archive/compiled1/*` predates Revision One** — contains ~5,000 words that Revision One cut (verified against commit `45996c6`).

## In infrastructure files (fixed or fixable by tooling edits)

5. **`outlines/manifest.json` word counts predate Revision One** (e.g. m2-algo-02 recorded at 4,397 words; actual 2,245). Counts are historical; `python scripts/stats.py` is the live source. A `_note` key records this.
6. **`.gitignore` contained two stray `nul` lines** (Windows redirect artifact) — removed in Phase 1; `build/` and `__pycache__/` added.
7. **`bible/worldbuilding/Pantasm_Reference.png` filename typo** ("Pantasm" for "Phantasm"). Left as-is to avoid breaking external references; rename any time.
8. **`README.md` status/structure sections were frozen mid-draft** (said "drafting Movement Two, 52%") — updated in Phase 1.
9. **Legacy validators (`scripts/*_validator.py` etc.) take explicit file paths** and some docstrings still show `drafts/…` examples; they run fine against `manuscript/…` paths. `scripts/compile_movement.py` is hardcoded to the old layout and is superseded by `scripts/assemble.py` (archived in Phase 2).
