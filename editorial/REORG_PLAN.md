# Reorganization Plan

> Written **before** execution so the reorg is auditable as a document before it exists as a diff.
> Execution method: `git mv` only. No file is deleted, no manuscript file's *content* is touched — prose files change path only.

## Target shape

```
/manuscript/    30 canonical prose files, zero-padded reading order (NN-mX-thread-slug.md)
/bible/         world/character/continuity/voice reference (+ voices/, worldbuilding/, narrative-protocols/)
/editorial/     all editorial output; /revision-one/ holds the prior session's records; /chapters/ added in Phase 3
/outlines/      active structural documents (braiding specs, manifest)
/archive/       all 112 STALE files; /legacy/ = the old .archive tree; /drafting-records/ = scene prompts+context records
/scripts/       validators + configs (unchanged paths); new tools added in Phase 2
/protocols/     drafting/review process docs (kept as an extra top-level dir — existing coherent tooling docs)
CLAUDE.md       added in Phase 2
```

Adaptations from the brief's template, with reasons:
- **"Chapters" = the 30 scene/section units** in manifest reading order; numbering encodes the braid (`14-m2-arch-1-the-bleed.md` = 14th reading unit, Movement 2 cycle 1, Archaeologist thread), so the braid structure survives a flat directory listing.
- **`protocols/` kept** as a top-level tooling-docs directory rather than forced into `/scripts/`.
- **`archive/` mirrors source paths** (`archive/legacy/…` for the old `.archive`, `archive/drafting-records/…` for scene apparatus, `archive/scripts/…`, `archive/compiled1/…`) so provenance is readable from the path itself.
- **`.gitignore` gains `build/` and `__pycache__/`** (Phase 2 assembly output; cache) and loses its two stray `nul` lines — tooling edit, permitted.

## Reference-integrity edits (the one permitted non-manuscript content edit)

After the moves, these files get their internal references updated (each edit listed in §3 below):
1. `README.md` — Repository Structure section rewritten for the new layout; stale "Current Status" section replaced with post-Revision One status; links to moved files fixed.
2. `outlines/manifest.json` — a `_note` metadata key added recording that its `file:` fields describe the pre-reorg layout and pointing to `bible/structure-map.md` (Phase 3) for the live mapping. The scene data itself is untouched.
3. `scripts/movement_config.json` / `scripts/movement_three_config.json` — path fields updated from `drafts/…` to `manuscript/…` so the legacy validators keep running.
4. `editorial/INVENTORY.md` is *not* rewritten — it documents the pre-reorg state by design; this plan is the bridge.

## 1. Moves (full mapping, 175 files)

