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

## Narramorph interactive-edition proposals

Narramorph's [content-authority ADR](https://github.com/zekusmaximus/Narramorph/blob/main/docs/adr/0002-content-authority-and-edition-semantics.md) defines the shared edition boundary. This repository owns the canonical long-form manuscript and editorial constraints; Narramorph owns its separately authored interactive runtime edition. A reader-specific journey export is a derivative record, not an authoring source.

A manuscript/editorial change can inform Narramorph only through this sequence:

1. Complete the approval loop above for any canonical prose change. Metadata/tooling-only work does not grant prose-edit permission.
2. Produce a versioned literary-release artifact containing approved structured context and only excerpts that have an explicit interactive-use approval record.
3. Record the immutable manuscript commit, editorial release ID, contract/schema version, license/permission, input hashes, deterministic artifact hash, and validation results.
4. Transfer that immutable artifact deliberately. Narramorph stages and validates it, then produces a semantic diff; it does not fetch this repository's default branch.
5. Editorial review decides whether changed identities, chronology, terminology, philosophical constraints, causal promises/payoffs, ending claims, or approved excerpts are acceptable for the interactive edition.
6. Narramorph accepts release metadata and concordance through a pull request. Any runtime-prose proposal is a separate authored diff with the applicable editorial review.
7. Rollback selects or reverts to a prior accepted Narramorph package. It never edits this repository or rewrites manuscript history.

### Do-not-overwrite boundary

- No exporter, validator, or Narramorph-related command may modify, rename, reformat, or re-encode files beneath `manuscript/`.
- Ordinary exporter output belongs beneath git-ignored `build/`; an intentional release artifact is reviewed and versioned separately.
- This repository never writes into a Narramorph checkout or rewrites Narramorph runtime prose.
- Narramorph never writes into this repository and never fetches its default branch during build or runtime.
- Reader exports cannot be imported as canonical or runtime authoring inputs.
- Generated artifacts must declare their source and do-not-edit boundary.

If a proposed tool cannot preserve these boundaries, stop before execution and request the smallest explicit decision needed. Do not treat a schema, concordance, semantic diff, or generated artifact as permission to change prose.

## Session start (copy-paste for the operator)

> Read editorial/STATE.md, editorial/WORKFLOW.md, and roadmap item <ID>. Load the affected chapters and their editorial/chapters notes. Propose the revision as a plan in chat and wait for my approval before touching any file.

## When an item is rejected or deferred

Record it in STATE.md's decision table with a one-line reason. A rejected structural item (e.g. R-05 option (c)) may unlock simplified versions of later items — note that in the roadmap rather than editing history.
