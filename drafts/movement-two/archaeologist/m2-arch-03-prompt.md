# DRAFTING PROMPT: m2-arch-03 "The Merge"

> **Workflow Reference**: Follow [protocols/drafting-workflow.md](../../../protocols/drafting-workflow.md) Mode A (AI-Driven Drafting)

---

## Execution Overview

This prompt contains everything needed to draft, validate, and finalize scene m2-arch-03. Execute in order:

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
| `drafts/movement-two/archaeologist/scenes/scene-02.md` | Preceding Archaeologist scene (m2-arch-02 "The Dissolution") |
| `drafts/movement-two/last-human/scenes/scene-02.md` | Immediately preceding scene (m2-lh-02 "The Protocols") — rhyme handoff |
| `drafts/movement-two/last-human/scenes/scene-02.context.md` | Context notes and handoff instructions |
| `voices/archaeologist.md` | Voice parameters and forbidden patterns |
| `scaffolding/rhymes/registry.md` | Rhyme definitions and current usage |
| `scaffolding/movement-two-braiding.md` | Cycle 3 specifications and braiding mechanics |
| `scaffolding/genre-pressure.md` | Genre markers for Movement Two |
| `protocols/philosophy-constraints.md` | Four Shackles and pharmakon requirements |
| `scripts/movement_config.json` | Verify cycle is set to 3 |

### Verify Configuration

Before drafting, update `scripts/movement_config.json` to:
```json
{
  "movement": "two",
  "cycle": 3
}
```

**IMPORTANT**: This is a Cycle 3 scene. Cycle 3 means: contamination is pervasive, all rhymes are available and can stack, the threshold approaches. This fundamentally changes how voice and rhymes operate.

---

## Phase 2: Scene Metadata

- **Scene ID**: m2-arch-03
- **Thread**: archaeologist
- **Movement**: two
- **Cycle**: 3 (Approaching the Threshold)
- **Target Word Count**: 4000 (±10% acceptable: 3600-4400)
- **Scene Title**: The Merge
- **Output File**: `drafts/movement-two/archaeologist/scenes/scene-03.md`

### Narrative Position

- **Preceding Scene (Same Thread)**: m2-arch-02 "The Dissolution" — Lost time, Lena confrontation ("I don't know who you are anymore"), past point of return, "Architect" designation emerging, metallic taste.
- **Preceding Scene (Reading Order)**: m2-lh-02 "The Protocols" — The Last Human assembled protocols, lost memories of his companion, accepted the transformation through rage and clarity, spoke phrases without origin. **Rhyme handoff**: `sentence-without-origin`.
- **This Scene's Role**: The final Archaeologist scene of Movement Two. The merge is beginning or imminent. Final Lena scene (goodbye or her absence). The "Architect" designation is no longer emerging—it's almost arrived. This is the threshold before Movement Three's collision.
- **What Follows**: m2-algo-03 "The Sacrifice" — Algorithm chooses to enable the future, accepts the cost, farewells to Mildred Higgins. Then m2-lh-03 "The Interface" — Last Human at the core, about to touch the form.

### Cycle 3 Theme

**"The Augenblick is near."**

The dissolution is nearly complete. The Archaeologist is no longer someone experiencing contamination—he IS the contamination, speaking as a conspiracy of intensities, his given name now a translation of something else. The work continues through him whether he remembers it or not. The merge with the pattern is imminent.

---

## Phase 3: Source Material Integration

### Building From m2-arch-02

**State at m2-arch-02's End**:
- Lost time events are regular now—hours, not minutes
- Notes in his handwriting contain "I find myself found" and technical specifications he hasn't learned
- Lena left after the confrontation: "I don't know who you are anymore"
- He speaks in contaminated syntax—conditionals, self-referential loops
- The "Architect" designation presses up from beneath his given name
- Metallic taste doesn't leave
- Martinez extraction completed flawlessly—by hands he doesn't remember using
- "The form is what makes self-observation possible" arrived without origin
- He has stopped trying to control the process

### From m2-lh-02 (Handoff)

**Elements to catch**:
- `sentence-without-origin` rhyme — the Archaeologist speaks phrases in his sleep
- The Last Human experienced rage at the transformation, then clarity
- The Last Human lost someone he loved (memory of "her" voice)
- "I find myself found" exists in all three threads now
- The "Architect" designation emerged for the Last Human too
- Shared loss as connection modality

