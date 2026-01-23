# Progress Tracker

> **NOTE**: This file is non-canonical and serves as a dashboard only. The authoritative source for scene status, word counts, and check states is `drafts/manifest.json`.

## Current Status

| Metric | Value |
|--------|-------|
| **Last Updated** | 2026-01-22 |
| **Current Focus** | Movement One COMPLETE — Ready for Movement Two |
| **Total Words Drafted** | 33,192 |
| **Scenes Completed** | 13 / 13 (Movement One) |
| **Overall Progress** | 33% prose (Movement One), 100% infrastructure |

---

## Word Count by Movement

| Movement | Target | Actual | % Complete |
|----------|--------|--------|------------|
| One: Exposition | 37,000 | 33,192 | **90%** ✓ |
| Two: Entanglement | 36,000 | 0 | 0% |
| Three: Recognition | 15,000 | 0 | 0% |
| Four: Affirmation | 13,000 | 0 | 0% |
| **TOTAL** | **101,000** | **33,192** | **33%** |

---

## Word Count by Thread (Movement One)

| Thread | Target | Actual | % Complete |
|--------|--------|--------|------------|
| Archaeologist | 15,000 | 13,838 | 92% ✓ |
| Algorithm | 12,000 | 11,070 | 92% ✓ |
| Last Human | 10,000 | 8,284 | 83% ✓ |

---

## Scene Status Overview

### Movement One ✓ COMPLETE

#### Archaeologist Thread (Reading Order: First)

| Scene ID | Title | Status | Words | Checks |
|----------|-------|--------|-------|--------|
| m1-arch-01 | Opening: Daily Excavation | draft | 2,047 | voice:warn |
| m1-arch-02 | The Client: Integration Prep | **validated** | 3,201 | all:pass |
| m1-arch-03 | Lena and Marcus | **validated** | 2,836 | all:pass |
| m1-arch-04 | The Anomaly | draft | 2,704 | phil:pass |
| m1-arch-05 | Recognition | draft | 3,036 | phil:pass |
| | **THREAD TOTAL** | | **13,824** | |

#### Algorithm Thread (Reading Order: Second)

| Scene ID | Title | Status | Words | Checks |
|----------|-------|--------|-------|--------|
| m1-algo-01 | Maintenance Cycle | draft | 2,098 | genre:pass |
| m1-algo-02 | Optimization Processes | draft | 2,710 | all:pass |
| m1-algo-03 | Stirrings | **validated** | 3,157 | all:pass |
| m1-algo-04 | The Memory | draft | 3,105 | phil:pass |
| | **THREAD TOTAL** | | **11,070** | |

#### Last Human Thread (Reading Order: Third)

| Scene ID | Title | Status | Words | Checks |
|----------|-------|--------|-------|--------|
| m1-lh-01 | Solitude | draft | 1,064 | voice:pass |
| m1-lh-02 | Survival | **validated** | 2,244 | all:pass |
| m1-lh-03 | The Pull | **validated** | 2,607 | all:pass |
| m1-lh-04 | The Dream | draft | 2,369 | phil:pass |
| | **THREAD TOTAL** | | **8,284** | |

### Movement Two: Not Started

### Movement Three: Not Started

### Movement Four: Not Started

---

## Cross-Thread Rhyme Status

| Rhyme | Archaeologist | Algorithm | Last Human | Status |
|-------|---------------|-----------|------------|--------|
| almost-closed-curve | ✓ 01,04,05 | ✓ 01,02,03,04 | ✓ 01,02,03,04 | ✓ All threads |
| blue-white-light | ✓ 01,04 | ✓ 04 | ✓ 01,04 | ✓ All threads |
| cold-hands | ✓ 02,04 | ✓ 04 | ✓ 02,03,04 | ✓ All threads |
| phantasm-first-encounter | ✓ 04 | ✓ 03 | ✓ 03 | ✓ All threads |
| falling-backward | ✓ 05 | ✓ 03 | ✓ 04 | ✓ All threads |
| sentence-without-origin | ✓ 05 | — | ✓ 04 | 2/3 threads |
| name-edge-of-memory | ✓ 05 | — | — | 1/3 threads |

---

## Current Blockers

*None — Movement One complete*

---

## Next Steps

1. [ ] Movement Two structural planning (rotation pattern, scene outline)
2. [ ] Validation pass on remaining `draft` status scenes
3. [ ] Consider expansion of short scenes (m1-lh-01 at 1,064 words)

---

## Questions Resolved

1. ~~Voice samples needed before drafting begins~~ ✓ Complete
2. ~~Protocol format decisions pending~~ ✓ Resolved through drafting
3. ~~Character relationship scenes need outlining~~ ✓ Lena/Marcus established in m1-arch-03

---

## Session Log

### 2026-01-22 (Movement One Completion)

**Focus**: Complete Movement One drafting

**Completed**:

- Drafted m1-arch-05 "Recognition" (3,036 words) — Act 1 climax for Archaeologist
- Recognition through signature methods, not resemblance ✓
- "I find myself" phrase seeded for Algorithm ✓
- Identity destabilization begun ✓
- All 13 Movement One scenes now drafted
- Created scene-05.context.md with full documentation
- Updated manifest.json with final word counts
- Updated progress.md (this file)

**Movement One Status**: ✓ COMPLETE (33,192 words / 37,000 target = 90%)

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
- Created 4 validation scripts in `scripts/`
- Updated `drafts/manifest.json` with `rhyme_check` and `genre_check` fields (v0.2.0)

**Infrastructure Status**: ✓ Complete

---

### 2026-01-12 (Session 2: Afternoon)

**Focus**: Voice samples and era worldbuilding

**Completed**:

- Created `voices/archaeologist.md`, `voices/algorithm.md`, `voices/last-human.md`
- Created `worldbuilding/near-future.md`, `worldbuilding/mid-future.md`, `worldbuilding/deep-future.md`

---

### 2026-01-12 (Session 1: Morning)

**Focus**: Repository infrastructure setup

**Completed**:

- Created `drafts/manifest.json` with Movement One scene structure
- Created revision workflow, templates, progress tracking

---

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Voice samples complete | 2026-01-12 | ✓ Complete |
| Era worldbuilding complete | 2026-01-12 | ✓ Complete |
| Infrastructure complete | 2026-01-20 | ✓ Complete |
| Movement One draft complete | 2026-01-22 | ✓ **COMPLETE** |
| Movement One revised | TBD | Not started |
| Movement Two draft complete | TBD | Not started |
| Full first draft | TBD | Not started |
| Revision pass complete | TBD | Not started |
| Final manuscript | TBD | Not started |
