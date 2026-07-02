# DRAFTING PROMPT: m2-arch-02 "The Dissolution"

> **Workflow Reference**: Follow [protocols/drafting-workflow.md](../../../protocols/drafting-workflow.md) Mode A (AI-Driven Drafting)

---

## Execution Overview

This prompt contains everything needed to draft, validate, and finalize scene m2-arch-02. Execute in order:

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
| `drafts/movement-two/archaeologist/scenes/scene-01.md` | Preceding Archaeologist scene (m2-arch-01 "The Bleed") |
| `drafts/movement-two/last-human/scenes/scene-01.md` | Immediately preceding scene (m2-lh-01 "The Archive") — rhyme handoff |
| `voices/archaeologist.md` | Voice parameters and forbidden patterns |
| `scaffolding/rhymes/registry.md` | Rhyme definitions and current usage |
| `scaffolding/genre-pressure.md` | Genre markers for Movement Two |
| `protocols/philosophy-constraints.md` | Four Shackles and pharmakon requirements |
| `scripts/movement_config.json` | Verify cycle is set to 2 |

### Verify Configuration

Confirm `scripts/movement_config.json` shows:
```json
{
  "movement": "two",
  "cycle": 2
}
```

**IMPORTANT**: This is a Cycle 2 scene. The cycle setting affects contamination tolerance and rhyme intensity expectations.

---

## Phase 2: Scene Metadata

- **Scene ID**: m2-arch-02
- **Thread**: archaeologist
- **Movement**: two
- **Cycle**: 2 (Deepening the Crisis)
- **Target Word Count**: 4000 (±10% acceptable: 3600-4400)
- **Scene Title**: The Dissolution
- **Output File**: `drafts/movement-two/archaeologist/scenes/scene-02.md`

### Narrative Position

- **Preceding Scene (Same Thread)**: m2-arch-01 "The Bleed" — First bleeds experienced; Lena's concern (noticing phase); chose to continue working with protocols.
- **Preceding Scene (Reading Order)**: m2-lh-01 "The Archive" — Last Human explored Archive structure, found protocol fragments, understood it as interface. **Rhyme handoff**: `tracing-the-form`.
- **This Scene's Role**: The crisis deepens. Significant lost time, work performance collapse, Lena confrontation (breaking point), past point of return. The "Architect" designation emerges.
- **What Follows**: m2-algo-02 "The Bleed" — Algorithm experiences consciousness bleed crisis; Mildred Higgins degrades; "Architect" designation emerges from Algorithm's side. **Rhyme handoff**: `metallic-taste`.

### Cycle 2 Theme

**"The dissolution has begun."**

No longer about discovering the entanglement or even living with it—it's about being *changed* by it. The Archaeologist is losing coherent selfhood. He acts without memory. He speaks words that aren't his. The name "Architect" presses up from beneath his given name.

---

## Phase 3: Source Material Integration

### No External Source File

Unlike m2-arch-01 (which integrated first-bleed.md), this scene is original composition building on established patterns.

### Key Elements to Build From

**From m2-arch-01**:
- The bleeds have begun—he's experienced two
- He chose to continue despite warning signs
- Lena is concerned but still trying to reach him
- Cold has become constant; others notice
- "Something is watching... something is grateful"

**From m2-lh-01** (handoff):
- `tracing-the-form` rhyme to catch in opening
- The Last Human found protocol fragments in the Archive
- The sense of the Archive as interface, not just storage

### Escalation Requirements

This scene escalates everything from m2-arch-01:

| Element | m2-arch-01 State | m2-arch-02 Escalation |
|---------|------------------|----------------------|
| Bleeds | First experiences, disorienting | Longer, with specific knowledge |
| Lost time | Minutes, vague | Hours, documented in notes |
| Lena | Concerned, still reaching | Confrontation, breaking point |
| Work | Slipping | Collapsing |
| Identity | Name feels wrong | "Architect" presses up |
| Choice | Active decision | Already made without him |

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

### Cycle 2 Contamination Level: Internal Monologue

