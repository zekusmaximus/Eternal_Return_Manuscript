# Archive

Nothing in this directory is deleted from version control — "archived" means moved here via `git mv` (full history preserved). Nothing here is canonical. If you need the current novel text, it is in `/manuscript/`; if you need reference material, it is in `/bible/`; prior editorial records are in `/editorial/revision-one/`.

Archived by the 2026-07-02 reorganization session (see `editorial/REORG_PLAN.md` for the complete old→new mapping and `editorial/INVENTORY.md` for the evidence behind each classification).

## Contents

### `compiled1/` — stale compiled manuscript (IMPORTANT)
The full-book and per-movement compiles plus `entire-manuscript.docx`. **Compiled from pre-Revision One text**: they contain passages Revision One deleted (verified line-by-line against commit `45996c6`) and are ~5,000 words heavier than the current manuscript. **They also truncate the final line of every Movement Four section** — the compiled book ends "What returns—" and drops the novel's final word "*continues.*". Do not send this file to anyone. Rebuild with `python scripts/assemble.py`, which verifies chapter endings.

### `legacy/` — the old `.archive/` tree, moved intact
- `compiled/` — the earlier compile of the same pre-revision text (with encoding artifacts; `compiled1` was its UTF-8 re-encode). Same truncation bug.
- `Brainstorm1.md`, `brainstorm2.md` — pre-drafting brainstorms (mechanism, tone, genre). Historical.
- `SONNET_IMPLEMENTATION_PROMPT.md`, `next_session_prompt.md` — one-off session prompts.
- `claude-legacy/` — pre-`protocols/` Claude configuration and templates, superseded 2026-01-20.
- `README.md` — the old archive's own index.

### `drafting-records/` — per-scene drafting apparatus (mirrors old `drafts/` layout)
- `*-prompt.md` (16) — the single-use AI drafting prompts that produced each scene/section.
- `*.context.md` (30) — retrospective per-scene records: rhymes caught/released, validation results, continuity facts, handoff notes. **These embed continuity data not always recorded elsewhere** (e.g. Mildred Higgins instance #2,847,102 and her 99.9%→82.7% integrity curve; consciousness count 4,847,293; KL-7 protocol mechanics). They are kept intact as a continuity fallback; `bible/name-index.md` (generated) is the live cross-reference.
- `movement-one/archaeologist/first-bleed.md` + `.context.md` — a superseded **alternate prose scene** ("The First Bleed", id m1-arch-04b). Its passages were absorbed near-verbatim into what is now `manuscript/14-m2-arch-1-the-bleed.md` (documented in that scene's context record). Not canonical; do not reintegrate.

### `scripts/` — superseded script material (mirrors old `scripts/` layout)
- `archive/movement_one/` — Movement One-era validator versions.
- `compiled/` — stub outputs of `compile_movement.py` test runs.
- `__pycache__/` — Python bytecode cache that had been committed; now ignored via `.gitignore`.
- `validation-outputs/*.json` — one-off validator outputs (2026-01-23) against drafts that have since been revised.
- `validation-script-review-prompt.md`, `validation-scripts-review-report.md` — one-off QA of the validators.

### `examples/` — pre-drafting voice exercises and an early braided-style sample.

### `scaffolding/` — superseded planning
- `movement-two-prep.md` — pre-draft consolidation of the brainstorms ("before archiving"); superseded by the completed draft and by `outlines/movement-two-braiding.md`.
- `rhymes/movement-tracking.md` — v1.0 rhyme tracker stub; superseded by `bible/rhyme-registry.md`.

### `progress.md` — drafting dashboard frozen at "Movement Two Cycle 2 in progress" (self-declared non-canonical; superseded by the completed draft and `editorial/STATE.md`).

## Unclear items awaiting operator review

None. Every archived file has a determined status (see `editorial/INVENTORY.md` §2.7 for the closest calls and how they were resolved).
