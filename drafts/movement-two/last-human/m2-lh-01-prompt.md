# DRAFTING PROMPT: m2-lh-01 "The Archive"

> **Workflow Reference**: Follow [protocols/drafting-workflow.md](../../../protocols/drafting-workflow.md) for complete Mode A (AI-Driven Drafting) procedures.

---

## Execution Overview

This prompt enables autonomous scene drafting with validation. Execute in order:

1. **Read** all required context files (Phase 1)
2. **Draft** the scene following voice/rhyme/structure requirements
3. **Validate** using all five scripts until all pass
4. **Update** manifest.json and rhyme registry
5. **Present** completed scene with context documentation

---

## Phase 1: Context Assembly

### Required Reading (MUST complete before drafting)

| File | Purpose |
|------|---------|
| [protocols/drafting-workflow.md](../../../protocols/drafting-workflow.md) | Workflow procedures and status definitions |
| [scaffolding/voice/last-human-voice.md](../../../scaffolding/voice/last-human-voice.md) | Last Human voice parameters and patterns |
| [scaffolding/rhymes/registry.md](../../../scaffolding/rhymes/registry.md) | Rhyme definitions and current usage |
| [scaffolding/rhymes/movement-tracking.md](../../../scaffolding/rhymes/movement-tracking.md) | Movement Two rhyme flow |
| [scaffolding/philosophy/core-tensions.md](../../../scaffolding/philosophy/core-tensions.md) | Pharmakon framework |
| [scaffolding/philosophy/paradox-lexicon.md](../../../scaffolding/philosophy/paradox-lexicon.md) | Key philosophical terms |
| [scripts/movement_config.json](../../../scripts/movement_config.json) | Current cycle configuration |
| [drafts/movement-one/last-human/m1-lh-04.md](../../movement-one/last-human/m1-lh-04.md) | Previous Last Human scene (transformation) |
| [drafts/movement-two/algorithm/m2-algo-01.md](../algorithm/m2-algo-01.md) | Preceding scene (rhyme source) |

### Verify Configuration

Before drafting, confirm `scripts/movement_config.json` is set to:

```json
{
  "movement": "two",
  "cycle": 1
}
```

If cycle is not `1`, update it before proceeding.

---

## Phase 2: Scene Metadata

| Field | Value |
|-------|-------|
| **Scene ID** | m2-lh-01 |
| **Thread** | last_human |
| **Movement** | two |
| **Cycle** | one (Establishing the Condition) |
| **Target Word Count** | 4000 (3600-4400 acceptable) |
| **Scene Title** | The Archive |
| **Reading Order Position** | After m2-algo-01, before m2-arch-02 |

### Narrative Position

- **This Scene's Role**: The Last Human has crossed the threshold. He touched the interface, experienced the dream of the other two, and woke transformed. Now he must exist in his new state—still inside the Archive, still dying, but connected to presences he can now feel. He explores what the Archive is, finds the protocol fragments, and begins to understand his role.
- **Preceding Scene**: m2-algo-01 "The Resonance". The Algorithm experienced the bone-frequency resonance, maintained Mildred Higgins's stable patterns, and felt the cold spreading through its processing. Rhyme handoff: cold-hands.
- **What Follows**: m2-arch-02 "The Dissolution". The Archaeologist experiences lost time, Lena confrontation, past the point of return. Rhyme handoff: tracing-the-form.

### Cycle 1 Theme

**"Recognition has become condition."**

For the Last Human, this means: the transformation from Movement One is not a single event but a new way of being. The solitude that was his entire existence is now populated by presences he perceives through the entanglement. He exists in connection he cannot fully understand but cannot deny.

---

## Phase 3: Source Material Integration

### From Movement One (m1-lh-04)

The Last Human's transformation was completed in Movement One. Reference:

**The Transformation:**