| Old path | New path | Bucket |
|---|---|---|
| `.archive/Brainstorm1.md` | `archive/legacy/Brainstorm1.md` | STALE |
| `.archive/README.md` | `archive/legacy/README.md` | STALE |
| `.archive/SONNET_IMPLEMENTATION_PROMPT.md` | `archive/legacy/SONNET_IMPLEMENTATION_PROMPT.md` | STALE |
| `.archive/brainstorm2.md` | `archive/legacy/brainstorm2.md` | STALE |
| `.archive/claude-legacy/CLAUDE.md` | `archive/legacy/claude-legacy/CLAUDE.md` | STALE |
| `.archive/claude-legacy/commands.md` | `archive/legacy/claude-legacy/commands.md` | STALE |
| `.archive/claude-legacy/manual-sync.md` | `archive/legacy/claude-legacy/manual-sync.md` | STALE |
| `.archive/claude-legacy/project-rules.md` | `archive/legacy/claude-legacy/project-rules.md` | STALE |
| `.archive/claude-legacy/revision-workflow.md` | `archive/legacy/claude-legacy/revision-workflow.md` | STALE |
| `.archive/claude-legacy/settings.json` | `archive/legacy/claude-legacy/settings.json` | STALE |
| `.archive/claude-legacy/templates/character-template.md` | `archive/legacy/claude-legacy/templates/character-template.md` | STALE |
| `.archive/claude-legacy/templates/scene-template.md` | `archive/legacy/claude-legacy/templates/scene-template.md` | STALE |
| `.archive/claude-legacy/templates/voice-exercise.md` | `archive/legacy/claude-legacy/templates/voice-exercise.md` | STALE |
| `.archive/claude-legacy/templates/worldbuilding-template.md` | `archive/legacy/claude-legacy/templates/worldbuilding-template.md` | STALE |
| `.archive/compiled/entire-manuscript.docx` | `archive/legacy/compiled/entire-manuscript.docx` | STALE |
| `.archive/compiled/entire-manuscript.md` | `archive/legacy/compiled/entire-manuscript.md` | STALE |
| `.archive/compiled/movement-four-complete.md` | `archive/legacy/compiled/movement-four-complete.md` | STALE |
| `.archive/compiled/movement-one-algorithm.md` | `archive/legacy/compiled/movement-one-algorithm.md` | STALE |
| `.archive/compiled/movement-one-archaeologist.md` | `archive/legacy/compiled/movement-one-archaeologist.md` | STALE |
| `.archive/compiled/movement-one-complete.md` | `archive/legacy/compiled/movement-one-complete.md` | STALE |
| `.archive/compiled/movement-one-last-human.md` | `archive/legacy/compiled/movement-one-last-human.md` | STALE |
| `.archive/compiled/movement-three-complete.md` | `archive/legacy/compiled/movement-three-complete.md` | STALE |
| `.archive/compiled/movement-two-complete.md` | `archive/legacy/compiled/movement-two-complete.md` | STALE |
| `.archive/compiled/movements-one-two-complete.md` | `archive/legacy/compiled/movements-one-two-complete.md` | STALE |
| `.archive/movement_three_phase_A_B_revision_plan.md` | `editorial/revision-one/movement_three_phase_A_B_revision_plan.md` | EDITORIAL |
| `.archive/next_session_prompt.md` | `archive/legacy/next_session_prompt.md` | STALE |
| `Notes.md` | `bible/development-notes.md` | BIBLE |
| `compiled1/entire-manuscript.docx` | `archive/compiled1/entire-manuscript.docx` | STALE |
| `compiled1/entire-manuscript.md` | `archive/compiled1/entire-manuscript.md` | STALE |
| `compiled1/movement-four-complete.md` | `archive/compiled1/movement-four-complete.md` | STALE |
| `compiled1/movement-one-complete.md` | `archive/compiled1/movement-one-complete.md` | STALE |
| `compiled1/movement-three-complete.md` | `archive/compiled1/movement-three-complete.md` | STALE |
| `compiled1/movement-two-complete.md` | `archive/compiled1/movement-two-complete.md` | STALE |
| `drafts/manifest.json` | `outlines/manifest.json` | OUTLINE |
| `drafts/movement-four/m4-1-prompt.md` | `archive/drafting-records/movement-four/m4-1-prompt.md` | STALE |
| `drafts/movement-four/m4-1.context.md` | `archive/drafting-records/movement-four/m4-1.context.md` | STALE |
| `drafts/movement-four/m4-2-prompt.md` | `archive/drafting-records/movement-four/m4-2-prompt.md` | STALE |
| `drafts/movement-four/m4-2.context.md` | `archive/drafting-records/movement-four/m4-2.context.md` | STALE |
| `drafts/movement-four/m4-3-prompt.md` | `archive/drafting-records/movement-four/m4-3-prompt.md` | STALE |
| `drafts/movement-four/m4-3.context.md` | `archive/drafting-records/movement-four/m4-3.context.md` | STALE |
| `drafts/movement-four/m4-4-prompt.md` | `archive/drafting-records/movement-four/m4-4-prompt.md` | STALE |
| `drafts/movement-four/m4-4.context.md` | `archive/drafting-records/movement-four/m4-4.context.md` | STALE |
| `drafts/movement-four/section-4-1-digitization-choice.md` | `manuscript/27-m4-1-digitization-choice.md` | MANUSCRIPT |
| `drafts/movement-four/section-4-2-sacrifice.md` | `manuscript/28-m4-2-sacrifice.md` | MANUSCRIPT |
| `drafts/movement-four/section-4-3-merge.md` | `manuscript/29-m4-3-merge.md` | MANUSCRIPT |
| `drafts/movement-four/section-4-4-coda.md` | `manuscript/30-m4-4-coda.md` | MANUSCRIPT |
| `drafts/movement-one/algorithm/scenes/scene-01.context.md` | `archive/drafting-records/movement-one/algorithm/scenes/scene-01.context.md` | STALE |
| `drafts/movement-one/algorithm/scenes/scene-01.md` | `manuscript/06-m1-algo-1-maintenance-cycle.md` | MANUSCRIPT |
| `drafts/movement-one/algorithm/scenes/scene-02.context.md` | `archive/drafting-records/movement-one/algorithm/scenes/scene-02.context.md` | STALE |
| `drafts/movement-one/algorithm/scenes/scene-02.md` | `manuscript/07-m1-algo-2-optimization-processes.md` | MANUSCRIPT |
| `drafts/movement-one/algorithm/scenes/scene-03.context.md` | `archive/drafting-records/movement-one/algorithm/scenes/scene-03.context.md` | STALE |
| `drafts/movement-one/algorithm/scenes/scene-03.md` | `manuscript/08-m1-algo-3-stirrings.md` | MANUSCRIPT |
| `drafts/movement-one/algorithm/scenes/scene-04.context.md` | `archive/drafting-records/movement-one/algorithm/scenes/scene-04.context.md` | STALE |
| `drafts/movement-one/algorithm/scenes/scene-04.md` | `manuscript/09-m1-algo-4-the-memory.md` | MANUSCRIPT |
| `drafts/movement-one/archaeologist/first-bleed.context.md` | `archive/drafting-records/movement-one/archaeologist/first-bleed.context.md` | STALE |
| `drafts/movement-one/archaeologist/first-bleed.md` | `archive/drafting-records/movement-one/archaeologist/first-bleed.md` | STALE |
| `drafts/movement-one/archaeologist/scenes/scene-01.context.md` | `archive/drafting-records/movement-one/archaeologist/scenes/scene-01.context.md` | STALE |
| `drafts/movement-one/archaeologist/scenes/scene-01.md` | `manuscript/01-m1-arch-1-daily-excavation.md` | MANUSCRIPT |
| `drafts/movement-one/archaeologist/scenes/scene-02.context.md` | `archive/drafting-records/movement-one/archaeologist/scenes/scene-02.context.md` | STALE |
| `drafts/movement-one/archaeologist/scenes/scene-02.md` | `manuscript/02-m1-arch-2-integration-prep.md` | MANUSCRIPT |
| `drafts/movement-one/archaeologist/scenes/scene-03.context.md` | `archive/drafting-records/movement-one/archaeologist/scenes/scene-03.context.md` | STALE |
| `drafts/movement-one/archaeologist/scenes/scene-03.md` | `manuscript/03-m1-arch-3-lena-and-marcus.md` | MANUSCRIPT |
| `drafts/movement-one/archaeologist/scenes/scene-04.context.md` | `archive/drafting-records/movement-one/archaeologist/scenes/scene-04.context.md` | STALE |
| `drafts/movement-one/archaeologist/scenes/scene-04.md` | `manuscript/04-m1-arch-4-the-anomaly.md` | MANUSCRIPT |
| `drafts/movement-one/archaeologist/scenes/scene-05.context.md` | `archive/drafting-records/movement-one/archaeologist/scenes/scene-05.context.md` | STALE |
| `drafts/movement-one/archaeologist/scenes/scene-05.md` | `manuscript/05-m1-arch-5-recognition.md` | MANUSCRIPT |
| `drafts/movement-one/last-human/scenes/scene-01.context.md` | `archive/drafting-records/movement-one/last-human/scenes/scene-01.context.md` | STALE |
| `drafts/movement-one/last-human/scenes/scene-01.md` | `manuscript/10-m1-lh-1-solitude.md` | MANUSCRIPT |
| `drafts/movement-one/last-human/scenes/scene-02.context.md` | `archive/drafting-records/movement-one/last-human/scenes/scene-02.context.md` | STALE |
| `drafts/movement-one/last-human/scenes/scene-02.md` | `manuscript/11-m1-lh-2-survival.md` | MANUSCRIPT |
| `drafts/movement-one/last-human/scenes/scene-03.context.md` | `archive/drafting-records/movement-one/last-human/scenes/scene-03.context.md` | STALE |
| `drafts/movement-one/last-human/scenes/scene-03.md` | `manuscript/12-m1-lh-3-the-pull.md` | MANUSCRIPT |
| `drafts/movement-one/last-human/scenes/scene-04.context.md` | `archive/drafting-records/movement-one/last-human/scenes/scene-04.context.md` | STALE |
| `drafts/movement-one/last-human/scenes/scene-04.md` | `manuscript/13-m1-lh-4-the-dream.md` | MANUSCRIPT |
| `drafts/movement-three/convergence.context.md` | `archive/drafting-records/movement-three/convergence.context.md` | STALE |
| `drafts/movement-three/convergence.md` | `manuscript/26-m3-convergence.md` | MANUSCRIPT |
| `drafts/movement-three/m3-phase-a-prompt.md` | `archive/drafting-records/movement-three/m3-phase-a-prompt.md` | STALE |
| `drafts/movement-three/m3-phase-a.context.md` | `archive/drafting-records/movement-three/m3-phase-a.context.md` | STALE |
| `drafts/movement-three/m3-phase-b-prompt.md` | `archive/drafting-records/movement-three/m3-phase-b-prompt.md` | STALE |
| `drafts/movement-three/m3-phase-b.context.md` | `archive/drafting-records/movement-three/m3-phase-b.context.md` | STALE |
| `drafts/movement-three/m3-phase-c-prompt.md` | `archive/drafting-records/movement-three/m3-phase-c-prompt.md` | STALE |
| `drafts/movement-three/phase-a-accelerating-cuts.md` | `manuscript/23-m3-phase-a-accelerating-cuts.md` | MANUSCRIPT |
| `drafts/movement-three/phase-b-simultaneous-narration.md` | `manuscript/24-m3-phase-b-simultaneous-narration.md` | MANUSCRIPT |
| `drafts/movement-three/phase-c-dissolution.md` | `manuscript/25-m3-phase-c-dissolution.md` | MANUSCRIPT |
| `drafts/movement-two/algorithm/m2-algo-01-prompt.md` | `archive/drafting-records/movement-two/algorithm/m2-algo-01-prompt.md` | STALE |
| `drafts/movement-two/algorithm/m2-algo-02-prompt.md` | `archive/drafting-records/movement-two/algorithm/m2-algo-02-prompt.md` | STALE |
| `drafts/movement-two/algorithm/m2-algo-02.context.md` | `archive/drafting-records/movement-two/algorithm/m2-algo-02.context.md` | STALE |
| `drafts/movement-two/algorithm/m2-algo-02.md` | `manuscript/18-m2-algo-2-the-bleed.md` | MANUSCRIPT |
| `drafts/movement-two/algorithm/m2-algo-03-prompt.md` | `archive/drafting-records/movement-two/algorithm/m2-algo-03-prompt.md` | STALE |
| `drafts/movement-two/algorithm/m2-algo-03.context.md` | `archive/drafting-records/movement-two/algorithm/m2-algo-03.context.md` | STALE |
| `drafts/movement-two/algorithm/scenes/scene-01.context.md` | `archive/drafting-records/movement-two/algorithm/scenes/scene-01.context.md` | STALE |
| `drafts/movement-two/algorithm/scenes/scene-01.md` | `manuscript/15-m2-algo-1-the-resonance.md` | MANUSCRIPT |
| `drafts/movement-two/algorithm/scenes/scene-03.md` | `manuscript/21-m2-algo-3-the-sacrifice.md` | MANUSCRIPT |
| `drafts/movement-two/archaeologist/m2-arch-01-prompt.md` | `archive/drafting-records/movement-two/archaeologist/m2-arch-01-prompt.md` | STALE |
| `drafts/movement-two/archaeologist/m2-arch-02-prompt.md` | `archive/drafting-records/movement-two/archaeologist/m2-arch-02-prompt.md` | STALE |
| `drafts/movement-two/archaeologist/m2-arch-02.context.md` | `archive/drafting-records/movement-two/archaeologist/m2-arch-02.context.md` | STALE |
| `drafts/movement-two/archaeologist/m2-arch-03-prompt.md` | `archive/drafting-records/movement-two/archaeologist/m2-arch-03-prompt.md` | STALE |
| `drafts/movement-two/archaeologist/m2-arch-03.context.md` | `archive/drafting-records/movement-two/archaeologist/m2-arch-03.context.md` | STALE |
| `drafts/movement-two/archaeologist/scenes/scene-01.context.md` | `archive/drafting-records/movement-two/archaeologist/scenes/scene-01.context.md` | STALE |
| `drafts/movement-two/archaeologist/scenes/scene-01.md` | `manuscript/14-m2-arch-1-the-bleed.md` | MANUSCRIPT |
| `drafts/movement-two/archaeologist/scenes/scene-02.md` | `manuscript/17-m2-arch-2-the-dissolution.md` | MANUSCRIPT |
| `drafts/movement-two/archaeologist/scenes/scene-03.md` | `manuscript/20-m2-arch-3-the-merge.md` | MANUSCRIPT |
| `drafts/movement-two/last-human/m2-lh-01-prompt.md` | `archive/drafting-records/movement-two/last-human/m2-lh-01-prompt.md` | STALE |
| `drafts/movement-two/last-human/m2-lh-02-prompt.md` | `archive/drafting-records/movement-two/last-human/m2-lh-02-prompt.md` | STALE |
| `drafts/movement-two/last-human/m2-lh-03-prompt.md` | `archive/drafting-records/movement-two/last-human/m2-lh-03-prompt.md` | STALE |
| `drafts/movement-two/last-human/m2-lh-03.context.md` | `archive/drafting-records/movement-two/last-human/m2-lh-03.context.md` | STALE |
| `drafts/movement-two/last-human/scenes/scene-01.context.md` | `archive/drafting-records/movement-two/last-human/scenes/scene-01.context.md` | STALE |
| `drafts/movement-two/last-human/scenes/scene-01.md` | `manuscript/16-m2-lh-1-the-archive.md` | MANUSCRIPT |
| `drafts/movement-two/last-human/scenes/scene-02.context.md` | `archive/drafting-records/movement-two/last-human/scenes/scene-02.context.md` | STALE |
| `drafts/movement-two/last-human/scenes/scene-02.md` | `manuscript/19-m2-lh-2-the-protocols.md` | MANUSCRIPT |
| `drafts/movement-two/last-human/scenes/scene-03.md` | `manuscript/22-m2-lh-3-the-interface.md` | MANUSCRIPT |
| `examples/Digital_Archaeologist_Exercises.md` | `archive/examples/Digital_Archaeologist_Exercises.md` | STALE |
| `examples/Last_Human_Exercises.md` | `archive/examples/Last_Human_Exercises.md` | STALE |
| `examples/Movement_Two_Example.md` | `archive/examples/Movement_Two_Example.md` | STALE |
| `examples/Self_Aware_Algorithm_Exercises.md` | `archive/examples/Self_Aware_Algorithm_Exercises.md` | STALE |
| `progress.md` | `archive/progress.md` | STALE |
| `protocols/philosophy-constraints.md` | `bible/philosophy-constraints.md` | BIBLE |
| `research/framework.md` | `bible/philosophical-framework.md` | BIBLE |
| `revision_plan_one.md` | `editorial/revision-one/revision-plan.md` | EDITORIAL |
| `scaffolding/genre-pressure.md` | `bible/genre-pressure.md` | BIBLE |
| `scaffolding/movement-four-braiding.md` | `outlines/movement-four-braiding.md` | OUTLINE |
| `scaffolding/movement-three-braiding.md` | `outlines/movement-three-braiding.md` | OUTLINE |
| `scaffolding/movement-three-phase-c-braid.md` | `outlines/movement-three-phase-c-braid.md` | OUTLINE |
| `scaffolding/movement-three-prep.md` | `outlines/movement-three-prep.md` | OUTLINE |
| `scaffolding/movement-two-braiding.md` | `outlines/movement-two-braiding.md` | OUTLINE |
| `scaffolding/movement-two-prep.md` | `archive/scaffolding/movement-two-prep.md` | STALE |
| `scaffolding/narrative_protocols/fragment-alpha.md` | `bible/narrative-protocols/fragment-alpha.md` | BIBLE |
| `scaffolding/narrative_protocols/protocol-design.md` | `bible/narrative-protocols/protocol-design.md` | BIBLE |
| `scaffolding/rhymes/movement-three-escalation.md` | `outlines/movement-three-rhyme-escalation.md` | OUTLINE |
| `scaffolding/rhymes/movement-tracking.md` | `archive/scaffolding/rhymes/movement-tracking.md` | STALE |
| `scaffolding/rhymes/registry.md` | `bible/rhyme-registry.md` | BIBLE |
| `scripts/__pycache__/genre_checker.cpython-313.pyc` | `archive/scripts/__pycache__/genre_checker.cpython-313.pyc` | STALE |
| `scripts/__pycache__/philosophy_checker.cpython-313.pyc` | `archive/scripts/__pycache__/philosophy_checker.cpython-313.pyc` | STALE |
| `scripts/__pycache__/phrase_tracker.cpython-313.pyc` | `archive/scripts/__pycache__/phrase_tracker.cpython-313.pyc` | STALE |
| `scripts/__pycache__/rhyme_tracker.cpython-313.pyc` | `archive/scripts/__pycache__/rhyme_tracker.cpython-313.pyc` | STALE |
| `scripts/__pycache__/voice_validator.cpython-313.pyc` | `archive/scripts/__pycache__/voice_validator.cpython-313.pyc` | STALE |
| `scripts/archive/movement_one/genre_checker.py` | `archive/scripts/archive/movement_one/genre_checker.py` | STALE |
| `scripts/archive/movement_one/philosophy_checker.py` | `archive/scripts/archive/movement_one/philosophy_checker.py` | STALE |
| `scripts/archive/movement_one/rhyme_tracker.py` | `archive/scripts/archive/movement_one/rhyme_tracker.py` | STALE |
| `scripts/archive/movement_one/voice_validator.py` | `archive/scripts/archive/movement_one/voice_validator.py` | STALE |
| `scripts/compiled/movement-one-algorithm.md` | `archive/scripts/compiled/movement-one-algorithm.md` | STALE |
| `scripts/compiled/movement-one-archaeologist.md` | `archive/scripts/compiled/movement-one-archaeologist.md` | STALE |
| `scripts/compiled/movement-one-complete.md` | `archive/scripts/compiled/movement-one-complete.md` | STALE |
| `scripts/compiled/movement-one-last-human.md` | `archive/scripts/compiled/movement-one-last-human.md` | STALE |
| `scripts/validation-outputs/algorithm-genre.json` | `archive/scripts/validation-outputs/algorithm-genre.json` | STALE |
| `scripts/validation-outputs/algorithm-philosophy.json` | `archive/scripts/validation-outputs/algorithm-philosophy.json` | STALE |
| `scripts/validation-outputs/algorithm-rhyme.json` | `archive/scripts/validation-outputs/algorithm-rhyme.json` | STALE |
| `scripts/validation-outputs/algorithm-voice.json` | `archive/scripts/validation-outputs/algorithm-voice.json` | STALE |
| `scripts/validation-outputs/archaeologist-genre.json` | `archive/scripts/validation-outputs/archaeologist-genre.json` | STALE |
| `scripts/validation-outputs/archaeologist-philosophy.json` | `archive/scripts/validation-outputs/archaeologist-philosophy.json` | STALE |
| `scripts/validation-outputs/archaeologist-rhyme.json` | `archive/scripts/validation-outputs/archaeologist-rhyme.json` | STALE |
| `scripts/validation-outputs/archaeologist-voice.json` | `archive/scripts/validation-outputs/archaeologist-voice.json` | STALE |
| `scripts/validation-outputs/last-human-genre.json` | `archive/scripts/validation-outputs/last-human-genre.json` | STALE |
| `scripts/validation-outputs/last-human-philosophy.json` | `archive/scripts/validation-outputs/last-human-philosophy.json` | STALE |
| `scripts/validation-outputs/last-human-rhyme.json` | `archive/scripts/validation-outputs/last-human-rhyme.json` | STALE |
| `scripts/validation-outputs/last-human-voice.json` | `archive/scripts/validation-outputs/last-human-voice.json` | STALE |
| `scripts/validation-outputs/phase-a-audit.yaml` | `editorial/revision-one/phase-a-audit.yaml` | EDITORIAL |
| `scripts/validation-outputs/phase-b-revisions.yaml` | `editorial/revision-one/phase-b-revisions.yaml` | EDITORIAL |
| `scripts/validation-outputs/phase-c-calibration.yaml` | `editorial/revision-one/phase-c-calibration.yaml` | EDITORIAL |
| `scripts/validation-outputs/phase-d-compression.yaml` | `editorial/revision-one/phase-d-compression.yaml` | EDITORIAL |
| `scripts/validation-outputs/phase-e-agency.yaml` | `editorial/revision-one/phase-e-agency.yaml` | EDITORIAL |
| `scripts/validation-outputs/phase-f-anchoring.yaml` | `editorial/revision-one/phase-f-anchoring.yaml` | EDITORIAL |
| `scripts/validation-outputs/phase-g-validation.yaml` | `editorial/revision-one/phase-g-validation.yaml` | EDITORIAL |
| `scripts/validation-script-review-prompt.md` | `archive/scripts/validation-script-review-prompt.md` | STALE |
| `scripts/validation-scripts-review-report.md` | `archive/scripts/validation-scripts-review-report.md` | STALE |
| `voices/algorithm.md` | `bible/voices/algorithm.md` | BIBLE |
| `voices/archaeologist.md` | `bible/voices/archaeologist.md` | BIBLE |
| `voices/last-human.md` | `bible/voices/last-human.md` | BIBLE |
| `voices/quick-reference.md` | `bible/voices/quick-reference.md` | BIBLE |
| `worldbuilding/Pantasm_Reference.png` | `bible/worldbuilding/Pantasm_Reference.png` | BIBLE |
| `worldbuilding/Phantasm.md` | `bible/worldbuilding/Phantasm.md` | BIBLE |
| `worldbuilding/catastrophe-timeline.md` | `bible/worldbuilding/catastrophe-timeline.md` | BIBLE |
| `worldbuilding/deep-future.md` | `bible/worldbuilding/deep-future.md` | BIBLE |
| `worldbuilding/mid-future.md` | `bible/worldbuilding/mid-future.md` | BIBLE |
| `worldbuilding/near-future.md` | `bible/worldbuilding/near-future.md` | BIBLE |