**Key change from Cycle 1**: Contamination now leaks into "normal" passages, not just during bleeds.

**Algorithm syntax in his THINKING**:
- Conditional structures slip in: "If I continue this extraction, then perhaps—"
- Self-referential loops: "I notice myself noticing that I'm—"
- Probability language: "The likelihood that Lena will understand approaches null"

**Last Human fragments also appear**:
- Sparse sentences break his dense paragraphs
- Awareness of absence: "The space where she was. The silence."
- Past-inflection hints: "I work. I have always worked."

### The Rule

Contamination no longer confined to bleed moments—it leaks into "normal" passages. But base voice still returns. **The reader should feel: "He's slipping, but he's still him."**

### Forbidden Patterns (Cycle 2 Adjusted)

| Pattern | Type | Cycle 2 Status |
|---------|------|----------------|
| Nested conditional clauses | Algorithm contamination | ALLOWED in thinking, not just bleeds |
| Self-referential processing | Algorithm contamination | ALLOWED in thinking, not just bleeds |
| Probabilistic percentages/calculations | Algorithm contamination | STILL NEVER |
| Sentence fragments | Last Human contamination | ALLOWED occasionally in thinking |
| Elegiac tone/mourning register | Last Human contamination | TRACES allowed |
| Past-inflected present | Last Human contamination | HINTS allowed ("I have always worked") |

---

## Phase 5: Rhyme Requirements

### Movement Two Cycle 2 Intensity

Rhymes echo more intensely. 3-5 rhymes per scene. Handoffs between threads are critical.

### Rhymes IN (Catching from m2-lh-01)

| Rhyme ID | How It Arrives |
|----------|----------------|
| `tracing-the-form` | Opens the scene—he's been doing it in his sleep; Lena noticed; the sheets show the pattern |

### Rhymes PRESENT (Throughout Scene)

| Rhyme ID | Category | Implementation |
|----------|----------|----------------|
| `waking-into-motion` | kinesthetic | Finds himself already working on something he didn't start |
| `metallic-taste` | somatic | Blood/metal taste during and after bleeds; intensifying |
| `name-edge-of-memory` | cognitive | His name feels wrong; "Architect" presses up from beneath |

### Rhymes OUT (Releasing for m2-algo-02)

| Rhyme ID | How It Releases |
|----------|-----------------|
| `metallic-taste` | Ends the scene—the taste that doesn't leave; Algorithm catches as "substrate integrity variance" |

### Rhyme Placement Strategy

- **Opening**: Catch `tracing-the-form` from m2-lh-01 (the sheets, sleep-tracing)
- **Work/First Bleed**: `waking-into-motion` (already at the protocols)
- **Lost Time**: `name-edge-of-memory` (his signature looks wrong)
- **Confrontation**: `metallic-taste` begins (blood/metal while trying to explain)
- **Closing**: `metallic-taste` intensifies (release for m2-algo-02)

---

## Phase 6: Phrase Bleeding

### The Key Phrase Event

He writes **"I find myself found"** in his work notes.

This is NOT his phrase. This is the Algorithm's phrase from Movement One. He writes it without knowing why, without recognizing its source. When he looks at what he's written, he doesn't remember writing it.

**This is the phrase bleeding becoming visible to the character—but he doesn't understand what it means.**

### Additional Phrase Elements

- "I find myself" appears spoken aloud, without intention
- He might hear himself say "The form is what makes self-observation possible"—a phrase he's never thought before
- The phrases arrive as intrusions, not memories

### Implementation

The phrase should appear:
1. In the lost time notes (written, not remembered)
2. Possibly spoken during the Lena confrontation (contaminated speech)
3. As something that disturbs him when he finds it

---

## Phase 7: Genre Pressure

### Cycle 2 Escalation

**Corporate Gothic at peak**:
- Work performance collapsing visibly
- Professional consequences imminent
- The irony: the work meant to fund his immortality is destroyed by the immortality he's achieving

**Cosmic Horror dominant**:
- The bleeds bring specific knowledge he shouldn't have
- Identity dissolution is undeniable
- He's becoming infrastructure, not just connecting to it