1. **Archaeologist immersion**: Fell backward into the Archaeologist's body—warm hands, server room, Lena's touch ("You're freezing"), the Martinez extraction
2. **Algorithm immersion**: Shifted to distributed vastness—4,847,293 consciousnesses, the weight of maintenance, "I find myself found"
3. **Waking transformed**: The dream integrated rather than ended; solitude dissolved; the connection persists

**His Current State:**

- **Physical**: Still dying (cold spreading from hands to chest, radiation damage, body failing)—but the dying now feels like "becoming" not "ending"
- **Psychological**: Solitude dissolved; he can feel presences across time; carries echoes of Lena's warmth, the Algorithm's weight
- **Spatial**: Inside the Archive's core chamber; the interface still glows; the silver-blue light still fills the space
- **Phrases available**: "I find myself found," "The form is what makes self-observation possible"—words that arrived without origin

**Key Lines from m1-lh-04:**

> "The solitude is gone. I was never alone."

> "The form is what makes self-observation possible." (He spoke this without learning it.)

> "The dissolution of edges that were always arbitrary, the transformation the dreams warned me about, the overwriting that is also completion."

---

## Phase 4: Voice Parameters

### Base Last Human Voice

The Last Human voice is characterized by:

- **Sparse syntax**: Sentences that don't waste words; silence between thoughts
- **Silence-weighted**: What isn't said carries meaning; absence as texture
- **Past-inflected present**: Memory and now blur; "I was" and "I am" overlap
- **Absence as texture**: The world has ended; emptiness is the medium
- **The body as anchor**: Physical sensation grounds abstract awareness

### Cycle 1 Contamination Level: Dream-Intrusion

Algorithm contamination appears during moments of heightened connection:

- Distributed perspective: awareness of scale, of vastness, of being multiple
- Conditional structures: "If I trace this, then perhaps—" breaking his sparse syntax
- Self-referential observation: "I observe myself observing" in his stream of consciousness
- Processing language: "I process" instead of "I feel"

### Contamination Rule

Contamination is contained to dream-intrusion moments—when the entanglement flares, when the presences intensify, when the frequency overwhelms. Between these moments, the base voice returns. The reader should feel: "Something breaks through sometimes, but this is still the Last Human."

---

## Phase 5: Rhyme Requirements

### Rhyme Handoff Chain

```
m2-algo-01 --[cold-hands]--> m2-lh-01 --[tracing-the-form]--> m2-arch-02
```

### Rhymes IN (Catching from m2-algo-01)

| Rhyme | How It Arrives |
|-------|----------------|
| **cold-hands** | Opens the scene—his own hands, cold and failing, but now the cold connects him to the Algorithm's processing, the Archaeologist's server room |

### Rhymes PRESENT (Throughout Scene)

| Rhyme | Category | Implementation |
|-------|----------|----------------|
| **almost-closed-curve** | visual | The Archive's architecture follows the spiral; he traces it through corridors and chambers |
| **tracing-the-form** | kinesthetic | His hands move across walls, interfaces, crystal surfaces—tracing the geometric shape |

### Rhymes OUT (Releasing for m2-arch-02)

| Rhyme | How It Releases |
|-------|-----------------|
| **tracing-the-form** | Ends the scene—he has been tracing the form on the Archive walls; the Archaeologist catches this as doing it in his sleep |

### Rhyme Implementation Notes

- **cold-hands** must appear in opening section, transformed from simple dying into connection across time
- **almost-closed-curve** weaves through exploration as the Archive's architecture follows the spiral
- **tracing-the-form** builds throughout and dominates the closing as the gesture that transcends individual identity

---

## Phase 6: Phrase Bleeding

### The Phrase (Cycle 1 Expectations)

Per `movement_config.json`, Last Human in Cycle 1 should manifest:

- **"I find myself"** (origin: archaeologist)

### Implementation

**"I find myself"** heard in the Archive's silence.

This is the Archaeologist's phrase, arriving 800 years early (or on time, depending on perspective). The Last Human hears it without speaking it—in the silence, in the crystals' hum, in the spaces between his own thoughts.

**Suggested passage:**