## 2. Files that stay in place (22 TOOLING files + this session's editorial output)

| Path | Note |
|---|---|
| `.claude/settings.local.json` | tooling; unchanged |
| `.gitignore` | tooling; unchanged |
| `.vscode/settings.json` | tooling; unchanged |
| `README.md` | tooling; unchanged |
| `protocols/drafting-workflow.md` | tooling; unchanged |
| `protocols/prompt-template.md` | tooling; unchanged |
| `protocols/review-protocol.md` | tooling; unchanged |
| `protocols/revision-phase-prompts.md` | tooling; unchanged |
| `protocols/scene-lifecycle-protocol.md` | tooling; unchanged |
| `scripts/alternation_validator.py` | tooling; unchanged |
| `scripts/compile_movement.py` | tooling; unchanged |
| `scripts/dissolution_validator.py` | tooling; unchanged |
| `scripts/genre_checker.py` | tooling; unchanged |
| `scripts/movement_config.json` | tooling; unchanged |
| `scripts/movement_three_config.json` | tooling; unchanged |
| `scripts/phase-c-validation-workflow.md` | tooling; unchanged |
| `scripts/phase_c_review_script.py` | tooling; unchanged |
| `scripts/philosophy_checker.py` | tooling; unchanged |
| `scripts/phrase_tracker.py` | tooling; unchanged |
| `scripts/rhyme_tracker.py` | tooling; unchanged |
| `scripts/rhyme_tracker_m3.py` | tooling; unchanged |
| `scripts/voice_validator.py` | tooling; unchanged |

