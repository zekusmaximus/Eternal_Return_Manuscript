# DRAFTING PROMPT: m2-lh-02 "The Protocols"

> **Workflow Reference**: Follow [tasks/scene-lifecycle.md](../../../tasks/scene-lifecycle.md) for a complete Scene Lifecycle workflow. This prompt applies Phase 1 (Plan Scene) and Phase 2 (Draft Scene); ensure all lifecycle dependencies are satisfied.

---

## Execution Overview

This prompt enables scene drafting aligned with the Scene Lifecycle Protocol. Ensure the following steps are completed in full:

1. **Read** all specified context and support files.
2. **Draft** the scene, strictly adhering to voice/rhyme/structure requirements.
3. **Log deviations** from the `.context.md` file in "Deviations" sections.
4. **Follow Scene Lifecycle rules** from [tasks/scene-lifecycle.md](../../../tasks/scene-lifecycle.md).
5. **Prepare for Validation** by updating all outputs and configuration files specified.

---

## Phase 1: Context Assembly

### Required Reading (MUST complete before entering Draft Scene phase)

| File | Purpose |
|------|---------|
| [tasks/scene-lifecycle.md](../../../tasks/scene-lifecycle.md) | Scene drafting phases: plan → draft → validate |
| [tasks/model-routing.md](../../../tasks/model-routing.md) | Model-specific routing and constraints |
| [scaffolding/voice/last-human-voice.md](../../../scaffolding/voice/last-human-voice.md) | Last Human voice rules |
| [scaffolding/rhymes/registry.md](../../../scaffolding/rhymes/registry.md) | Rhyme definitions and flow |
| [drafts/movement-two/last-human/m2-lh-01.md](m2-lh-01.md) | Preceding Last Human scene |
| [drafts/movement-two/algorithm/m2-algo-02.md](../algorithm/m2-algo-02.md) | Rhyme handoff source |

### Verify Configuration

Before drafting, confirm `manifest.json` status for `m2-lh-02`:

```json
{
  "id": "m2-lh-02",
  "planned": true,
  "drafted": false,
  "validated": false,
  "polished": false
}
```

If `drafted` is `true`, revise completion steps using Phase 3 (Validation).

---

## Phase 2: Draft Scene

### Drafting Objectives

- **Target Word Count**: 4000 (3600-4400 acceptable).
- **Scene Title**: "The Protocols".
- **Thread and Movement Sequence**: Last Human, Movement Two, Cycle Two.
- **Opening Rhyme**: name-edge-of-memory.
- **Closing Rhyme**: sentence-without-origin.

### Voice Contamination Rules

- "Sparse syntax; absence between thoughts."
- "Present-tense tactility leaks into past: memories dissolve."
- "Archaeologist voice boundaries fade into dense informational paragraphs."

---

Follow drafting instructions in **tasks/scene-lifecycle.md**, Phase 2, ensuring:

1. Input compliance with `.context.md` beats.
2. Use of contaminant "tactility" motifs embedded into Last Human sequencing (Rule interpolation).
3. No final validator assumptions until Phase 3 instructions resolve rhyme parent-source validation (irrevocable).

Update deviation logs.