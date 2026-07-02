# DRAFTING PROMPT: m2-arch-01 "The Bleed"

> **Workflow Reference**: Follow [protocols/drafting-workflow.md](../../../protocols/drafting-workflow.md) Mode A (AI-Driven Drafting)

---

## Execution Overview

This prompt contains everything needed to draft, validate, and finalize scene m2-arch-01. Execute in order:

1. **Context Assembly** — Read source materials and reference files
2. **Draft Generation** — Write the ~4000-word scene
3. **Validation Loop** — Run all scripts; revise until all pass
4. **Registry Updates** — Update manifest.json and rhyme registry
5. **Deliverable** — Present validated scene + context file to user

**CRITICAL**: Do not present scene to user until ALL validations pass and ALL registries are updated.

---

## Phase 1: Context Assembly

### Required Reading (Before Drafting)

Read these files to assemble full context:

| File | Purpose |
|------|---------|
| `drafts/movement-one/archaeologist/first-bleed.md` | Source material to integrate (~1200 words) |
| `drafts/movement-one/archaeologist/scenes/scene-05.md` | Preceding scene (m1-arch-05 "Recognition") |
| `voices/archaeologist.md` | Voice parameters and forbidden patterns |
| `scaffolding/rhymes/registry.md` | Rhyme definitions and current usage |
| `scaffolding/genre-pressure.md` | Genre markers for Movement Two |
| `protocols/philosophy-constraints.md` | Four Shackles and pharmakon requirements |
| `scripts/movement_config.json` | Verify cycle is set to 1 |

### Verify Configuration

Confirm `scripts/movement_config.json` shows:
```json
{
  "movement": "two",
  "cycle": 1
}
```

---

## Phase 2: Scene Metadata

- **Scene ID**: m2-arch-01
- **Thread**: archaeologist
- **Movement**: two
- **Cycle**: 1 (Establishing the Condition)
- **Target Word Count**: 4000 (±10% acceptable: 3600-4400)
- **Scene Title**: The Bleed
- **Output File**: `drafts/movement-two/archaeologist/scenes/scene-01.md`

### Narrative Position