## 3. Post-move edit log

Filled in during execution — every content edit made for reference integrity is listed here.

- README.md: Repository Structure + Current Status sections rewritten for the new layout; stale mid-draft status replaced; dead references (root brainstorms, nonexistent `/characters`) removed; pointer added warning that the archived compiled DOCX is stale/truncated.
- outlines/manifest.json: added `metadata._note` (paths refer to pre-reorg layout; word counts predate Revision One; see `bible/structure-map.md` and `scripts/stats.py`). Scene data untouched.
- scripts/movement_config.json, scripts/movement_three_config.json: inspected — they contain **no file paths** (validation parameters only), so no edit was needed. Legacy validators take explicit paths as CLI arguments and work against `manuscript/…`. `scripts/compile_movement.py` is hardcoded to the old layout; it is superseded by `scripts/assemble.py` in Phase 2 and archived then.
- outlines/movement-four-braiding.md, outlines/movement-three-prep.md, outlines/movement-three-phase-c-braid.md, outlines/movement-three-rhyme-escalation.md, bible/rhyme-registry.md, bible/worldbuilding/Phantasm.md: broken links/path mentions updated to new locations (incl. one absolute local-machine path in movement-three-prep.md).
- protocols/*.md (5 files): a one-paragraph "Layout note" added under the title instead of rewriting dozens of historical path mentions — these are process records of the drafting era; the note points to this plan for the mapping.
- .gitignore: rewritten — stray `nul` lines removed; `build/`, `__pycache__/`, `*.pyc` added.
- editorial/mechanical-issues.md: created (defects in manuscript files are logged, never fixed in place).
- archive/README.md: created — inventory of everything archived and why.
