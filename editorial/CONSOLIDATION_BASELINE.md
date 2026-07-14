# Manuscript pre-consolidation baseline

Reviewed: July 13, 2026

Immutable tag: `pre-consolidation-2026-07-13`

Tagged commit: `103d7f3d6a65379bd851d218a303058d1f576d46`

## Role in consolidation

This repository remains active and is the canonical source for long-form prose, story-bible facts, voice constraints, philosophy constraints, structure, continuity, and editorial approval. It is not the interactive application and is not an archive candidate.

Narramorph owns its interactive runtime edition. Cross-repository exchange will use explicit, versioned literary releases and provenance rather than direct default-branch coupling.

## Verified state

| Check | Result |
|---|---|
| `python scripts/stats.py` | Passed; 28 manuscript files, 85,114 counted words |
| `python scripts/assemble.py` | Passed; 28 chapters, 85,138 assembled words, all endings verified |
| `python scripts/edit_status.py` | Reported 15/15 roadmap items complete, then failed on Windows CP1252 output for a Unicode arrow |

The small word-count difference is produced by the scripts' different counting contexts and should be reconciled in later documentation/tooling work rather than hidden.

## Editorial state

- The canonical manuscript contains 28 files across four movements.
- The developmental revision roadmap reports 15 of 15 items complete.
- Assembly verifies that every chapter ending is present.
- Story bible, voice guides, philosophy constraints, rhyme registry, structure map, chapter notes, and continuity tooling are present.

## Baseline documentation defects

- The root README still says 30 scenes/approximately 90,600 words and calls the developmental edit in progress; live scripts and editorial status indicate 28 canonical files, roughly 85,100 words, and a completed roadmap/verification pass.
- `edit_status.py` violates the repository's Windows/cross-platform expectation when the active console cannot encode the arrow in the next-action field.

These are recorded for the later documentation/tooling batch and do not authorize manuscript prose changes.

## Rights and approval boundary

The root license files reserve manuscript/editorial content while licensing executable tooling under MIT. `INTERACTIVE_USE_PERMISSION.md` defines a narrow, release-specific permission for approved manuscript-derived material to be distributed in official Narramorph builds. No particular excerpt is authorized until its versioned approval record exists.

Canonical prose remains read-only by default under `CLAUDE.md` and `editorial/WORKFLOW.md`.

## Issue disposition

GitHub reported no open issues on July 13, 2026. Future cross-repository work is tracked in Narramorph, while manuscript prose/editorial work continues under this repository's workflow.