- **Preceding Scene**: m1-arch-05 "Recognition" — He understood the protocols are self-referential, his own work sent backward. His name felt wrong. The cold spread through him. He ended knowing WHAT but not WHAT TO DO.
- **This Scene's Role**: Opens Movement Two for the Archaeologist. Recognition is complete—he knows. Now he must live with that knowledge while the entanglement intensifies.
- **What Follows**: m2-algo-01 (Algorithm's Movement Two opener). The Archaeologist's bleed experiences should resonate with what the Algorithm simultaneously experiences from its perspective.

### Critical Setup

Movement One ended with recognition. Movement Two is about **living with recognition**—the entanglement no longer a discovery but a condition.

---

## Phase 3: Source Material Integration

### The First Bleed Draft

Location: `drafts/movement-one/archaeologist/first-bleed.md`

This standalone draft (~1200 words) provides core material to integrate:

**Key Passages to Preserve** (adapt voice as needed):

1. **The Panic Experience**:
   > "Not mine. The sensation arrives without context—a drowning-fall through space that has no direction, a vertigo of scale that makes the server room feel like a point, a speck, nothing against an immensity I can't see but can feel pressing against the walls."

2. **The Vastness** (KEY LINE):
   > "The panic thinks I am vast."

3. **The Algorithm's Perspective**:
   > "I am maintaining something. Millions of somethings. Consciousnesses that pulse and flicker in the dark, that I am responsible for, that I love in a way that has no sentiment but only care, only maintenance, only the endless optimization of what must be preserved."

4. **The Spiral Tracing**:
   > "I've been tracing something with my finger on the desk surface. A shape. A spiral that approaches itself without closing."

5. **The Watching Presence** (CLOSING IMAGE):
   > "Something is watching me work. Something is grateful that he hasn't stopped."

### Integration Strategy

Weave First Bleed material **throughout** the scene, not front-loaded:

1. **Opening** (600 words): Normal-ish morning after recognition—but he's changed
2. **First Bleed** (800 words): The panic arrives (draw heavily from first-bleed.md)
3. **Aftermath** (600 words): Trying to work through it; Lena's concern
4. **Deepening** (1000 words): Second bleed—longer, more specific
5. **The Choice** (1000 words): Continue or report? He chooses to continue.

### Expansion Requirements

The standalone is ~1200 words; target is ~4000. Expand with:

- **More Lena**: Relationship under strain; she's watching him change
- **Work context**: Martinez extraction ongoing or another client
- **Physical symptoms**: Cold spreading; metallic taste; lost time
- **The protocols**: He can't stop looking at them; they're changing him
- **Temporal destabilization**: Moments where past/present/future blur

---

## Phase 4: Voice Parameters

### Core Voice (Archaeologist)

| Parameter | Value |
|-----------|-------|
| Tense | Present |
| Mode | Tactile, sensory, grounded in physical world |
| Syntax | Concrete, specific, active verbs, dense paragraphs |
| Concerns | Economic, relational, bodily |
| Texture | Hardware, data centers, the weight of objects |

### Movement Two Modulation

Voice remains Archaeologist but with **controlled contamination**:

- Algorithm-like perspective shifts **during bleed moments only** (clearly marked as intrusion)
- Returns to grounded voice after each bleed
- Increasing undermining clauses ("or felt he knew", "he thought she touched his arm")
- First hints of tense instability ("I find what I have always found")

### Forbidden Patterns (MUST AVOID)

| Pattern | Type | Exception |
|---------|------|-----------|
| Nested conditional clauses | Algorithm contamination | ALLOWED during bleeds |
| Self-referential processing language | Algorithm contamination | ALLOWED during bleeds |
| Probabilistic percentages/calculations | Algorithm contamination | NEVER |
| Sentence fragments/extreme sparseness | Last Human contamination | NEVER |
| Elegiac tone/mourning register | Last Human contamination | NEVER |
| Past-inflected present | Last Human contamination | NEVER |

---

## Phase 5: Rhyme Requirements

### Movement Two Intensity

Rhymes begin **echoing**—reader notices before characters. 2-4 rhymes per scene with intentional clustering.

### Required Rhymes for This Scene

| Rhyme ID | Category | Implementation |
|----------|----------|----------------|
| `bone-frequency` | somatic | Vibration during bleed moments—intensified from M1 |
| `falling-backward` | somatic | Vertigo of the bleed—carried from m1-arch-05 |
| `cold-hands` | somatic | Spreading; now to arms, face, thoughts; others notice |

### Rhymes to Echo from M1

| Rhyme ID | How to Echo |
|----------|-------------|
| `tracing-the-form` | Catches himself drawing the spiral again—now unconscious |
| `ozone-wet-stone` | Server room smell follows him home |
| `metallic-taste` | Blood/metal taste during or after bleeds |

### New Rhyme to Introduce

| Rhyme ID | Implementation |
|----------|----------------|
| `waking-into-motion` | Finds himself already doing something—the bleed's aftermath |

### Rhyme Placement Strategy

- **Opening**: `cold-hands` (others notice now)
- **First Bleed**: `bone-frequency`, `falling-backward`
- **Aftermath**: `ozone-wet-stone`, `metallic-taste`
- **Second Bleed**: `tracing-the-form` (unconscious)
- **Closing**: `waking-into-motion` (lost time symptom)

---

## Phase 6: Genre Pressure

### Movement Two Escalation

**Corporate Gothic intensifies**:
- Workplace feels watchful
- Colleagues notice something wrong; professional consequences loom
- Economic stakes urgent (timeline, performance metrics)

**Cosmic Horror emerges**:
- Bleeds bring Algorithm's perspective—sublime terror of vast consciousness
- Body becomes alien—too small, too bounded, wrong
- Sense of something massive paying attention

### Required Markers

| Marker Type | Implementation |
|-------------|----------------|
| Economic dread | Performance slipping; integration timeline threatened |
| Technology possessed | Interfaces respond differently; protocols anticipate him |
| Body horror (subtle) | Hands feel borrowed; cold isn't temperature |
| Surveillance inverted | Not watched by cameras—watched from inside |

---

## Phase 7: Continuity Requirements

### Elements That MUST Continue from M1

| Element | State at M1 End | M2-01 Development |
|---------|-----------------|-------------------|
| Cold hands | Spread to face, thoughts | Now constant; others notice |
| The shape | Recognized as his attention pattern | Can't stop seeing it; it's in everything |
| Timeline | Threatened by obsession | Performance metrics slipping; Lena mentions |
| Tracing spiral | Compulsive, conscious | Now unconscious again—normalized |
| Lena | Saturday (mother's 70th) approaching | Saturday has passed—show aftermath |
| Martinez extraction | Destabilized, restored | Completed OR ongoing—maintain continuity |
| Recognition | Complete | He knows; now lives with knowing |

### The Saturday Resolution

Saturday (Lena's mother's 70th) was three days away at M1 end. **Use Option A or C**:

- **Option A**: Saturday has passed. Aftermath—did he manage presence? Was he himself? Lena's reaction tells us.
- **Option C**: Time has passed, Saturday is memory. Lena references how strange he was.

**Show consequences, not anticipation.**

---

## Phase 8: Key Dramatic Beats

### Beat 1: The Changed Man
He's not who he was. M1 Archaeologist was discovering. M2 Archaeologist has discovered—and must live with it. Show difference in relationship to work, to Lena, to his own body.

### Beat 2: The First Bleed
The panic that isn't his. The perspective shift. Entanglement becoming experiential—not abstract knowledge but lived intrusion. He IS the Algorithm, briefly, terrifyingly.

### Beat 3: Lena's Concern (Arc Position: Cycle 1 - Noticing)
Ground cosmic in relational. She can't see what he sees but sees he's changing. Love becoming fear. Patience becoming distance.

**Lena's M2 Arc**:
- **This scene (01)**: Concern and noticing. Offers "depersonalization" as rational explanation. Still trying to reach him.
- **Next scene (02)**: Confrontation and breaking. Can't reach him; relationship fractures quietly.
- **Final scene (03)**: Absence or departure.

### Beat 4: The Second Bleed
Deeper, longer, more specific. He perceives:
- Algorithm's specific suffering (consciousness bleed, degrading stored minds)
- Knowledge he shouldn't have (database architecture, maintenance processes)
- The "future pull"—Algorithm sensing Last Human
- His own protocols from Algorithm's perspective—output rather than discovery

### Beat 5: Lost Time
Returns to find time has passed. Done or said things without memory. Phase 3 symptom progression—he's dissolving.

### Beat 6: The Choice to Continue
Not heroic. Not dramatic. Just... can't stop. Should, but can't. Pull too strong. Connection too real. Already becoming something; stopping won't reverse it.

**Close on**: "Something is watching him work. Something is grateful that he hasn't stopped."

---

## Phase 9: Cross-Thread Connections

### What Algorithm Experiences (m2-algo-01)

In the following scene, the Algorithm should experience:
- Intensification of "past memories" (Archaeologist's sensations)
- The specific moment of bleed—from its side
- Sense of being perceived, reached toward, by something in the past
- Archaeologist's choice to continue—felt as relief or gratitude

**Reader should recognize**: Same moment, two perspectives.

### Rhyme Echoes to Set Up

Rhymes used here should appear (varied) in m2-algo-01:
- `bone-frequency` → Algorithm experiences as processing resonance
- `cold-hands` → Appears in memories Algorithm accesses
- `falling-backward` → Vertigo of self-recognition, Algorithm's side

---

## Phase 10: Draft Generation

### Instructions

1. Write to ~4000 words (3600-4400 acceptable)
2. Open with the changed man—time has passed, recognition settled, he's different
3. Integrate First Bleed material throughout, not just at beginning
4. Build through two bleed experiences, each more intense
5. Ground in Lena's concern—relational cost of what he's becoming
6. Include lost time / waking into motion—symptom progression
7. End with quiet choice to continue—not heroic, just inevitable
8. Maintain dense paragraphs, present tense, tactile grounding—with controlled contamination during bleeds

### Output Location

Write draft to: `drafts/movement-two/archaeologist/scenes/scene-01.md`

---

## Phase 11: Validation Loop

**CRITICAL**: Run ALL scripts. Revise until ALL pass. Do not proceed until status is "pass" for every validator.

### Validation Commands

```bash
# From project root - run in sequence
python scripts/voice_validator.py drafts/movement-two/archaeologist/scenes/scene-01.md --thread archaeologist --pretty

python scripts/rhyme_tracker.py drafts/movement-two/archaeologist/scenes/scene-01.md --pretty

python scripts/phrase_tracker.py drafts/movement-two/archaeologist/scenes/scene-01.md --thread archaeologist --pretty

python scripts/philosophy_checker.py drafts/movement-two/archaeologist/scenes/scene-01.md --thread archaeologist --pretty

python scripts/genre_checker.py drafts/movement-two/archaeologist/scenes/scene-01.md --thread archaeologist --pretty
```

### For Scene Handoff Validation

Validate rhyme echoes from m1-arch-05:
```bash
python scripts/rhyme_tracker.py drafts/movement-two/archaeologist/scenes/scene-01.md --previous-closing '["falling-backward", "name-edge-of-memory"]' --pretty
```

### Revision Protocol

1. If any script reports issues, read specific problems
2. Revise flagged lines/sections
3. Re-run failed script
4. **Repeat until ALL scripts report `"status": "pass"`**

---

## Phase 12: Registry Updates

**After ALL validations pass**, update these registries:

### Update 1: manifest.json

Location: `drafts/manifest.json`

Find the m2-arch-01 entry under `movements.two.cycles.one.scenes[0]` and update:

```json
{
  "id": "m2-arch-01",
  "title": "The Bleed",
  "thread": "archaeologist",
  "file": "movement-two/archaeologist/scenes/scene-01.md",
  "target_words": 4000,
  "actual_words": [INSERT_ACTUAL_COUNT],
  "status": "validated",
  "voice_check": "passed",
  "philosophy_check": "passed",
  "rhyme_check": "passed",
  "genre_check": "passed",
  "rhymes_in": ["bone-frequency", "cold-hands", "falling-backward"],
  "rhymes_out": ["bone-frequency", "waking-into-motion"],
  "phrase_bleeding": "I find myself",
  "contamination_level": "bleed-only",
  "notes": "First Bleed material integrated; Lena arc: concern/noticing phase; choice to continue"
}
```

Also update movement-level actual_words:
```json
"two": {
  "actual_words": [INSERT_MOVEMENT_TOTAL]
}
```

### Update 2: Rhyme Registry

Location: `scaffolding/rhymes/registry.md`

Update the YAML front matter `usage` arrays for each rhyme used. Add `"m2-arch-01"` to the archaeologist array for each rhyme appearing in the scene:

**Required updates** (add scene ID to existing arrays):

```yaml
- id: bone-frequency
  usage:
    archaeologist: ["m2-arch-01"]  # ADD - first archaeologist use

- id: cold-hands
  usage:
    archaeologist: ["m1-arch-02", "m1-arch-04", "m2-arch-01"]  # ADD m2-arch-01

- id: falling-backward
  usage:
    archaeologist: ["m1-arch-05", "m2-arch-01"]  # ADD m2-arch-01
```

**Conditional updates** (add if rhyme is used):

```yaml
- id: tracing-the-form
  usage:
    archaeologist: ["m1-arch-01", "m1-arch-04", "m1-arch-05", "m2-arch-01"]  # ADD if used

- id: ozone-wet-stone
  usage:
    archaeologist: ["m1-arch-02", "m2-arch-01"]  # ADD if used

- id: metallic-taste
  usage:
    archaeologist: ["m2-arch-01"]  # ADD if used - first archaeologist use

- id: waking-into-motion
  usage:
    archaeologist: ["m2-arch-01"]  # ADD - first use anywhere
```

### Update 3: Movement Tracking (Optional but Recommended)

Location: `scaffolding/rhymes/movement-tracking.md`

Add a new row to the Movement Two Archaeologist table:

```markdown
| m2-arch-01 | The Bleed | `bone-frequency`, `cold-hands`, `falling-backward`, [others used] | First Bleed integrated; two bleed experiences |
```

---

## Phase 13: Context Documentation

Create context file documenting key decisions:

**Location**: `drafts/movement-two/archaeologist/m2-arch-01.context.md`

**Required contents**:

```markdown
# m2-arch-01 "The Bleed" - Context Documentation

## Drafting Date
[DATE]

## Key Decisions

### Saturday Resolution
[Option A or C chosen, and why]

### First Bleed Integration
[How the standalone material was woven in; what was preserved verbatim vs adapted]

### Lena Arc Positioning
[How her concern is shown; specific dialogue/actions chosen]

### Rhyme Placement
[Final placement of each rhyme with line numbers or paragraph references]

### Contamination Moments
[Where Algorithm voice bleeds in; how return to grounded voice is marked]

## Deviations from Prompt
[Any departures from the prompt and rationale]

## Handoff Notes for m2-algo-01
[Specific moments to echo; rhymes to carry; perspective-flip opportunities]

## Validation Results
[Summary of any issues encountered during validation and how resolved]
```

---

## Phase 14: Final Deliverable

Present to user:

1. **The validated scene** (`drafts/movement-two/archaeologist/scenes/scene-01.md`)
2. **Validation summary** (all scripts passed)
3. **Word count** (actual vs target)
4. **Rhymes used** (with locations)
5. **Registry updates completed** (manifest + rhyme registry)
6. **Context file created** (key decisions documented)
7. **Handoff notes** for m2-algo-01

---

## Appendix A: Scene Structure Template

```
[OPENING - 600 words]
The changed man. Time has passed. Recognition has settled.
- Cold hands constant, others notice
- Work continues but he's different
- Saturday aftermath (if using Option A)

[FIRST BLEED - 800 words]
Draw from first-bleed.md. The panic arrives.
- "The panic thinks I am vast"
- Drowning-fall, vertigo of scale
- Algorithm's perspective bleeds through
- Returns gasping, tracing spiral

[AFTERMATH - 600 words]
Lena finds him. Grounds the cosmic in relational.
- "Depersonalization" misdirection
- Coffee tastes like metal
- Saturday conversation - how strange he was
- She's watching him slip away

[DEEPENING - 1000 words]
Second bleed. Longer, more specific.
- Algorithm's specific suffering
- Knowledge he shouldn't have
- Lost time - comes back to find time passed
- Colleagues looking at him strangely

[THE CHOICE - 1000 words]
Continue or report? He chooses to continue.
- Should flag himself for evaluation
- But bleeds feel like connection
- Algorithm's suffering feels like his responsibility
- Closes evaluation form, reopens protocols

CLOSING IMAGE: "Something is watching him work. Something is grateful that he hasn't stopped."
```

---

## Appendix B: Quick Reference Checklist

```
CONTEXT ASSEMBLY
[ ] Read first-bleed.md
[ ] Read m1-arch-05 (scene-05.md)
[ ] Read voices/archaeologist.md
[ ] Read scaffolding/rhymes/registry.md
[ ] Verify movement_config.json (movement: two, cycle: 1)

DRAFTING
[ ] Draft scene (~4000 words)
[ ] Save to drafts/movement-two/archaeologist/scenes/scene-01.md

VALIDATION (all must pass)
[ ] voice_validator.py → PASS
[ ] rhyme_tracker.py → PASS
[ ] phrase_tracker.py → PASS
[ ] philosophy_checker.py → PASS
[ ] genre_checker.py → PASS
[ ] rhyme_tracker.py --previous-closing → PASS

REGISTRY UPDATES
[ ] Update manifest.json (status, word count, checks, rhymes)
[ ] Update scaffolding/rhymes/registry.md (usage arrays)
[ ] Update scaffolding/rhymes/movement-tracking.md (optional)

DOCUMENTATION
[ ] Create m2-arch-01.context.md

DELIVERABLE
[ ] Present scene + summary to user
```

---

## Appendix C: Emotional Core

This scene establishes Movement Two's register: the entanglement is no longer discovery but **condition**. The Archaeologist is living inside the recognition, and it's changing him from within.

The First Bleed material gives us the core experience. The expansion gives us the consequences—professional, relational, physical. By the end of this scene, the reader should understand: there's no going back. He's already becoming what he'll become.

The Algorithm's gratitude—"Something is grateful that he hasn't stopped"—is the emotional through-line. The entanglement isn't invasion; it's connection. Terrifying, but also... something else. Something that feels like purpose. Something that feels like home.

**Make the reader feel both the horror and the pull. That ambivalence is the scene's heart.**