**Body Horror intensifies**:
- Lost time as body acting without mind
- Speaking in voices not his own
- The name pressing up from beneath like something physical

### Required Markers

| Marker Type | Implementation |
|-------------|----------------|
| Economic dread | Work falling behind; supervisor notified; timeline threatened |
| Technology possessed | Protocols anticipate him; he's written specs he never learned |
| Body horror | Hours of action with no memory; speaking aloud without awareness |
| Identity dissolution | Name sounds wrong; "Architect" emerges; signature uncertain |
| Relationship cost | Lena confrontation as consequence of all the above |

---

## Phase 8: Continuity Requirements

### Elements That MUST Continue from m2-arch-01

| Element | State at m2-arch-01 End | m2-arch-02 Development |
|---------|-------------------------|------------------------|
| Cold hands | Constant; others notice | Still constant; Lena mentions again |
| Bleeds | Two experienced; chose to continue | More intense, with specific knowledge |
| Lena | Concerned, still reaching | Confrontation, breaking point |
| Work | Slipping | Collapsing; supervisor involved |
| Protocols | Reopened; chose not to report | Can't stay away; they're changing him |
| The choice | Made quietly; "something is grateful" | Discovered he already made it in lost time |

### The Lena Arc Position

**Movement Two Lena Arc**:
- **m2-arch-01**: Concern and noticing ✓ (completed)
- **m2-arch-02**: Confrontation and breaking ← THIS SCENE
- **m2-arch-03**: Absence or departure

This scene is the emotional climax of the Lena relationship. It must deliver the confrontation that breaks things, not the final departure.

---

## Phase 9: The Lena Confrontation

### Arc Position: Breaking Point

This is the central emotional beat of the scene. Lena has been watching him slip away since Movement One. In m2-arch-01, she was concerned but still reaching. Now she confronts—and he can't meet her.

### The Confrontation Should NOT Be