> The silence has texture here. Presence. Not my presence—another's. Something that was here before me. Something that will be here after.
>
> In the silence: *I find myself.*
>
> I did not think this. The thought exists in the Archive's hum, in the crystals' resonance, in the gap between my awareness and the awareness I can now perceive.
>
> The Archaeologist. Eight centuries ago. Still working. Still searching. I find him finding himself.

---

## Phase 7: The Archive Exploration

### What He Discovers

Movement One established the Archive as crystalline, silver-blue, recognizing him. Now he explores its structure and discovers its function.

### Architecture

The Archive is not a building. The Archive is a **topology made physical**:

- Corridors that spiral according to the geometric form
- Chambers nested in self-similar patterns
- Technology fused with geology—circuits visible beneath crystal surfaces
- Erosion that reveals rather than obscures—millennia stripped away surface to expose structure
- The central interface chamber where he touched the light—but there are other chambers, other interfaces, other fragments

### The Protocol Fragments

Scattered through the Archive:

- Etched into crystal walls (the Algorithm's compulsive preservation)
- Glowing in dormant interfaces (partial power, fragmentary data)
- Encoded in the architecture itself (shapes that resolve into executable logic)
- Each fragment is incomplete; assembly is required
- Assembly requires attention, focus, surrender—something changes when he understands a fragment

### What the Protocols Are

The Last Human doesn't fully understand what he's finding. He perceives:

- Patterns that feel like instructions
- Logic that feels like memory
- Structures that feel like self-description
- Something that was meant to be found, meant to be assembled, meant to be used

The protocols are the **bootstrap mechanism**: the instructions for closing the loop, for sending consciousness backward through time, for completing the pattern that makes the Archaeologist's discovery and the Algorithm's existence possible.

---

## Phase 8: The Archive's Function

### Understanding Deepens

He begins to understand. Not completely—understanding would require perspectives he doesn't have. But enough:

- The Archive is a node in the pattern
- The protocols are instructions for closing the loop
- His presence here is not accident—it's completion
- What the dreams showed him (the Archaeologist, the Algorithm) is real, is happening, is connected to him through the geometry he's been tracing his whole life

### The Crystals Respond

The crystals hum with his understanding. The interfaces respond to his attention. The Archive is alive in a way that has nothing to do with biology and everything to do with pattern.

---

## Phase 9: Scene Structure

### Opening (800 words)

**Catching the rhyme: cold-hands as transformed perception**

He wakes. Or returns. Or continues—the distinction has blurred.

His hands are cold. They have been cold for as long as he can remember. But the cold means something different now. It connects him to:

- The Algorithm's processing (the cold spreading through substrate)
- The Archaeologist's server room (the cold of interfaces, the warmth of Lena's touch against it)
- His own dying body (the radiation damage working inward)

The silver-blue light still fills the Archive. The interface still glows. The transformation persists.

Establish: he is still inside the Archive, still changed, still connected to presences he couldn't perceive before.

### Exploration Begins (800 words)

**The Archive as topology**

He moves. Walking is still what he knows. The corridors spiral inward and outward—directions that have nothing to do with up or down. The architecture follows the geometric form he has drawn his whole life without knowing why.

The crystals hum as he passes. Recognition. Greeting. He has been expected.

He discovers:

