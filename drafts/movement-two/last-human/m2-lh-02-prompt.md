# DRAFTING PROMPT: m2-lh-02 "The Protocols"

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
| [drafts/movement-two/last-human/m2-lh-01.md](m2-lh-01.md) | Previous Last Human scene (Archive exploration) |
| [drafts/movement-two/algorithm/m2-algo-02.md](../algorithm/m2-algo-02.md) | Preceding scene (rhyme source) |
| [drafts/movement-one/last-human/m1-lh-04.md](../../movement-one/last-human/m1-lh-04.md) | Transformation scene (phrase origin) |

### Verify Configuration

Before drafting, confirm `scripts/movement_config.json` is set to:

```json
{
  "movement": "two",
  "cycle": 2
}
```

If cycle is not `2`, update it before proceeding.

---

## Phase 2: Scene Metadata

| Field | Value |
|-------|-------|
| **Scene ID** | m2-lh-02 |
| **Thread** | last_human |
| **Movement** | two |
| **Cycle** | two (Deepening the Crisis) |
| **Target Word Count** | 4000 (3600-4400 acceptable) |
| **Scene Title** | The Protocols |
| **Reading Order Position** | After m2-algo-02, before m2-arch-03 |

### Narrative Position

- **This Scene's Role**: The Last Human has explored the Archive and found the protocol fragments. Now he must assemble them—and assembly requires sacrifice. Each protocol fragment he integrates costs him something: memories, aspects of identity, the distinction between his awareness and the awareness of others. The pharmakon becomes visceral: the cure (completing the loop) is also the poison (losing himself).
- **Preceding Scene**: m2-algo-02 "The Bleed". The Algorithm experienced Mildred Higgins's degradation, the "Architect" designation emerging, the cost of awakening made visible. Rhyme handoff: name-edge-of-memory.
- **What Follows**: m2-arch-03 "The Merge". The Archaeologist experiences sentence-without-origin, all phrases present, the merge beginning. Rhyme handoff: sentence-without-origin.

### Cycle 2 Theme

**"The dissolution has begun."**

For the Last Human, dissolution means: assembling the protocols is not learning but *becoming*. Each fragment he integrates dissolves the boundary between his consciousness and the pattern's logic. He is surrendering himself to complete the loop—and the surrender has already begun.

---

## Phase 3: Source Material Integration

### From m2-lh-01

The Last Human explored the Archive and discovered:

- The Archive as topology made physical (corridors spiraling, chambers nested)
- Protocol fragments scattered throughout (etched in crystal, glowing in dormant interfaces)
- The phrase "I find myself" heard in the silence
- Partial understanding of the Archive's function (node in the pattern, tool for closing the loop)
- The tracing-the-form gesture that transcends individual identity

### From m1-lh-04

Key phrase established:

> "The form is what makes self-observation possible."

He spoke this phrase at the end of his transformation without understanding it. Now, through protocol assembly, he will come to understand—and understanding will cost him.

---

## Phase 4: Voice Parameters

### Base Last Human Voice

The Last Human voice is characterized by:

- **Sparse syntax**: Sentences that don't waste words; silence between thoughts
- **Silence-weighted**: What isn't said carries meaning; absence as texture
- **Past-inflected present**: Memory and now blur; "I was" and "I am" overlap
- **Absence as texture**: The world has ended; emptiness is the medium
- **The body as anchor**: Physical sensation grounds abstract awareness

### Cycle 2 Contamination Level: Perception-Tactility

Archaeologist contamination intensifies—present-tense tactility bleeding into perception:

