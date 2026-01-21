# DRAFTING CONTEXT FOR: m1-lh-02

## Scene Metadata

- **Scene ID**: m1-lh-02
- **Thread**: last_human
- **Movement**: one
- **Target Word Count**: 2500
- **Scene Title**: Survival
- **Scene Notes**: How he survives, his knowledge of history. Deepen the daily existence, reveal what he knows about the world that was.

### Narrative Position

- **Preceding Scene**: m1-lh-01 "Solitude". Established the ruined world, absolute isolation, the Last Human's journey toward "the Archive" three days east. First dream intrusion (server room, hands in light, the woman who spoke). Drew the spiral shape in dust upon waking. Rhymes used: blue-white-light, almost-closed-curve.
- **Following Scene**: m1-lh-03 "The Pull" (Journey begins in earnest, drawn toward ruins, phantasm-first-encounter).
- **Rhyming Moments Required**: None specified—save the major phantasm encounter for scene 03.

---

## Voice Reference

### Core Voice Parameters

- **Tense**: Past-inflected present (present events described as if already historical)
- **Mode**: Elegiac, sparse, weighted with absence
- **Syntax**: Short sentences. Fragments. The occasional longer passage like a held breath.
- **Concerns**: Survival, memory, meaning, legacy
- **Texture**: Silence, ruins, the absence of others, the presence of ghosts

### Forbidden Patterns (MUST AVOID)

- ❌ Present-tense active work descriptions (Archaeologist contamination)
- ❌ Economic stakes or client concerns (Archaeologist contamination)
- ❌ Technology working normally (Archaeologist contamination)
- ❌ Other people as active presences (Archaeologist contamination)
- ❌ Dense, unbroken paragraphs (Archaeologist contamination)
- ❌ Self-referential processing language (Algorithm contamination)
- ❌ Nested conditional clauses (Algorithm contamination)
- ❌ Probabilistic percentages or calculations (Algorithm contamination)
- ❌ Parallel syntactic structures (Algorithm contamination)
- ❌ Analytical framing of emotion (Algorithm contamination)

---

## Rhyme Injection

### Movement Intensity

Movement One: Single occurrence per thread—establishing vocabulary. Subtle, dismissable.

### Available Rhymes (Recommended)

- **cold-hands** (somatic): Already established in scene 01 ("My hands stopped being warm weeks ago")—can echo/develop
- **ozone-wet-stone** (olfactory): Already appeared in scene 01 ("it smells of ozone and wet stone")—can develop
- **metallic-taste** (somatic): The water "tastes like survival"—could manifest as the metallic taste of radiation, exhaustion
- **held-breath** (kinesthetic): The pause before significant thresholds

### Integration Examples

> The air tastes wrong. Metal on the tongue. I've learned this taste means radiation, means take shelter, means another hour of life traded for knowing what to avoid.

> My hands. I look at them sometimes. They were warm once. I remember warm. The cold started in the fingertips and spread. It hasn't stopped spreading. I wonder how much of me will be cold before I reach the Archive.

---

## Genre Pressure

### Thread Genre Register

**Dying Earth / New Weird**

- A world that has moved on from biology.
- The environment is a **hostile character**. Nature reclaimed the ruins—but it's crystalline, fungal, silicon-based. Not green.
- The Last Human is an **invasive species** in a world that cured itself of us.

### Markers to Include (2-3 for Movement One)

- **Alien ecology**: Nature that isn't natural—crystalline growths, silicon plants, fungal processors
- **Hostile environment**: The world actively resists—radiation, atmospheric poison, predatory architecture
- **Human as invasive**: He doesn't belong—everything adapted away from biology
- **Temporal ruins**: Architecture from incomprehensible ages
- **Silence as presence**: The weight of no one else—silence that has density

---

## Philosophy Constraints

### The Four Shackles (MUST AVOID)

1. **Identity**: Do not describe the three protagonists as "the same person."
2. **Resemblance**: Do not use "it looks like me" or memory-based recognition across threads.
3. **Opposition**: Do not frame their differences as simple binaries.
4. **Analogy**: Do not reduce recognition to "metaphor" or "symbol."

### Key Concepts to Dramatize

- **Eternal Return**: The Last Human walking a path that was always his path—survival as a form of return rather than progress
- **Intensity**: Knowledge arriving through the body, not logic. He *knows* things in his bones, his chest, his frequency-sense.
- **Pharmakon**: Survival is both what keeps him alive and what keeps him alone. The skills that preserve him are the same skills that mark him as the last.

---

## Continuity from Scene 01

### Elements to Reference/Develop

- **The Archive**: Three days east, pulled toward it by dreams. What does he know about it? What does he hope to find?
- **The dream**: The server room, the hands in light, the woman who spoke ("You're freezing"). Does he dream again? Does he resist dreaming?
- **The spiral shape**: Drew it in the dust. Has he always drawn it? Does he find it in the ruins he passes?
- **The violet crystalline plants**: Established as the new ecology. What else has changed?
- **Cold hands**: His hands haven't been warm for weeks. The cold is spreading.
- **The silence**: Has texture, weight, presses against the ears like deep water

### New Elements to Introduce

- **How he survives**: What are his daily routines, his knowledge, his skills?
- **What he knows of history**: How much does he understand about what happened? About the Integration? About the Archive?
- **The source of his knowledge**: He knows things he shouldn't. Where does this knowledge come from?
- **His relationship with time**: Days blur, numbers lose meaning, but the pull toward the Archive is constant

---

## Drafting Instructions

1. **Write to ~2500 words**.
2. **Open** with survival—the daily texture of staying alive in a hostile world. Let us feel the weight of solitude, the rhythm of endurance.
3. **Show** the elegiac voice: fragments, short sentences, past-inflected present. The prose should feel weathered, spare, like the landscape.
4. **Develop** his knowledge—what he understands about the old world, the Archive, his own impossible knowing. He should reveal knowledge without fully explaining how he has it.
5. **Deepen** the hostile ecology: the world has adapted away from humans. Silicon, crystal, fungal. Nature is not green here.
6. **End** with forward momentum—the Archive is closer. The pull is stronger. Something is waiting, and he is walking toward it.

---

## Workflow Reminders

Per `protocols/drafting-workflow.md`:

1. **Draft** to target word count (±10%)
2. **Run validation scripts** in order:
   ```bash
   python scripts/voice_validator.py drafts/movement-one/last-human/scenes/scene-02.md --thread last_human
   python scripts/philosophy_checker.py drafts/movement-one/last-human/scenes/scene-02.md
   python scripts/rhyme_tracker.py drafts/movement-one/last-human/scenes/scene-02.md --movement one
   python scripts/genre_checker.py drafts/movement-one/last-human/scenes/scene-02.md --thread last_human --movement one
   ```
3. **Iterate** if any validation fails
4. **Create** a `scene-02.context.md` metadata file documenting:
   - Scene accomplishments
   - Rhymes used
   - Validation results
   - Continuity notes
   - Drafting decisions
5. **Update** `drafts/manifest.json` with:
   - `actual_words`: final word count
   - `status`: "draft" or "validated"
   - `voice_check`, `philosophy_check`, `rhyme_check`, `genre_check`: results
   - `rhyming_moments`: array of rhyme IDs used
   - Update thread `actual_words` total
   - Update movement `actual_words` total