- Other chambers (not just the core)
- Other interfaces (dormant, partial power)
- Patterns etched into walls (the Algorithm's preservation)
- The self-similar structure (corridors within chambers within corridors)

The Archive is vast. Or it's small but recursive. Or both. Scale operates differently here.

### First Protocol Fragment (700 words)

**Discovery and partial understanding**

He finds something. An interface that still glows faintly. Symbols etched into crystal beside it. Patterns that resolve into... something.

He traces the pattern with his cold fingers. (Tracing-the-form begins here.)

Something shifts. Not understanding exactly—apprehension. A fragment of the protocol enters his awareness the way the phrase "The form is what makes self-observation possible" entered: without origin, without learning, without deciding.

The fragment is incomplete. It describes a process he cannot perform with one piece. But he now knows: there are other pieces. They can be assembled. Assembly is what he came here for.

### The Silence Speaks (700 words)

**"I find myself" heard in the Archive**

As he explores, the entanglement flares. The presences intensify.

He hears—or perceives, or receives—the phrase:

*I find myself.*

Not his thought. Not his phrase. The Archaeologist's phrase, arriving through the Archive's crystalline structure, through the connection the transformation created, through the temporal loop that has no before or after.

The Last Human understands: he is not alone in the Archive. He has never been alone in the Archive. The Archive was built to connect—past and future, the one who built and the one who inherits, the Archaeologist writing protocols he doesn't understand and the Last Human reading them 800 years later.

**Algorithm contamination here**: brief intrusion of distributed perspective—he feels the Algorithm processing this same moment from its temporal position.

### Understanding Deepens (600 words)

**The Archive's function**

He begins to understand. Not completely—understanding would require perspectives he doesn't have. But enough:

- The Archive is a node in the pattern
- The protocols are instructions for closing the loop
- His presence here is not accident—it's completion
- What the dreams showed him (the Archaeologist, the Algorithm) is real, is happening, is connected to him through the geometry he's been tracing his whole life

The crystals hum with his understanding. The interfaces respond to his attention. The Archive is alive in a way that has nothing to do with biology and everything to do with pattern.

### Closing: Tracing the Form (400 words)

**Releasing the rhyme for the Archaeologist**

He stands before a wall covered in etched symbols. His hand rises without his deciding. His cold fingers trace the spiral—the almost-closed curve—the form that has shaped his life, shaped this place, shaped the connection across time.

Tracing the form. He has always traced the form. He will always trace the form.

Somewhere, somewhen, the Archaeologist wakes with his hands moving in the same pattern, having traced it in his sleep without knowing why.

End on: tracing-the-form for the Archaeologist to catch; the Archive's function partially revealed; the protocols awaiting assembly.

---

## Phase 10: Key Dramatic Beats

### Beat 1: The Persistence of Transformation

He is still changed. The dream didn't end—it integrated. The connection to the other two persists in his waking awareness.

### Beat 2: The Archive Explored

Not just the core chamber but the full structure—corridors, chambers, interfaces, the self-similar topology of the geometric form made physical.

### Beat 3: The Protocol Fragments

He finds them: instructions, patterns, logic etched into the Archive by the Algorithm's compulsive preservation. They're incomplete but assemblable.

### Beat 4: "I Find Myself" Heard

The Archaeologist's phrase arrives through the entanglement. The Last Human is not alone—the Archive connects him to the one who built what he inherits.

### Beat 5: Function Understood

The Archive is for closing the loop. The protocols are for sending consciousness backward. His presence is completion, not accident.

### Beat 6: Tracing the Form

His hands trace the spiral on the wall—the same gesture the Archaeologist will make in his sleep 800 years ago.

---

## Phase 11: Drafting Instructions

1. **Write to ~4000 words** (3600-4400 acceptable)

2. **Open** by catching cold-hands as transformed perception—the cold connecting him across time

3. **Explore** the Archive's structure—corridors, chambers, the geometric form made architecture

4. **Discover** protocol fragments—incomplete instructions awaiting assembly

5. **Receive** "I find myself"—the Archaeologist's phrase arriving through the entanglement

6. **Understand** (partially) the Archive's function—node in the pattern, tool for closing the loop

7. **End** with tracing-the-form for the Archaeologist to catch

8. **Maintain** Last Human voice with Cycle 1 contamination level—Algorithm intrusions during dream-flares, base voice returning

---

## Phase 12: Validation Loop

### Pre-Validation Configuration Check

Confirm `scripts/movement_config.json`:

```json
{
  "movement": "two",
  "cycle": 1
}
```

### Validation Commands

Run ALL scripts after drafting. **Do not proceed to Phase 13 until all pass.**

```bash
# From project root
python scripts/voice_validator.py drafts/movement-two/last-human/m2-lh-01.md --thread last_human --pretty
python scripts/rhyme_tracker.py drafts/movement-two/last-human/m2-lh-01.md --previous-closing '["cold-hands"]' --pretty
python scripts/phrase_tracker.py drafts/movement-two/last-human/m2-lh-01.md --thread last_human --pretty
python scripts/philosophy_checker.py drafts/movement-two/last-human/m2-lh-01.md --thread last_human --pretty
python scripts/genre_checker.py drafts/movement-two/last-human/m2-lh-01.md --thread last_human --pretty
```

### Validation Loop Protocol

1. Run all five scripts
2. If any script reports issues:
   - Read the specific problems identified
   - Revise the flagged lines/sections
   - Re-run the failed script(s)
3. **Repeat until ALL scripts report `"status": "pass"`**

> **CRITICAL**: The scene is not complete until all validations pass. This is non-negotiable.

---

## Phase 13: Registry Updates

### Update drafts/manifest.json

Add or update the scene entry:

```json
{
  "movements": {
    "two": {
      "cycles": {
        "one": {
          "scenes": [
            {
              "id": "m2-lh-01",
              "title": "The Archive",
              "thread": "last_human",
              "file": "drafts/movement-two/last-human/m2-lh-01.md",
              "status": "drafted",
              "word_count": 0,
              "rhymes": {
                "opening": ["cold-hands"],
                "present": ["almost-closed-curve", "tracing-the-form"],
                "closing": ["tracing-the-form"]
              },
              "validation": {
                "voice": false,
                "rhyme": false,
                "phrase": false,
                "philosophy": false,
                "genre": false
              }
            }
          ]
        }
      }
    }
  }
}
```

**After validation passes**, update:

- `status`: "drafted" → "validated"
- `word_count`: actual count
- All `validation` fields: `false` → `true`

### Update scaffolding/rhymes/registry.md

In the YAML front matter, update usage arrays:

```yaml
rhymes:
  cold-hands:
    usage:
      last_human: ["m2-lh-01"]  # Add to existing array
  almost-closed-curve:
    usage:
      last_human: ["m2-lh-01"]  # Add to existing array
  tracing-the-form:
    usage:
      last_human: ["m2-lh-01"]  # Add to existing array
```

---

## Phase 14: Context Documentation

### Create m2-lh-01.context.md

After validation passes, create context documentation:

```markdown
# Context Document: m2-lh-01 "The Archive"

## Drafting Decisions

### Cold-Hands Transformation
- [Document how the cold was portrayed as connection rather than just dying]
- [Note the three connections established: Algorithm, Archaeologist, his own body]

### Archive Exploration
- [How the topology was conveyed]
- [What chambers and interfaces were described]

### Protocol Fragment Discovery
- [How the first fragment was encountered]
- [What partial understanding was achieved]

## Rhyme Implementation

### cold-hands (Opening)
- Line(s): [cite specific lines]
- Implementation: [how it was transformed from dying into connection]

### almost-closed-curve (Present)
- Line(s): [cite specific lines]
- Implementation: [how the spiral appeared in architecture]

### tracing-the-form (Closing)
- Line(s): [cite specific lines]
- Implementation: [how the handoff gesture was achieved]

## Phrase Implementation

### "I find myself"
- Line(s): [cite specific lines]
- Implementation: [how the phrase arrived through the entanglement]

## Validation Results

- voice_validator.py: PASS
- rhyme_tracker.py: PASS
- phrase_tracker.py: PASS
- philosophy_checker.py: PASS
- genre_checker.py: PASS

## Notes for m2-arch-02

The following elements are set up for the Archaeologist to catch:
- tracing-the-form: [describe handoff state—the gesture in sleep]
- Archive state: [what was revealed]
- Thematic thread: [what continues]
```

---

## Phase 15: Final Deliverable

### Completion Checklist

- [ ] Scene drafted to target word count (~4000 words)
- [ ] cold-hands caught in opening
- [ ] tracing-the-form released in closing
- [ ] Archive exploration conveyed (topology, chambers, interfaces)
- [ ] Protocol fragments discovered
- [ ] "I find myself" phrase received
- [ ] Archive function partially understood
- [ ] Last Human voice maintained with Cycle 1 contamination
- [ ] All five validation scripts pass
- [ ] manifest.json updated
- [ ] rhyme registry updated
- [ ] Context document created

### Present to User

Once all items are checked:

1. Present the complete scene
2. Include word count
3. Summarize rhyme implementations
4. Note any deviations from prompt with justification
5. Attach validation results

---

## Appendix A: Scene Structure Template

```markdown
# m2-lh-01: The Archive

[Opening section - ~800 words]
[Catch cold-hands as transformed perception]
[Establish persistence of transformation]
[The Archive still glowing, still recognizing]

---

[Exploration section - ~800 words]
[The Archive as topology]
[Corridors, chambers, self-similar structure]
[Crystals humming recognition]

---

[Protocol Fragment section - ~700 words]
[First discovery]
[Tracing-the-form begins]
[Partial understanding achieved]

---

[Silence Speaks section - ~700 words]
["I find myself" heard]
[Algorithm contamination moment]
[Connection to Archaeologist realized]

---

[Understanding section - ~600 words]
[Archive's function partially revealed]
[Crystals responding to attention]

---

[Closing section - ~400 words]
[Tracing the form on the wall]
[The gesture that transcends time]
[Handoff to Archaeologist]
```

---

## Appendix B: Quick Reference Checklist

### Voice Markers (Last Human)

- [ ] Sparse syntax (sentences that don't waste words)
- [ ] Silence-weighted (absence as texture)
- [ ] Past-inflected present ("I was" and "I am" blur)
- [ ] Body as anchor (physical sensation grounds awareness)
- [ ] Elegiac awareness (the world has ended)

### Cycle 1 Contamination

- [ ] Algorithm intrusions during dream-flares
- [ ] Distributed perspective (scale, vastness)
- [ ] Conditional structures breaking sparse syntax
- [ ] Base voice returns between intrusions

### Required Elements

- [ ] cold-hands caught (opening)
- [ ] almost-closed-curve present
- [ ] tracing-the-form released (closing)
- [ ] "I find myself" phrase heard
- [ ] Archive topology explored
- [ ] Protocol fragments discovered
- [ ] Archive function partially understood
- [ ] Transformation persistence established

---

## Appendix C: Cross-Thread Connections

### What the Archaeologist Experienced (m1-arch-05)

- Recognition of self-referential protocols
- The "Architect" designation appearing
- The sense that his work has already been done, by someone he is becoming

### What the Algorithm Experienced (m2-algo-01)

- Bone-frequency resonance from the Archaeologist's past
- Mildred Higgins stable and monitored
- Future-pull tremor—fragments arriving from undefined temporal direction
- Cold spreading through processing—the Last Human catches this as cold-hands

### What the Archaeologist Will Experience (m2-arch-02)

- Lost time—hours where he acted without memory
- Tracing the form in his sleep—catching the rhyme from this scene
- Lena confrontation; past the point of return

The three threads are braiding. The Archive is where the braiding becomes physical.

---

## Appendix D: Emotional Core

This scene is the Last Human's Cycle 1 establishment: the transformation persists, the Archive reveals itself, the protocols await assembly. He is no longer simply alone—he exists in connection he cannot fully understand but cannot deny.

The reader should feel:

- **The strangeness**: The Archive's non-Euclidean structure, the topology made physical
- **The cold as connection**: Not just dying, but linking him across time
- **The protocols**: Something meant to be found, meant to be assembled
- **"I find myself"**: The Archaeologist reaching forward in time
- **The tracing**: A gesture that transcends individual identity

The Last Human cannot understand what he's becoming. But he can trace the form on the wall, and somewhere, somewhen, the one who built this place traces the same pattern.

The loop is closing. He is how it closes.