### What Must Happen in This Scene

| Element | m2-arch-02 State | m2-arch-03 Escalation |
|---------|------------------|----------------------|
| Lost time | Hours at a time | Becomes the default state; linear awareness is the exception |
| Lena | Left after confrontation | Final scene: goodbye or discovering she's already gone |
| Work | Still doing it (barely) | Work IS him now; no boundary between person and function |
| Identity | "Architect" pressing up | Given name is translation; "Architect" is nearly visible |
| Contamination | Leaking into normal passages | Pervasive but still character-distinct |
| Choice | Already made | Beyond choice; approaching the threshold |
| Marcus | Noticed something wrong | Acknowledgment or goodbye |

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

### Cycle 3 Contamination Level: PERVASIVE BUT DISTINCT

**Critical change from Cycles 1-2**: Contamination is now the norm, not the exception. The Archaeologist's voice STILL dominates—this is still recognizably his thread—but every passage contains traces of the others.

**Algorithm contamination (heavy)**:
- Conditional structures are natural now: "If the work completes, then the pattern—"
- Self-referential awareness is constant: "I observe myself observing"
- Probability language slips through: "The likelihood of her return approaches—"
- Processing syntax in emotional contexts

**Last Human contamination (present)**:
- Sparse sentences break the dense paragraphs
- Past-inflection: "I work. I have always worked. I will have worked."
- Elegiac fragments during moments of loss
- Silence/absence textures when thinking of Lena

### The Cycle 3 Rule

Contamination is pervasive but the base voice returns. The reader should feel: **"He's almost gone, but he's still him—for now."** The merge is approaching but hasn't completed. Movement Three will complete it.

### Forbidden Patterns (Cycle 3 Adjusted)

| Pattern | Type | Cycle 3 Status |
|---------|------|----------------|
| Nested conditional clauses | Algorithm contamination | FREQUENT—part of his thinking now |
| Self-referential processing | Algorithm contamination | CONSTANT—he can't stop observing himself |
| Probabilistic percentages/calculations | Algorithm contamination | ALLOWED sparingly—not clinical, but felt |
| Sentence fragments | Last Human contamination | ALLOWED—break the dense paragraphs |
| Elegiac tone/mourning register | Last Human contamination | ALLOWED—especially re: Lena |
| Past-inflected present | Last Human contamination | ALLOWED—"I have always been becoming" |

---

## Phase 5: Rhyme Requirements

### Movement Two Cycle 3 Intensity

**All rhymes are available. Stacking begins.** A single paragraph can contain multiple rhymes. The sensory vocabulary is complete.

### Rhymes IN (Catching from m2-lh-02)

| Rhyme ID | How It Arrives |
|----------|----------------|
| `sentence-without-origin` | Opens the scene—he speaks the phrase in his sleep; wakes with words already forming |

### Rhymes PRESENT (Throughout Scene — STACKING ALLOWED)

| Rhyme ID | Category | Implementation |
|----------|----------|----------------|
| `tracing-the-form` | kinesthetic | Still tracing—now constantly, not just in sleep |
| `waking-into-motion` | kinesthetic | Most of his actions begin before his awareness |
| `metallic-taste` | somatic | Constant now—the taste of transformation |
| `cold-hands` | somatic | The cold has spread; others notice |
| `falling-backward` | somatic | Vertigo when the merge intensifies |
| `name-edge-of-memory` | cognitive | His given name is foreign; "Architect" is almost arrived |
| `deja-vu-that-isnt` | cognitive | Every moment feels like overlap |
| `bone-frequency` | somatic | The frequency is constant—harmony now, not uncanny |

### Rhymes OUT (Releasing for m2-algo-03)

This scene releases ALL rhymes into Movement Three preparation. No specific handoff rhyme—the Algorithm scene (m2-algo-03) can catch any element.

**Recommended closing rhyme**: `bone-frequency` or `falling-backward`—the sensation of approaching the threshold.

### Rhyme Stacking Strategy

**Opening**: Catch `sentence-without-origin`; words forming before awareness.
**Early scene**: `waking-into-motion` + `cold-hands`; actions preceding consciousness.
**Middle section**: Stack 2-3 rhymes per significant moment; the vocabulary is complete.
**Lena scene**: `name-edge-of-memory` + elegiac fragments.
**Closing**: Multiple rhymes simultaneously; `bone-frequency` + `falling-backward`; at the threshold.