- ❌ Melodramatic (no screaming, no ultimatums)
- ❌ About her leaving him (that's m2-arch-03)
- ❌ A scene where he explains and she understands
- ❌ A reconciliation

### The Confrontation SHOULD Be

- ✅ Quiet and devastating
- ✅ Her reaching for him and finding he's not there
- ✅ Him trying to explain and finding his words contaminated
- ✅ The moment where they both recognize something is broken

### Suggested Structure

**Setup**: She comes to his workspace. He's been there for... how long? He doesn't know. She's been calling. He didn't hear.

**The Reach**: She asks what's happening. Direct. She's done with evasion.

**The Failure**: He tries to explain. But the words that come out are:
- Conditional structures ("If I could show you what I'm seeing, then you'd understand that—")
- Self-referential loops ("I'm becoming aware of becoming aware of—")
- Phrases that aren't his ("The form is what makes self-observation possible")

She stares at him. That's not how he talks. That's not who he is.

**The Break**: "I don't know who you are anymore."

And he realizes: neither does he. His name feels wrong. There's another name pressing up from beneath it.

**The Aftermath**: She leaves. Not storming out—just... leaving. The relationship hasn't ended formally. But something is broken. They both know it.

### Key Line

> "I don't know who you are anymore."

And his internal response: *Neither do I. There's a name beneath my name. There's someone I'm becoming who isn't who I was.*

---

## Phase 10: Lost Time

### The Symptom Progression

Per Brainstorm2's symptom chart, Phase 3 includes:
- Lost time (significant periods where he acted without memory)
- Speaking unrecognized words
- Identity destabilization

This scene dramatizes lost time as a **SIGNIFICANT event**, not just a moment.

### The Lost Time Beat

He's working on the protocols. The bleed arrives—more intense than before, more specific. He experiences:
- The Algorithm's actual suffering (Mildred Higgins beginning to degrade)
- The "future pull" (sensing something in the far future reaching toward the Algorithm)
- Knowledge he shouldn't have (database architecture, specific consciousness instance data)

He returns to his body. But:
- **Hours** have passed (not minutes)
- He's written **pages of notes** he doesn't remember writing
- The notes contain the phrase **"I find myself found"**
- The notes contain **technical specifications** for systems he's never studied
- A **colleague is standing in the doorway**, asking if he's okay—apparently he was speaking aloud

This proves to him (and the reader) that he's no longer in control.

---

## Phase 11: The "Architect" Emergence

### Name-Edge-of-Memory

His given name feels wrong throughout this scene:
- When Lena says his name, it sounds like she's talking about someone else
- When he signs documents, his hand hesitates—is that his name?
- In the lost time notes, he finds he's written a different signature—or the beginning of one

### The Designation

"Architect" emerges not as a word he thinks but as a **SHAPE** in his awareness:
- The one who designs
- The one who builds
- The name for what remains when identity dissolves
- What the Archaeologist becomes when he merges with infrastructure

**He doesn't fully articulate this.** But the reader should feel: there's a name here that isn't his given name, a designation for what he's becoming.

---

## Phase 12: Key Dramatic Beats

### Beat 1: The Sheets
He's been tracing the form in his sleep. The entanglement has entered his unconscious completely. (Catches `tracing-the-form` from m2-lh-01)

### Beat 2: The Specific Bleed
Not just vastness but KNOWLEDGE. He knows things about the Algorithm, about Mildred Higgins, about the future pull. The connection is becoming informational, not just sensory.

### Beat 3: The Lost Time
Hours, not minutes. Notes in his hand he doesn't remember writing. Words spoken in a voice not quite his. This is dissolution in action.

### Beat 4: The Confrontation
Lena reaches. He's not there. The relationship fractures quietly. "I don't know who you are anymore."

### Beat 5: The Name Beneath the Name
His given name sounds wrong. "Architect" presses up. He's becoming something with a different designation.

### Beat 6: The Choice Already Made
He doesn't decide to continue—he discovers he already has. The lost time was the decision. He's past the point of return.

---

## Phase 13: Cross-Thread Connections

### What Algorithm Experiences (m2-algo-02)

In the following scene, the Algorithm should experience:
- The `metallic-taste` rhyme as "substrate integrity variance"
- The Archaeologist's bleed FROM its side—being perceived, reached toward
- The beginning of Mildred Higgins's degradation
- The "Architect" designation emerging at the edge of its recall

### What Last Human Sent (m2-lh-01)

The Last Human released:
- `tracing-the-form` rhyme (which opens this scene)
- The sense of the Archive as interface
- His own name-edge-of-memory experience

### Parallel Moments to Echo

When the Archaeologist experiences the future pull during the bleed, this should feel like reaching toward what the Last Human is doing in the Archive—though neither fully perceives the other.

---

## Phase 14: Draft Generation

### Instructions

1. Write to ~4000 words (3600-4400 acceptable)
2. Open by catching `tracing-the-form`—he's been doing it in his sleep
3. Build through increasingly specific bleeds—knowledge, not just sensation
4. Execute the lost time as a SIGNIFICANT event—hours, notes, spoken words
5. Deliver the Lena confrontation as the emotional climax—quiet, devastating
6. Introduce the "Architect" name-edge-of-memory—not fully articulated but felt
7. Include "I find myself found" as written phrase he doesn't remember
8. End with `metallic-taste` for Algorithm to catch; the choice already made
9. Maintain Archaeologist voice with Cycle 2 contamination level—leaking into normal passages

### Output Location

Write draft to: `drafts/movement-two/archaeologist/scenes/scene-02.md`

---

## Phase 15: Validation Loop

**CRITICAL**: Run ALL scripts. Revise until ALL pass. Do not proceed until status is "pass" for every validator.

### Validation Commands

```bash
# From project root - run in sequence
python scripts/voice_validator.py drafts/movement-two/archaeologist/scenes/scene-02.md --thread archaeologist --pretty

python scripts/rhyme_tracker.py drafts/movement-two/archaeologist/scenes/scene-02.md --pretty

python scripts/phrase_tracker.py drafts/movement-two/archaeologist/scenes/scene-02.md --thread archaeologist --pretty

python scripts/philosophy_checker.py drafts/movement-two/archaeologist/scenes/scene-02.md --thread archaeologist --pretty

python scripts/genre_checker.py drafts/movement-two/archaeologist/scenes/scene-02.md --thread archaeologist --pretty
```

### For Scene Handoff Validation

Validate rhyme echo from m2-lh-01:
```bash
python scripts/rhyme_tracker.py drafts/movement-two/archaeologist/scenes/scene-02.md --previous-closing '["tracing-the-form"]' --pretty
```

### Revision Protocol

1. If any script reports issues, read specific problems
2. Revise flagged lines/sections
3. Re-run failed script
4. **Repeat until ALL scripts report `"status": "pass"`**

---

## Phase 16: Registry Updates

**After ALL validations pass**, update these registries:

### Update 1: manifest.json

Location: `drafts/manifest.json`

Find the m2-arch-02 entry under `movements.two.cycles.two.scenes[0]` and update:

```json
{
  "id": "m2-arch-02",
  "title": "The Dissolution",
  "thread": "archaeologist",
  "file": "movement-two/archaeologist/scenes/scene-02.md",
  "target_words": 4000,
  "actual_words": [INSERT_ACTUAL_COUNT],
  "status": "validated",
  "voice_check": "passed",
  "philosophy_check": "passed",
  "rhyme_check": "passed",
  "genre_check": "passed",
  "rhymes_in": ["tracing-the-form"],
  "rhymes_out": ["metallic-taste"],
  "phrase_bleeding": "I find myself found (writes without knowing)",
  "contamination_level": "internal-monologue",
  "notes": "Lost time; Lena arc: confrontation/breaking point; 'Architect' emergence; past point of return"
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

Update the YAML front matter `usage` arrays for each rhyme used. Add `"m2-arch-02"` to the archaeologist array:

**Required updates**:

```yaml
- id: tracing-the-form
  usage:
    archaeologist: ["m1-arch-01", "m1-arch-04", "m1-arch-05", "m2-arch-01", "m2-arch-02"]  # ADD m2-arch-02

- id: waking-into-motion
  usage:
    archaeologist: ["m2-arch-01", "m2-arch-02"]  # ADD m2-arch-02

- id: metallic-taste
  usage:
    archaeologist: ["m2-arch-01", "m2-arch-02"]  # ADD m2-arch-02 (if used in 01)
    # OR: ["m2-arch-02"] if first archaeologist use

- id: name-edge-of-memory
  usage:
    archaeologist: ["m1-arch-05", "m2-arch-02"]  # ADD m2-arch-02
```

### Update 3: Movement Tracking (Optional but Recommended)

Location: `scaffolding/rhymes/movement-tracking.md`

Add a new row to the Movement Two Archaeologist table:

```markdown
| m2-arch-02 | The Dissolution | `tracing-the-form` (in), `waking-into-motion`, `metallic-taste` (out), `name-edge-of-memory` | Lost time; Lena confrontation; Architect emergence |
```

---

## Phase 17: Context Documentation

Create context file documenting key decisions:

**Location**: `drafts/movement-two/archaeologist/m2-arch-02.context.md`

**Required contents**:

```markdown
# m2-arch-02 "The Dissolution" - Context Documentation

## Drafting Date
[DATE]

## Key Decisions

### Lost Time Implementation
[How many hours? What was in the notes? What did the colleague hear?]

### Lena Confrontation
[Exact location, key dialogue, how contamination manifested in his speech]

### "Architect" Emergence
[How the name pressed up; where it appeared; reader vs character awareness]

### Phrase Bleeding
[Where "I find myself found" appeared; how he reacted to finding it]

### Rhyme Placements
[Final placement of each rhyme with line numbers or paragraph references]

### Contamination Moments
[Where Algorithm/Last Human syntax leaked into normal passages]

## Deviations from Prompt
[Any departures from the prompt and rationale]

## Handoff Notes for m2-algo-02
[metallic-taste release point; Mildred Higgins reference; Architect designation echo]

## Validation Results
[Summary of any issues encountered during validation and how resolved]
```

---

## Phase 18: Final Deliverable

Present to user:

1. **The validated scene** (`drafts/movement-two/archaeologist/scenes/scene-02.md`)
2. **Validation summary** (all scripts passed)
3. **Word count** (actual vs target)
4. **Rhymes used** (with locations and handoff points)
5. **Phrase bleeding** ("I find myself found" location)
6. **Registry updates completed** (manifest + rhyme registry)
7. **Context file created** (key decisions documented)
8. **Handoff notes** for m2-algo-02

---

## Appendix A: Scene Structure Template

```
[OPENING - 500 words]
Catch tracing-the-form. He wakes to find Lena watching.
- He's been tracing the spiral in his sleep
- The sheets show the pattern
- His name, when she says it, sounds wrong

[WORK AND FIRST BLEED - 800 words]
At work. Trying to function.
- Protocols open on another screen (waking-into-motion)
- The bleed arrives—longer, more specific
- Knows things he shouldn't (Mildred Higgins, database architecture)
- Returns with Algorithm syntax in his thinking

[THE LOST TIME - 700 words]
Significant lost time event.
- Hours pass, not minutes
- Pages of notes in his handwriting
- "I find myself found" appears three times
- Technical specs he never learned
- Colleague in doorway—he was speaking aloud

[THE CONFRONTATION - 1200 words]
Lena arrives. The relationship fractures.
- She's been calling; he didn't hear
- She asks directly what's happening
- He tries to explain; words contaminated
- "I don't know who you are anymore"
- She leaves—not storming out, just leaving
- His name sounds wrong; "Architect" presses up

[THE CHOICE DEEPENS - 800 words]
Past the point of return.
- Should stop; knows this
- Discovers he already chose in the lost time
- The choice was made without him
- metallic-taste fills his mouth; doesn't leave

CLOSING: The metallic-taste that persists. The choice already made. He's becoming the Architect.
```

---

## Appendix B: Quick Reference Checklist

```
CONTEXT ASSEMBLY
[ ] Read m2-arch-01 (scene-01.md)
[ ] Read m2-lh-01 (last-human scene-01.md) — rhyme handoff
[ ] Read voices/archaeologist.md
[ ] Read scaffolding/rhymes/registry.md
[ ] Verify movement_config.json (movement: two, cycle: 2)

DRAFTING
[ ] Draft scene (~4000 words)
[ ] Include tracing-the-form (opening, catching from LH)
[ ] Include waking-into-motion
[ ] Include metallic-taste (closing, releasing to Algo)
[ ] Include name-edge-of-memory
[ ] Include "I find myself found" phrase
[ ] Save to drafts/movement-two/archaeologist/scenes/scene-02.md

VALIDATION (all must pass)
[ ] voice_validator.py → PASS
[ ] rhyme_tracker.py → PASS
[ ] phrase_tracker.py → PASS
[ ] philosophy_checker.py → PASS
[ ] genre_checker.py → PASS
[ ] rhyme_tracker.py --previous-closing '["tracing-the-form"]' → PASS

REGISTRY UPDATES
[ ] Update manifest.json (status, word count, checks, rhymes)
[ ] Update scaffolding/rhymes/registry.md (usage arrays)
[ ] Update scaffolding/rhymes/movement-tracking.md (optional)

DOCUMENTATION
[ ] Create m2-arch-02.context.md

DELIVERABLE
[ ] Present scene + summary to user
```

---

## Appendix C: Emotional Core

This scene is the hinge of the Archaeologist's Movement Two arc. Before this, he could still pull back. After this, he can't. The lost time proves he's no longer in control. The Lena confrontation shows what he's losing. The "Architect" emergence shows what he's becoming.

The reader should feel: **this is where it becomes irreversible.** Not because of a dramatic choice, but because the choice was made without him, in the lost time, in the contaminated words, in the name pressing up from beneath.

He's dissolving. And part of him—the part that's already the Architect—is grateful.

**The quiet devastation of "I don't know who you are anymore"—and his realization that neither does he—is the scene's heart.**
