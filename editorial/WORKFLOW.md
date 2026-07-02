# Revision workflow (standing procedure)

The loop every revision session follows. It exists to keep the manuscript safe: prose is read-only *except* inside an approved roadmap item, and only for that item's affected files.

## The loop

1. **Operator picks one item** from `editorial/REVISION-ROADMAP.md` (respect the suggested order and each item's dependency notes; R-05's decision gates R-04).
2. **Session loads context**: `editorial/STATE.md` → the roadmap item → the item's affected chapters (full text) → the relevant `editorial/chapters/NN-*.md` notes → any bible files the item cites. Run `python scripts/edit_status.py` first for orientation.
3. **Session proposes the revision as a plan in chat** — the exact edits (quoted before/after for prose changes, or the full move list for reorders), the rationale, and the done-condition check it will run. **No file is touched yet.**
4. **Operator approves explicitly in that session.** Approval of the plan is approval for *those files, that item, that session* — nothing carries over. If the operator amends, re-propose; if rejected, record the decision in STATE.md and stop.
5. **Session executes** — edits only the item's affected files. Renames/merges use `git mv`. Nothing is deleted (superseded material moves to `archive/` with a line in `archive/README.md`).
6. **Verify**:
   - `python scripts/assemble.py` — must pass its chapter-ending verification (mandatory; this is the check that catches the truncation failure mode).
   - `python scripts/stats.py` — confirm word-count deltas match the plan.
   - If rhymes/voice were touched: `python scripts/rhyme_tracker.py` / `scripts/voice_validator.py` on the changed files; `python scripts/continuity.py` after any naming/number changes.
7. **Update the records**: BOOK-MAP.md entries for every touched chapter; mark the roadmap checkbox; STATE.md (decision → accepted, items-done count, session log line, next action); mechanical-issues.md if the item resolves logged defects.
8. **Commit**: `revise: <item-id> <summary>` — **one roadmap item per commit, never batched.** Structural moves (R-04/05/06) are their own commits even if small follow-up fixes are tempting.

## Standing rules (inherited from CLAUDE.md — repeated here because this file is the operative checklist)

- Never delete; archive via `git mv` + `archive/README.md` entry.
- Never edit manuscript prose outside step 5 of an approved item.
- Mechanical defects noticed en route go into `editorial/mechanical-issues.md`, not into the diff.
- Don't "fix" designed repetition (phrase bleeding, the 15 rhymes, handoff chains) — check `bible/rhyme-registry.md` and `editorial/revision-one/revision-plan.md` "What NOT to Do" before cutting anything repeated.
- Respect the reorder constraints recorded in roadmap items (04→09/13 order; 18→19→20 adjacency).
- Scripts are Python 3 stdlib, `python scripts/<name>.py`, UTF-8, pathlib — the operator runs Windows/PowerShell.

## Session start (copy-paste for the operator)

> Read editorial/STATE.md, editorial/WORKFLOW.md, and roadmap item <ID>. Load the affected chapters and their editorial/chapters notes. Propose the revision as a plan in chat and wait for my approval before touching any file.

## When an item is rejected or deferred

Record it in STATE.md's decision table with a one-line reason. A rejected structural item (e.g. R-05 option (c)) may unlock simplified versions of later items — note that in the roadmap rather than editing history.