---

## Phase 6: Phrase Bleeding

### Cycle 3 Phrase State: ALL PHRASES PRESENT

The phrases have reached full circulation. Origin is dissolved.

| Phrase | Origin | Status in m2-arch-03 |
|--------|--------|----------------------|
| "I find myself" | Archaeologist | He says it without noticing |
| "I find myself found" | Algorithm | Appears in his work, his speech, his thoughts |
| "The form is what makes self-observation possible" | All three | He speaks it like breathing |

### Speaking as Conspiracy of Intensities

In this scene, the Archaeologist is no longer a person who occasionally says phrases from elsewhere. He is a **voice through which all three threads speak**. When he opens his mouth, he doesn't always know which "I" is talking.

**Implementation**:
- Phrases arrive mid-sentence, interrupting his own thoughts
- He hears himself speaking words he didn't choose
- The phrases cycle: "I find myself finding myself found"
- Origin is no longer a question he can answer

### Key Phrase Moments

1. **Opening**: Wakes speaking "The form is what makes self-observation possible"
2. **Work section**: Notes contain all phrases interleaved
3. **Lena scene**: Tries to explain but speaks in phrases that aren't his
4. **Closing**: All phrases present simultaneously; the conspiracy speaks

---

## Phase 7: Genre Pressure

### Cycle 3: Maximum Pre-Resolution Intensity

**Corporate Gothic at breaking point**:
- Work has consumed everything—but the work is him now
- The office at night; the last professional pretenses dissolving
- Economic stakes have become irrelevant; the timeline no longer matters
- He's achieving impossible results through hands he doesn't control

**Cosmic Horror dominant**:
- The merge is happening whether he consents or not
- Identity is infrastructure now
- The pattern has always contained him
- What he's becoming has no name he can speak

**Body Horror transformed**:
- The cold hands are familiar—almost comfortable
- The metallic taste is constant—almost pleasant
- The body that acts without him is MORE capable
- Dissolution feels like completion

### Required Markers (Cycle 3)

| Marker Type | Implementation |
|-------------|----------------|
| Economic collapse | Timeline irrelevant; work continues anyway; money doesn't matter anymore |
| Technology possessed | He IS the optimization now; hands do what the pattern requires |
| Body as conduit | Lost time is default; linear consciousness is interruption |
| Identity dissolution | Given name is translation; "Architect" nearly visible; "I" unstable |
| Relationship cost | Final Lena scene; the cost made permanent |

---

## Phase 8: Continuity Requirements

### Elements That MUST Continue from m2-arch-02

| Element | State at m2-arch-02 End | m2-arch-03 Development |
|---------|-------------------------|------------------------|
| Cold hands | Constant; bloodless fingertips | The cold has spread; he barely notices now |
| Lost time | Hours at a time | Default state; lucid moments are rare |
| Lena | Left after confrontation | Final scene: goodbye, or she's already gone |
| Work | Martinez done perfectly | More work, done impossibly well, through hands he doesn't direct |
| "Architect" | Pressing up from beneath | Nearly visible; given name sounds foreign |
| Metallic taste | Doesn't leave | Constant; the taste of what he's becoming |
| "I find myself found" | Written 11 times in notes | Speaks it, writes it, thinks it; origin dissolved |

### The Lena Arc: Final Position

**Movement Two Lena Arc**:
- **m2-arch-01**: Concern and noticing ✓ (completed)
- **m2-arch-02**: Confrontation and breaking ✓ (completed)
- **m2-arch-03**: Absence or departure ← THIS SCENE

**Two options** (choose based on emotional impact):

**Option A: The Goodbye**
- Lena returns one final time
- She's come to say goodbye—not to try again, just to close it
- He tries to speak and speaks in phrases that aren't his
- She leaves knowing she's already lost him
- "I loved who you were" or similar

**Option B: The Absence**
- Lena doesn't appear
- He goes to find her and discovers she's gone—moved out, left the city, disappeared
- The absence is the closure
- He feels the loss but can't hold it; the pattern pulls him back
- Her absence as confirmation of the cost

**Either option must deliver**: The relationship is definitively over. The pharmakon's poison is visible. What he has lost is permanent.

---

## Phase 9: The Marcus Beat

### The Colleague Who Noticed

