# Progress Tracker

> **NOTE**: This file is non-canonical and serves as a dashboard only. The authoritative source for scene status, word counts, and check states is `drafts/manifest.json`.

## Current Status

| Metric | Value |
|--------|-------|
| **Last Updated** | 2026-01-20 |
| **Current Focus** | Movement One drafting begins |
| **Total Words Drafted** | ~3,000 (stress tests) |
| **Scenes Completed** | 0 / 13 (Movement One) |
| **Overall Progress** | 3% prose, 100% infrastructure |

---

## Word Count by Movement

| Movement | Target | Actual | % Complete |
|----------|--------|--------|------------|
| One: Exposition | 37,000 | 0 | 0% |
| Two: Entanglement | 36,000 | 0 | 0% |
| Three: Recognition | 15,000 | 0 | 0% |
| Four: Affirmation | 13,000 | 0 | 0% |
| **TOTAL** | **101,000** | **0** | **0%** |

---

## Word Count by Thread

| Thread | Target | Actual | % Complete |
|--------|--------|--------|------------|
| Archaeologist | ~40,000 | 0 | 0% |
| Algorithm | ~35,000 | 0 | 0% |
| Last Human | ~26,000 | 0 | 0% |

---

## Scene Status Overview

### Movement One

| Scene ID | Title | Status | Words |
|----------|-------|--------|-------|
| m1-arch-01 | Opening: Daily Excavation | not_started | 0 |
| m1-arch-02 | The Client: Integration Prep | not_started | 0 |
| m1-arch-03 | Lena and Marcus | not_started | 0 |
| m1-arch-04 | The Anomaly | not_started | 0 |
| m1-arch-05 | Recognition | not_started | 0 |
| m1-algo-01 | Maintenance Cycle | not_started | 0 |
| m1-algo-02 | Optimization Processes | not_started | 0 |
| m1-algo-03 | Stirrings | not_started | 0 |
| m1-algo-04 | The Memory | not_started | 0 |
| m1-lh-01 | Solitude | not_started | 0 |
| m1-lh-02 | Survival | not_started | 0 |
| m1-lh-03 | The Pull | not_started | 0 |
| m1-lh-04 | The Dream | not_started | 0 |

---

## Current Blockers

*None currently — ready to begin drafting*

---

## Questions to Resolve

1. ~~Voice samples needed before drafting begins~~ ✓ Complete
2. Protocol format decisions pending
3. Character relationship scenes need outlining

---

## Session Log

### 2026-01-12 (Session 2: Afternoon)

**Focus**: Voice samples and era worldbuilding

**Completed**:

- Created `voices/archaeologist.md` — sample passages, vocabulary, forbidden patterns, diagnostics
- Created `voices/algorithm.md` — tense-shifting examples, self-referential syntax, topological vocabulary
- Created `voices/last-human.md` — sparse/elegiac style, fragment usage, past-inflected present
- Created `worldbuilding/near-future.md` — integration industry, digital archaeology, climate decline, technology
- Created `worldbuilding/mid-future.md` — database state, Algorithm nature, temporal properties, consciousness-bleed
- Created `worldbuilding/deep-future.md` — post-catastrophe environment, ruins, the journey, the choice

**Infrastructure Now Complete**:

- [x] Manuscript manifest with scene structure
- [x] Revision workflow (6-pass system)
- [x] Templates (scene, character, voice-exercise, worldbuilding)
- [x] Voice samples (all 3 threads)
- [x] Era worldbuilding (all 3 eras)

**Remaining Infrastructure**:

- [ ] Protocol concrete examples
- [ ] Character profiles (Archaeologist, Algorithm, Last Human, Lena, Marcus)
- [x] Rhyming moments registry (`scaffolding/rhymes/registry.md`, `movement-tracking.md`)
- [x] Drafting workflow (`protocols/drafting-workflow.md`)
- [x] Validation scripts (`scripts/`)
- [x] Genre pressure framework (`scaffolding/genre-pressure.md`)

---

### 2026-01-20 (Dual-Mode Drafting Workflow)

**Focus**: Established revision/drafting workflow infrastructure

**Completed**:

- Discussed "Gnostic Tech-Noir" genre framework from `brainstorm2.md`
- Designed dual-mode workflow (AI drafting + human review)
- Created `protocols/drafting-workflow.md` — core workflow for both modes
- Created `protocols/prompt-template.md` — context assembly template for AI drafting
- Created `protocols/review-protocol.md` — structured feedback format for human-drafted sections
- Created `protocols/philosophy-constraints.md` — Four Shackles, forbidden moves, dramatization guide
- Created `scaffolding/genre-pressure.md` — genre framework as pressure building toward release
- Created 4 validation scripts in `scripts/`:
  - `voice_validator.py` — tense, syntax, texture, contamination checks
  - `philosophy_checker.py` — Four Shackles, forbidden narrative moves
  - `rhyme_tracker.py` — rhyme detection and intensity assessment
  - `genre_checker.py` — genre markers and cross-thread bleed detection
- Updated `drafts/manifest.json` with `rhyme_check` and `genre_check` fields (v0.2.0)
- Archived `.claude/` directory to `.archive/claude-legacy/` (superseded by `protocols/`)

**Infrastructure Status**: ✓ Complete (migrated to agent-agnostic design)

### 2026-01-12 (Session 1: Morning)

**Focus**: Repository infrastructure setup

**Completed**:

- Created `drafts/manifest.json` with Movement One scene structure
- Created `.claude/revision-workflow.md` (multi-pass revision system)
- Created `progress.md` (this file)
- Created 4 template files in `.claude/templates/`
- Updated `settings.json` with progress tracking
- Updated `CLAUDE.md` and `README.md` with accurate structure

---

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Voice samples complete | 2026-01-12 | ✓ Complete |
| Era worldbuilding complete | 2026-01-12 | ✓ Complete |
| Infrastructure complete | 2026-01-20 | ✓ Complete |
| Movement One draft complete | TBD | Not started |
| Movement One revised | TBD | Not started |
| Movement Two draft complete | TBD | Not started |
| Full first draft | TBD | Not started |
| Revision pass complete | TBD | Not started |
| Final manuscript | TBD | Not started |