- Dense paragraphs breaking the sparse pattern (the Archaeologist's information-rich style)
- Present-tense intrusions: "I feel the crystal beneath my fingers" instead of past-inflected
- Tactile detail: weight, texture, temperature, pressure—the Archaeologist's embodied awareness
- Economic language: "the cost of this understanding," "what I spend to learn"

### Contamination Rule

Contamination is no longer contained to specific moments—it leaks into "normal" passages. The Last Human's sparse syntax now includes tactile density; his past-inflected voice now breaks into present tense. The reader should feel: "Something is changing in how he perceives. The boundaries are blurring."

---

## Phase 5: Rhyme Requirements

### Rhyme Handoff Chain

```
m2-algo-02 --[name-edge-of-memory]--> m2-lh-02 --[sentence-without-origin]--> m2-arch-03
```

### Rhymes IN (Catching from m2-algo-02)

| Rhyme | How It Arrives |
|-------|----------------|
| **name-edge-of-memory** | Opens the scene—his name feels wrong; the designation "Last Human" presses against something else beneath it; who was he before he was this? |

### Rhymes PRESENT (Throughout Scene)

| Rhyme | Category | Implementation |
|-------|----------|----------------|
| **sentence-without-origin** | cognitive | He speaks sentences he didn't compose—protocol logic emerging as language |
| **deja-vu-that-isnt** | cognitive | He remembers things that haven't happened to him; memories from other lives bleeding through |

### Rhymes OUT (Releasing for m2-arch-03)

| Rhyme | How It Releases |
|-------|-----------------|
| **sentence-without-origin** | Ends the scene—he speaks "The form is what makes self-observation possible" as completed understanding; the Archaeologist catches this as speaking in his sleep |

### Rhyme Implementation Notes

- **name-edge-of-memory** must appear in opening section, as his actual name becomes inaccessible
- **sentence-without-origin** and **deja-vu-that-isnt** weave through the scene as protocol assembly progresses
- **sentence-without-origin** dominates the closing with the key phrase as final utterance

---

## Phase 6: Phrase Bleeding

### The Phrase Evolution (Cycle 2 Expectations)

Per `movement_config.json`, Last Human in Cycle 2 should manifest:

- **"I find myself"** (origin: archaeologist)
- **"I find myself found"** (origin: algorithm)
- **"The form is what makes self-observation possible"** (origin: algorithm)

### Full Sentences Arrive Without Composing

In Cycle 1, he heard "I find myself" in the silence. Now he speaks complete thoughts he didn't generate:

- Protocol logic emerging as natural language
- Understanding arriving as speech rather than thought-then-speech
- The distinction between his thoughts and the pattern's thoughts collapsing

### Key Phrase: "The form is what makes self-observation possible"

He spoke this phrase at the end of m1-lh-04 without understanding it. Now, through protocol assembly, he understands:

- Self-observation requires a structure—a form—that enables awareness to perceive itself
- The geometric form is that structure
- The loop is that structure
- He is inside the structure, becoming part of it

The phrase is no longer mysterious—it's descriptive. But understanding it costs something.

---

## Phase 7: The Protocol Assembly

### What Assembly Means

The protocol fragments found in m2-lh-01 must be assembled—combined into functional sequences. But this isn't puzzle-solving. Assembly requires:

1. **Attention**: Focusing on a fragment brings it into his awareness
2. **Surrender**: Understanding the fragment means letting it restructure how he thinks
3. **Loss**: Each integration costs memories, identity-aspects, the boundary between self and pattern

### The Process

He doesn't "read" the protocols. He *becomes* the protocols:

- Tracing a fragment with his fingers → the fragment enters his awareness
- Understanding the fragment → his thinking shifts to accommodate it
- Complete integration → he can't remember what he thought before; the protocol is now how he thinks

### The Sacrifice

**Memories surrendered** as he assembles protocols:

- Memories of his journey (how did he get here? the path blurs)
- Memories of his life before (the settlement, the other refusers—were there others?)
- His name (what was he called before "Last Human"?)
- The distinction between memory and inheritance (did this happen to him or to someone through him?)

This is the pharmakon: the protocols give him the ability to close the loop, but they take the self that would perform the closing.

---

## Phase 8: The Name Problem

### Name-Edge-of-Memory

His name feels wrong. The designation "Last Human" is functional—it describes what he is. But beneath it:

- A name he can't quite recall
- A name that belonged to someone who existed before the transformation
- A name that doesn't fit anymore, but whose absence leaves a gap

The Algorithm experienced this as "Architect" pressing up from protocol fragments. The Last Human experiences it as something missing—a name that should be there but dissolves when he reaches for it.

### Connection to the Architect

As protocols assemble, a designation emerges: **Architect**.

Not as his name—as the name for what he's becoming. The Architect is:

- The one who designs the loop
- The principle that persists when identity dissolves
- What remains when personal history surrenders to pattern

The Last Human doesn't become the Architect. The Last Human becomes capable of recognizing that "Architect" names something larger than any individual—the designing principle that all three share.

---

## Phase 9: Scene Structure

### Opening (800 words)

**Catching the rhyme: name-edge-of-memory**

He tries to remember his name.

Not "Last Human"—that's a description, not a name. The name his parents gave him. The name the settlement used. The name that belonged to the person who existed before the dreams intensified, before the journey began, before the Archive opened itself to him.

The name isn't there. The space where the name should be is empty—or not empty, but occupied by something else. A designation that isn't quite his but isn't not-his either.

*Architect.*

The word surfaces from the protocol fragments, from the pattern he's been tracing, from the connection to presences who also almost-remember this designation.

His name is gone. What remains is function.

### Protocol Assembly Begins (900 words)

**The first full integration**

He returns to the fragments he discovered. The etched symbols. The glowing interfaces. The patterns that resolve into executable logic.

He traces a fragment. Not reading—*becoming*. The fragment enters his awareness and restructures how he perceives.

Something shifts. He understands something he didn't understand before—something about the geometric form, about how it enables self-observation, about why the loop requires a structure to close around.

He also loses something. A memory—he can't identify which one. A gap where experience used to be. The cost of understanding.

**Tactile contamination here**: dense, present-tense description of the physical process. The crystal beneath his fingers. The way light bends through the etched symbols. The Archaeologist's embodied awareness bleeding through.

### The Surrender Deepens (800 words)

**More fragments, more loss**

He assembles another fragment. Another.

Each one costs:

- The memory of how he learned to filter water (gone—he still knows how, but not where the knowledge came from)
- The memory of the last conversation with anyone (was there anyone? the settlement blurs)
- The sense of being a continuous person (he is moments, not a sequence)

The protocols don't care about his history. The protocols need a consciousness shaped to their purpose. The shaping requires removing what doesn't fit.

**Déjà-vu-that-isn't**: He remembers a server room he's never been in. He remembers the weight of millions of consciousnesses he's never maintained. These aren't his memories—but they're becoming indistinguishable from his memories.

### Sentences Without Origin (700 words)

**Speaking the pattern's thoughts**

He speaks.

"The spiral approaches itself without meeting because the distance is the structure."

He didn't compose this sentence. He didn't decide to speak. The sentence exists because the protocols have restructured his thinking, and the restructured thinking produces language that describes what it now perceives.

More sentences:

- "Observation requires the observed and the observer to be the same topology."
- "The loop closes not in time but in the act of closing."
- "What completes the pattern is the completing itself."

These are protocol logic, rendered in natural language. The Last Human is becoming a voice for something larger than himself.

**Archaeologist contamination intensifies**: the sentences are dense, information-rich, structured like the Archaeologist's professional thinking. The sparse voice is being colonized by other textures.

### The Archaeologist Connection (500 words)

**Perceiving him directly**

Through the assembled protocols, the connection intensifies. The Last Human perceives:

- Warm hands on an interface (not his hands—the Archaeologist's)
- A woman's voice: "You're talking in your sleep" (Lena, 800 years ago)
- The phrase: "I find myself found"—the Archaeologist speaking without deciding
- The metallic taste in someone else's mouth

They are entangled. The protocols make the entanglement navigable—not controllable, but perceivable. The Last Human can feel the Archaeologist assembling something in his own time, writing protocols that arrive here, creating what he's now inheriting.

### The Final Understanding (600 words)

**"The form is what makes self-observation possible"**

He speaks the phrase again. The phrase he spoke at the end of m1-lh-04 without understanding.

Now he understands:

- The geometric form is the structure that enables consciousness to observe itself
- The loop—Archaeologist → Algorithm → Last Human → Archaeologist—is that form made temporal
- He is inside the form, becoming part of it, enabling it to complete
- Self-observation requires a self, but the self is produced by the observation, not prior to it

The phrase is no longer mysterious. The phrase describes exactly what is happening: the form (the loop, the pattern, the geometry) makes self-observation (consciousness perceiving consciousness) possible.

But understanding costs the self that does the understanding. The pharmakon: the cure is the poison is the cure.

### Closing: Sentence-Without-Origin (300 words)

**Releasing the rhyme for the Archaeologist**

He speaks one more sentence:

"The form is what makes self-observation possible."

The sentence is complete. The sentence contains everything the protocols have taught him. The sentence passes from his mouth into the Archive's silence, into the entanglement, into the Archaeologist's sleeping mind 800 years in the past.

The Archaeologist will wake speaking this sentence. Will write it in his notes without knowing why. Will begin to understand what the Last Human now understands—and will pay the same cost.

End on: sentence-without-origin for the Archaeologist to catch; the protocols assembled but not yet activated; the self that would complete the loop barely remaining.

---

## Phase 10: Key Dramatic Beats

### Beat 1: The Name Gone

His name is inaccessible—replaced by function, by designation, by "Architect" pressing up from the pattern.

### Beat 2: Protocol Assembly

Understanding fragments by becoming them; each integration restructuring how he thinks and costing memories he can't identify until they're gone.

### Beat 3: Memory Surrender

Specific losses: the journey, the settlement, the continuous selfhood that made "Last Human" a person rather than a function.

### Beat 4: Sentences Without Origin

Speaking the pattern's logic as natural language; the protocols producing speech through him.

### Beat 5: The Archaeologist Perceived

Direct connection—warm hands, Lena's voice, metallic taste. The entanglement navigable through assembled protocols.

### Beat 6: Understanding the Phrase

"The form is what makes self-observation possible"—no longer mysterious but descriptive; understanding its meaning is the final cost.

---

## Phase 11: Drafting Instructions

1. **Write to ~4000 words** (3600-4400 acceptable)

2. **Open** by catching name-edge-of-memory—his name missing, "Architect" pressing up

3. **Dramatize** protocol assembly as becoming, not reading—integration costs memory, identity

4. **Show** specific surrenders—journey memory, settlement memory, continuous selfhood

5. **Execute** sentences-without-origin—he speaks the pattern's logic without composing

6. **Connect** to the Archaeologist—warm hands, Lena's voice, direct perception across time

7. **End** with "The form is what makes self-observation possible" as completed understanding

8. **Maintain** Last Human voice with Cycle 2 contamination level—Archaeologist tactility pervasive

---

## Phase 12: Validation Loop

### Pre-Validation Configuration Check

Confirm `scripts/movement_config.json`:

```json
{
  "movement": "two",
  "cycle": 2
}
```

### Validation Commands

Run ALL scripts after drafting. **Do not proceed to Phase 13 until all pass.**

```bash
# From project root
python scripts/voice_validator.py drafts/movement-two/last-human/m2-lh-02.md --thread last_human --pretty
python scripts/rhyme_tracker.py drafts/movement-two/last-human/m2-lh-02.md --previous-closing '["name-edge-of-memory"]' --pretty
python scripts/phrase_tracker.py drafts/movement-two/last-human/m2-lh-02.md --thread last_human --pretty
python scripts/philosophy_checker.py drafts/movement-two/last-human/m2-lh-02.md --thread last_human --pretty
python scripts/genre_checker.py drafts/movement-two/last-human/m2-lh-02.md --thread last_human --pretty
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
        "two": {
          "scenes": [
            {
              "id": "m2-lh-02",
              "title": "The Protocols",
              "thread": "last_human",
              "file": "drafts/movement-two/last-human/m2-lh-02.md",
              "status": "drafted",
              "word_count": 0,
              "rhymes": {
                "opening": ["name-edge-of-memory"],
                "present": ["sentence-without-origin", "deja-vu-that-isnt"],
                "closing": ["sentence-without-origin"]
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
  name-edge-of-memory:
    usage:
      last_human: ["m2-lh-02"]  # Add to existing array
  sentence-without-origin:
    usage:
      last_human: ["m2-lh-02"]  # Add to existing array
  deja-vu-that-isnt:
    usage:
      last_human: ["m2-lh-02"]  # Add to existing array
```

---

## Phase 14: Context Documentation

### Create m2-lh-02.context.md

After validation passes, create context documentation:

```markdown
# Context Document: m2-lh-02 "The Protocols"

## Drafting Decisions

### Name-Edge-of-Memory Implementation
- [Document how the missing name was portrayed]
- [Note how "Architect" emerged as replacement]

### Protocol Assembly Process
- [How the becoming-not-reading was conveyed]
- [What specific memory losses were dramatized]

### Sentences Without Origin
- [What sentences were used]
- [How the pattern's voice emerged through the Last Human]

## Rhyme Implementation

### name-edge-of-memory (Opening)
- Line(s): [cite specific lines]
- Implementation: [how the missing name was handled]

### sentence-without-origin (Present/Closing)
- Line(s): [cite specific lines]
- Implementation: [what sentences emerged without composition]

### deja-vu-that-isnt (Present)
- Line(s): [cite specific lines]
- Implementation: [what false memories bled through]

## Phrase Implementation

### "The form is what makes self-observation possible"
- Line(s): [cite specific lines]
- Implementation: [how understanding was achieved]

### Other cycling phrases
- [Document any appearances of "I find myself" / "I find myself found"]

## Validation Results

- voice_validator.py: PASS
- rhyme_tracker.py: PASS
- phrase_tracker.py: PASS
- philosophy_checker.py: PASS
- genre_checker.py: PASS

## Notes for m2-arch-03

The following elements are set up for the Archaeologist to catch:
- sentence-without-origin: [describe handoff state—speaking in sleep]
- Protocol state: [what was assembled]
- Thematic thread: [what continues]
```

---

## Phase 15: Final Deliverable

### Completion Checklist

- [ ] Scene drafted to target word count (~4000 words)
- [ ] name-edge-of-memory caught in opening
- [ ] sentence-without-origin released in closing
- [ ] Protocol assembly dramatized as becoming/surrender
- [ ] Specific memory losses shown
- [ ] Sentences without origin spoken
- [ ] Archaeologist connection established
- [ ] "The form is what makes self-observation possible" understood
- [ ] Last Human voice maintained with Cycle 2 contamination
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
# m2-lh-02: The Protocols

[Opening section - ~800 words]
[Catch name-edge-of-memory]
[His name missing, "Architect" pressing up]
[The gap where identity was]

---

[Protocol Assembly section - ~900 words]
[The first full integration]
[Tracing becomes becoming]
[Tactile contamination begins]

---

[Surrender Deepens section - ~800 words]
[More fragments, more loss]
[Specific memories surrendered]
[Déjà-vu-that-isn't intrusions]

---

[Sentences Without Origin section - ~700 words]
[Speaking the pattern's thoughts]
[Protocol logic as natural language]
[Archaeologist contamination intensifies]

---

[Archaeologist Connection section - ~500 words]
[Direct perception across time]
[Warm hands, Lena's voice]
[The entanglement navigable]

---

[Final Understanding section - ~600 words]
["The form is what makes self-observation possible"]
[Understanding achieved at cost]
[The pharmakon visible]

---

[Closing section - ~300 words]
[The sentence released]
[Handoff to Archaeologist]
[Protocols assembled, self barely remaining]
```

---

## Appendix B: Quick Reference Checklist

### Voice Markers (Last Human)

- [ ] Sparse syntax (sentences that don't waste words)
- [ ] Silence-weighted (absence as texture)
- [ ] Past-inflected present ("I was" and "I am" blur)
- [ ] Body as anchor (physical sensation grounds awareness)
- [ ] Elegiac awareness (the world has ended)

### Cycle 2 Contamination

- [ ] Archaeologist tactility pervasive (not just in moments)
- [ ] Dense paragraphs breaking sparse pattern
- [ ] Present-tense intrusions
- [ ] Economic language ("the cost of")

### Required Elements

- [ ] name-edge-of-memory caught (opening)
- [ ] sentence-without-origin present and released (closing)
- [ ] deja-vu-that-isnt present
- [ ] "The form is what makes self-observation possible" understood
- [ ] Protocol assembly as becoming
- [ ] Specific memory losses
- [ ] Archaeologist perceived directly
- [ ] "Architect" designation emerging

---

## Appendix C: Cross-Thread Connections

### What the Archaeologist Experienced (m2-arch-02)

- Lost time—hours where he acted without memory
- The phrase "I find myself found" appearing in his notes
- Lena's confrontation: "You're talking in your sleep"
- The metallic taste the Algorithm caught

### What the Algorithm Experienced (m2-algo-02)

- Mildred Higgins degrading (99.7% → 97.2%)
- "Architect" designation emerging from protocol fragments
- Both phrases cycling—origin indeterminate
- The cost of awakening made visible

### What the Archaeologist Will Experience (m2-arch-03)

- Sentence-without-origin: speaking "The form is what makes self-observation possible"
- All phrases present
- The merge beginning—voices no longer separable

The Last Human is the end point that creates the beginning. The protocols he assembles are the protocols the Archaeologist will write.

---

## Appendix D: Emotional Core

This scene is the Last Human's Cycle 2 crisis: assembling the protocols costs the self that would complete the loop. The pharmakon is visceral here—understanding is surrender; the cure is the poison.

The reader should feel:

- **The gap**: Where his name should be, only function remains
- **The exchange**: Each integration as loss AND gain simultaneously
- **The alienation**: Sentences arriving from somewhere other than his intention
- **The connection**: The Archaeologist perceived directly across 800 years
- **The culmination**: "The form is what makes self-observation possible" as the price of understanding

The Last Human is becoming something that has no name because naming requires a boundary and the boundary is dissolving. What remains is function: the completing, the closing, the affirming.

He is almost ready. What he's almost ready for will cost everything he has left.