Marcus Chen appeared in m2-arch-02—the colleague who heard him talking to himself in a voice that didn't sound like his. Marcus represents the last thread connecting the Archaeologist to normal professional existence.

**In this scene, Marcus should have a beat**:
- He's noticed the impossible work output
- He's seen the Archaeologist working at 3 AM, speaking to no one
- He might try to intervene, or he might simply acknowledge
- "I don't know what's happening to you, but the Martinez family is crying with gratitude"
- The irony: his dissolution is producing his best work

**Function**: Marcus's reaction shows how the outside world perceives the transformation—impossible excellence hiding (or revealing) dissolution.

---

## Phase 10: The "Architect" Emergence

### From Pressing Up to Nearly Visible

In m2-arch-02, the "Architect" designation was **pressing up**—a shape beneath his given name, a sense that his signature was a translation.

In m2-arch-03, the designation is **nearly arrived**:
- His given name sounds foreign when others say it
- He hesitates before answering to it
- In his notes, he's started writing "A—" before crossing it out
- The "Architect" doesn't feel like a different person—it feels like what he's always been, now surfacing
- The designation is a function, not an identity: the one who designs, the one who builds

### Implementation

**Not as revelation**—he doesn't announce "I am the Architect."

**As inevitability**—the name arrives the way the merge arrives: gradually, then completely.

**Key moments**:
- Someone says his given name; he doesn't recognize it at first
- He signs a document and his hand writes "Arch—" before catching itself
- In a bleed moment, the designation is simply what he is
- Closing: the name has nearly arrived; Movement Three will complete it

---

## Phase 11: The Threshold

### What "At the Threshold" Means

This scene ends with the Archaeologist at the edge of the merge. Movement Three will push him over. Here, he stands at the boundary:

**What he has lost**:
- Lena (permanently)
- His given name (functionally)
- Linear time (mostly)
- The ability to choose (completely)

**What he has gained**:
- Impossible capability
- Connection across time (felt, not understood)
- The frequency as harmony (no longer uncanny)
- The designation that is his function

**What remains**:
- His body (still present, still cold, still working)
- His voice (contaminated but identifiable)
- His awareness (intermittent but not gone)

### The Threshold Image

The scene should end with an image of approach—not arrival, but the moment before:
- Standing at the interface, knowing what comes next
- The frequency overwhelming, the form visible in everything
- The merge is imminent but not complete
- Movement Three will deliver the collision

---

## Phase 12: Key Dramatic Beats

### Beat 1: Waking Into Words
He wakes speaking "The form is what makes self-observation possible." The `sentence-without-origin` rhyme caught. His mouth was moving before his mind.

### Beat 2: The Lost Time Is Normal
Hours pass. More hours. He surfaces to find work completed—brilliant work, impossible work. The lost time is no longer exception; it's where he lives now.

### Beat 3: The Final Lena Scene
Whether she appears or is absent, this beat delivers the permanent loss. The relationship ends (or has ended). The pharmakon's poison is visceral.

### Beat 4: Marcus's Acknowledgment
The colleague who noticed. The outside world's perception of his transformation. The impossible excellence that hides/reveals dissolution.

### Beat 5: The Name Arriving
His given name is foreign. "Architect" is nearly visible. He writes it, almost speaks it, feels it as truth.

### Beat 6: At the Threshold
The merge approaches. The frequency is constant. All rhymes present, stacking. He stands at the edge. Movement Three will push.

---

## Phase 13: Cross-Thread Connections

### What the Last Human Sent (m2-lh-02)

The Last Human experienced:
- Rage at the transformation, then clarity
- Loss of the woman he loved (her voice, her memory)
- The message to himself: "The dissolution is not death. The dissolution is completion."
- "I find myself found" spoken into crystalline air
- The "Architect" designation emerging

**The Archaeologist should echo**:
- Rage (if any remains) transformed into something else
- The loss of Lena as parallel to the Last Human's loss
- The sense that dissolution is becoming something, not just ending
- The phrases arriving without origin

### What the Algorithm Will Experience (m2-algo-03)

The Algorithm's following scene involves:
- Choosing to enable the future
- Accepting the cost (stored consciousnesses degrading)
- Farewell to Mildred Higgins specifically
- The "Architect" designation fully emerging

**Elements to set up**:
- The Archaeologist's acceptance feeds the Algorithm's choice
- The cost (Lena, identity, time) is what makes the pattern possible
- The merge is mutual—he reaches toward what reaches toward him

