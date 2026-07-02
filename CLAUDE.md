# CLAUDE.md — standing rules for this repository

This repository contains the novel *The Eternal Return of the Digital Self* (complete draft, ~90,600 words) and its editorial apparatus. These rules bind every AI-assisted session. They exist because the manuscript prose is the crown jewel of this repo.

## Hard rules

1. **Never delete a file.** "Archiving" means `git mv` into `archive/` (with a line added to `archive/README.md`). Nothing is ever removed from version control.
2. **Manuscript prose is read-only by default.** The files in `/manuscript/` may not be edited, reformatted, re-encoded, or renamed except inside an **approved revision-roadmap item** (see `editorial/WORKFLOW.md`): the operator picks an item from `editorial/REVISION-ROADMAP.md`, the session proposes the change as a plan in chat, and only after explicit operator approval *in that session* may the item's affected files be edited. Never batch multiple roadmap items into one change.
3. **Mechanical defects in manuscript files are logged, not fixed.** Broken links, encoding artifacts, numbering skips → add to `editorial/mechanical-issues.md`.
4. **All editorial output goes under `/editorial/`** (per-chapter notes in `editorial/chapters/`). Never overwrite prior editorial records (`editorial/revision-one/`, `editorial/DEV-EDIT-REPORT.md`, …) — extend them, and flag disagreements with prior notes explicitly rather than silently contradicting them.
5. **Work on the branch the session designates; one concern per commit.** Revision commits use `revise: <item-id> <summary>`; editorial-session commits use `phase N: <summary>` or a similarly scoped message.
6. **Scripts are Python 3, stdlib only, cross-platform** (the operator runs Windows/PowerShell). Invoke as `python scripts/<name>.py`. Use `pathlib`, forward slashes, and UTF-8 (`encoding="utf-8"` on every open). No bash-isms, no Makefiles.
7. **After any manuscript change**: run `python scripts/assemble.py` (its ending-verification is mandatory — the legacy compiler once silently dropped the book's final line), update the touched chapters' entries in `editorial/BOOK-MAP.md`, update `editorial/STATE.md`, then commit.

## Orientation (read these before working)

| What | Where |
|---|---|
| The novel, 30 chapters in reading order | `manuscript/NN-mX-thread-slug.md` |
| Chapter ↔ movement/voice/timeline map | `bible/structure-map.md` |
| Story bible (voices, worldbuilding, philosophy, rhyme registry) | `bible/` |
| Book map (per-chapter structure + promise/payoff ledger) | `editorial/BOOK-MAP.md` |
| Developmental edit findings | `editorial/DEV-EDIT-REPORT.md` |
| Prioritized revision checklist | `editorial/REVISION-ROADMAP.md` |
| Session state / what to do next | `editorial/STATE.md` → `python scripts/edit_status.py` |
| Standing revision procedure | `editorial/WORKFLOW.md` |
| Prior revision session (Revision One) records | `editorial/revision-one/` |
| Why files are where they are | `editorial/INVENTORY.md`, `editorial/REORG_PLAN.md`, `archive/README.md` |

## Things past sessions got wrong (do not repeat)

- **Do not use `archive/compiled1/`** (or its DOCX) as the manuscript: it is pre-Revision One text and its Movement Four endings are truncated. Rebuild with `python scripts/assemble.py`.
- **Do not trust `outlines/manifest.json` word counts** — they predate Revision One. Use `python scripts/stats.py`.
- **Do not "fix" designed repetition.** The phrase bleeding ("I find myself / I find myself found"), the 15 sensory rhymes, and the rhyme handoff chains are architecture, not redundancy — see `editorial/revision-one/revision-plan.md` ("What NOT to Do") and `bible/rhyme-registry.md` before cutting any repeated phrase.
- **Do not violate the Four Shackles** (`bible/philosophy-constraints.md`): the three protagonists are not "the same person," not opposites, not analogies, not resemblances. Editorial suggestions that flatten this violate the book's philosophical core.