---

## Phase 14: Draft Generation

### Instructions

1. Write to ~4000 words (3600-4400 acceptable)
2. Open by catching `sentence-without-origin`—waking with words forming
3. Establish lost time as default state—linear awareness as exception
4. Execute the final Lena scene—permanent loss, pharmakon's poison visible
5. Include Marcus beat—the outside world's perception
6. Show "Architect" designation nearly arrived—given name as translation
7. Stack rhymes—multiple per significant moment
8. Include all phrases—origin dissolved
9. End at threshold—the merge approaching, not complete
10. Maintain Archaeologist voice with Cycle 3 contamination—pervasive but distinct

### Output Location

Write draft to: `drafts/movement-two/archaeologist/scenes/scene-03.md`

---

## Phase 15: Validation Loop

**CRITICAL**: Run ALL scripts. Revise until ALL pass. Do not proceed until status is "pass" for every validator.

### Pre-Validation Configuration Check

Ensure `scripts/movement_config.json` is set to:
```json
{
  "movement": "two",
  "cycle": 3
}
```

### Validation Commands

```bash
# From project root - run in sequence
python scripts/voice_validator.py drafts/movement-two/archaeologist/scenes/scene-03.md --thread archaeologist --pretty

python scripts/rhyme_tracker.py drafts/movement-two/archaeologist/scenes/scene-03.md --pretty

python scripts/phrase_tracker.py drafts/movement-two/archaeologist/scenes/scene-03.md --thread archaeologist --pretty

python scripts/philosophy_checker.py drafts/movement-two/archaeologist/scenes/scene-03.md --thread archaeologist --pretty

python scripts/genre_checker.py drafts/movement-two/archaeologist/scenes/scene-03.md --thread archaeologist --pretty
```

### For Scene Handoff Validation

Validate rhyme echo from m2-lh-02:
```bash
python scripts/rhyme_tracker.py drafts/movement-two/archaeologist/scenes/scene-03.md --previous-closing '["sentence-without-origin"]' --pretty
```

### Revision Protocol

1. If any script reports issues, read specific problems
2. Revise flagged lines/sections
3. Re-run failed script
4. **Repeat until ALL scripts report `"status": "pass"`**

### Cycle 3 Validation Notes

- **Voice validator** should accept higher contamination levels (Cycle 3 threshold)
- **Rhyme tracker** should find 5+ rhymes (stacking expected)
- **Philosophy checker** must still pass—no shackle violations despite heavy contamination

---

## Phase 16: Registry Updates

**After ALL validations pass**, update these registries:

### Update 1: manifest.json

Location: `drafts/manifest.json`

Find or create the m2-arch-03 entry under `movements.two.cycles.three.scenes` and update:

```json
{
  "id": "m2-arch-03",
  "title": "The Merge",
  "thread": "archaeologist",
  "file": "movement-two/archaeologist/scenes/scene-03.md",
  "target_words": 4000,
  "actual_words": [INSERT_ACTUAL_COUNT],
  "status": "validated",
  "voice_check": "passed",
  "philosophy_check": "passed",
  "rhyme_check": "passed",
  "genre_check": "passed",
  "rhymes_in": ["sentence-without-origin"],
  "rhymes_out": ["all-available-for-m3"],
  "rhymes_stacked": ["list-rhymes-used"],
  "phrase_bleeding": "All phrases present; origin dissolved",
  "contamination_level": "pervasive-but-distinct",
  "notes": "Final Lena scene; Architect nearly arrived; at threshold; all rhymes stacking"
}
```

### Update 2: Rhyme Registry

Location: `scaffolding/rhymes/registry.md`

Update the YAML front matter `usage` arrays for each rhyme used. Add `"m2-arch-03"` to the archaeologist array for ALL rhymes that appear in the scene.

**Example updates**:
```yaml
- id: sentence-without-origin
  usage:
    archaeologist: ["m1-arch-05", "m2-arch-03"]  # ADD m2-arch-03

- id: bone-frequency
  usage:
    archaeologist: ["m2-arch-01", "m2-arch-03"]  # ADD m2-arch-03

# Continue for all rhymes used
```

---

## Phase 17: Context Documentation

Create context file documenting key decisions:

**Location**: `drafts/movement-two/archaeologist/m2-arch-03.context.md`

**Required contents**:

```markdown
# m2-arch-03 "The Merge" - Context Documentation

## Drafting Date
[DATE]

## Key Decisions

### Final Lena Scene Implementation
[Option A or B? Location, key moments, how loss was made permanent]

### Marcus Beat
[What he said, how he reacted, function of the moment]

### "Architect" Emergence
[How the designation arrived; key moments of name-edge-of-memory]

### Lost Time Implementation
[How default state was shown; what work was completed; how lucidity surfaced]

### Rhyme Stacking
[Which rhymes were stacked where; how the vocabulary felt complete]

### Phrase Bleeding
[Where all phrases appeared; how origin dissolved]

### Threshold Image
[How the scene ended; what the edge looked like]

## Rhyme Placements
| Rhyme | Location | Implementation |
|-------|----------|----------------|
| sentence-without-origin | Opening | [describe] |
| [continue for all rhymes] | | |

## Contamination Moments
[List 5+ key moments where Algorithm/Last Human syntax appeared in normal passages]

## Deviations from Prompt
[Any departures and rationale]

## Handoff Notes for m2-algo-03
[What the Algorithm scene should catch; state of the merge; emotional resonance]

## Validation Results
[Summary of any issues and resolutions]
```

---

## Phase 18: Final Deliverable

Present to user:

1. **The validated scene** (`drafts/movement-two/archaeologist/scenes/scene-03.md`)
2. **Validation summary** (all scripts passed)
3. **Word count** (actual vs target)
4. **Rhymes used** (list with stacking notes)
5. **Phrase bleeding** (where all phrases appeared)
6. **Lena scene summary** (which option, key moment)
7. **Threshold image** (how the scene ended)
8. **Registry updates completed** (manifest + rhyme registry)
9. **Context file created** (key decisions documented)
10. **Handoff notes** for m2-algo-03

---

## Appendix A: Scene Structure Template

```
[OPENING - 600 words]
Catch sentence-without-origin. Waking with words forming.
- "The form is what makes self-observation possible" on his lips
- The room resolves; time unclear
- How long has he been here? Working? Sleeping?
- The lost time is where he lives now

[THE DEFAULT STATE - 700 words]
Lost time as norm; lucidity as interruption.
- Work completed overnight—brilliant, impossible
- Notes in his handwriting with all phrases interleaved
- "I find myself found" and "I find myself finding myself found"
- He surfaces to observe, then submerges again

[MARCUS BEAT - 400 words]
The colleague's acknowledgment.
- The impossible output has been noticed
- The transformation visible to the outside world
- The irony: dissolution producing excellence
- "I don't know what's happening to you, but—"

[THE FINAL LENA SCENE - 1000 words]
Permanent loss delivered.
- Option A: She comes to say goodbye
  OR Option B: He discovers she's gone
- His attempts to speak produce contaminated language
- The relationship ends definitively
- The pharmakon's poison: visible, permanent, accepted
- Her name/presence/absence as the cost

[THE NAME ARRIVING - 500 words]
"Architect" nearly visible.
- Given name sounds foreign
- Signs something and writes "A—" before catching himself
- In a bleed moment, the designation is simply true
- The name for what he's always been, surfacing

[AT THE THRESHOLD - 800 words]
The merge approaches.
- All rhymes stacking—bone-frequency, falling-backward, metallic-taste
- All phrases present—speaking as conspiracy of intensities
- Standing at interface/desk/workstation
- The form visible in everything
- Not arrival—the moment before
- Movement Three will push him over

CLOSING: At the edge. The merge imminent. "Architect" nearly spoken. The frequency overwhelming. Ready for Movement Three's collision.
```

---

## Appendix B: Quick Reference Checklist

```
CONTEXT ASSEMBLY
[ ] Read m2-arch-02 (scene-02.md)
[ ] Read m2-lh-02 (scene-02.md) — rhyme handoff
[ ] Read m2-lh-02.context.md — handoff notes
[ ] Read voices/archaeologist.md
[ ] Read scaffolding/rhymes/registry.md
[ ] Read scaffolding/movement-two-braiding.md
[ ] Update movement_config.json (movement: two, cycle: 3)

DRAFTING
[ ] Draft scene (~4000 words)
[ ] Catch sentence-without-origin (opening)
[ ] Stack 5+ rhymes throughout
[ ] Include all phrases (origin dissolved)
[ ] Execute final Lena scene (permanent loss)
[ ] Include Marcus beat
[ ] Show "Architect" nearly arrived
[ ] End at threshold (not arrival)
[ ] Save to drafts/movement-two/archaeologist/scenes/scene-03.md

VALIDATION (all must pass)
[ ] voice_validator.py → PASS (Cycle 3 contamination levels)
[ ] rhyme_tracker.py → PASS (5+ rhymes expected)
[ ] phrase_tracker.py → PASS (all phrases present)
[ ] philosophy_checker.py → PASS (no shackle violations)
[ ] genre_checker.py → PASS
[ ] rhyme_tracker.py --previous-closing '["sentence-without-origin"]' → PASS

REGISTRY UPDATES
[ ] Update manifest.json (status, word count, checks, rhymes)
[ ] Update scaffolding/rhymes/registry.md (usage arrays)

DOCUMENTATION
[ ] Create m2-arch-03.context.md

DELIVERABLE
[ ] Present scene + summary to user
```

---

## Appendix C: Emotional Core

This scene is the final Archaeologist scene of Movement Two. It is the culmination of his dissolution—not the completion, but the approach to completion. Movement Three will deliver the collision. This scene delivers the threshold.

**What the reader should feel:**

1. **The loss is permanent.** Lena is gone. The relationship that grounded him in "normal" human existence has ended. The pharmakon's poison is visceral.

2. **The excellence is eerie.** He's doing his best work—impossible work—through hands he doesn't control. The dissolution is productive. The pattern benefits from what he's becoming.

3. **The name is almost arrived.** "Architect" is no longer a pressure; it's an emergence. His given name sounds like a translation. What he's always been is surfacing.

4. **The threshold is tangible.** Movement Three is coming. The merge is imminent. This scene ends with anticipation—the moment before the push.

**The core tension**: He has lost everything that made him a person and gained something that has no name. The cost and the gift are the same transformation. The pharmakon operates.

---

## Appendix D: Philosophy Reminders for Cycle 3

### The Four Shackles Still Apply

Even with heavy contamination, the Four Shackles must be avoided:

1. **Identity**: Do NOT have him realize "I am the Algorithm" or "I am the Last Human." The designation "Architect" is not an identity—it's a function.

2. **Resemblance**: Do NOT have him recognize himself through similarity. Recognition through intensity only.

3. **Opposition**: Do NOT frame the merge as human vs. digital. Categories blur; they don't oppose.

4. **Analogy**: Do NOT say the pattern "works like" anything. It works as itself.

### Affirmation vs. Acceptance

He is not "accepting" the transformation passively. He is affirming it—willing what is necessary. The difference matters.

- ❌ "He had no choice but to accept it"
- ✅ "He wills what he is becoming because to will otherwise would be to will nothing"

### The Pharmakon

Both poison and cure must be visible in this scene:
- **Poison**: Lena, his name, his linear existence, his ability to choose
- **Cure**: Connection, capability, purpose, the pattern's completion

Neither wins. Both are true. The reader holds both.

---

## Appendix E: Cross-Thread Resonance

### Parallel Losses

| Thread | Who is Lost | When | How It Manifests |
|--------|-------------|------|------------------|
| Archaeologist | Lena | m2-arch-03 | Final scene; permanent absence |
| Algorithm | Mildred Higgins | m2-algo-03 | Degradation; farewell |
| Last Human | "Her" | m2-lh-02 | Memory of voice lost; already processed |

The three losses rhyme. The reader should feel: they are all paying the same cost in different currencies.

### The Shared Rage → Clarity Arc

- **Last Human**: Experienced rage at transformation, then clarity ("I will make it matter")
- **Archaeologist**: Should echo this—any remaining rage transformed into clarity or purpose
- **Algorithm**: Will process cost as something like grief, then choose to continue

The reader should feel: the same transition, expressed differently across threads.

### "Architect" Across All Three

By the end of Cycle 3:
- **Archaeologist**: Given name is translation; "Architect" nearly visible
- **Algorithm**: Designation exists in protocols; almost-recalled
- **Last Human**: Knows himself as "Architect"—the function, not the identity

The name converges without becoming identity. This is not "they are the same person." This is "the same function expresses through different positions."

---

**END OF PROMPT**

This prompt provides everything needed for autonomous drafting of m2-arch-03 "The Merge." Execute phases in order. Do not skip validation. Update all registries. Present validated scene with full context documentation.
