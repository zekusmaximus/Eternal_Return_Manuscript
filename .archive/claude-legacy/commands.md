# Custom Commands and Workflows

## Quick Reference Commands

These are common task patterns for working on the novel. Use them as prompts or workflow guides.

---

## Drafting Commands

### `/draft [thread] [scene-description]`

Draft a scene for a specific thread.

**Process**:
1. Load `voices/[thread].md` for voice reference
2. Check `Notes.md` for structural placement
3. Check `brainstorm1.md` for relevant details
4. Draft scene maintaining voice consistency
5. Run Writing Checks before delivering

**Example**: `/draft archaeologist discovering the first anomalous protocol`

---

### `/draft-rhyme [moment-type]`

Draft a rhyming moment that echoes across all three threads.

**Process**:
1. Identify the core experience (discovery, loss, recognition, etc.)
2. Draft three versions—one per thread—each in correct voice
3. Ensure thematic resonance without surface resemblance
4. Verify no identity/resemblance language

**Example**: `/draft-rhyme first-encounter-with-the-geometric-form`

---

### `/draft-dissolution [word-count]`

Draft a section of the Movement Three dissolution phase.

**Process**:
1. Determine phase (paragraph alternation / sentence alternation / fragment)
2. Load all three voice references
3. Draft with progressive blending per `brainstorm1.md` specifications
4. Include sensory echoes (geometric form, frequency/vibration)
5. Verify disorientation is purposeful, not confusing

---

## Voice Commands

### `/voice-check [thread] [text]`

Analyze text for voice consistency with specified thread.

**Check for**:
- Correct tense usage
- Appropriate syntax patterns
- Thread-specific concerns and textures
- Absence of cross-contamination from other voices

**Output**: Specific line-by-line feedback on voice drift

---

### `/voice-sample [thread] [situation]`

Generate a voice sample showing how a thread would handle a specific situation.

**Example**: `/voice-sample algorithm experiencing-first-memory-intrusion`

---

## Philosophical Alignment Commands

### `/philosophy-check [text]`

Analyze text against the philosophical framework.

**Check against**:
- The Four Shackles (identity, opposition, analogy, resemblance)
- Active vs. reactive force depiction
- Proper differentiation/differenciation usage
- Intensity-based rather than memory-based recognition
- Augenblick as rupture vs. point in time
- Pharmakon double nature

**Output**: Specific violations and suggested corrections

---

### `/concept-dramatize [philosophical-concept]`

Generate a scene that dramatizes a philosophical concept without exposition.

**Example**: `/concept-dramatize the-selective-principle-eliminating-reactive-forces`

---

## Structure Commands

### `/place-scene [scene-description]`

Determine where a scene belongs in the novel's structure.

**Output**:
- Movement (1-4)
- Thread (if applicable)
- Position within movement
- Preceding and following scenes
- Structural function

---

### `/spiral-map [movement]`

Generate the current spiral structure for a movement, showing:
- Scene sequence
- Word count targets
- Rhyming moment placements
- Thread rotation pattern

---

## Character Commands

### `/character-status [character]`

Summarize current development state for a character.

**Output**:
- Key relationships established
- Arc progression
- Unresolved questions
- Scenes drafted
- Voice sample status

---

### `/relationship-scene [character1] [character2] [conflict/moment]`

Draft a scene focused on a specific relationship.

**Example**: `/relationship-scene archaeologist lena confrontation-about-obsession`

---

## Protocol Commands

### `/protocol-fragment [era] [layer]`

Generate a fragment of the protocols as they appear in a specific era.

**Eras**: archaeologist, algorithm, last-human
**Layers**: optimization, structural, self-referential

**Example**: `/protocol-fragment archaeologist self-referential`

---

### `/protocol-evolution [specific-element]`

Show how a specific protocol element evolves across all three eras.

**Example**: `/protocol-evolution the-compression-algorithm-shortcut`

---

## Review Commands

### `/critique [file-or-text]`

Provide direct, unsparing critique of draft content.

**Evaluate**:
- Voice consistency
- Philosophical alignment
- Structural fit
- Dramatic effectiveness
- Prose quality

**Output**: Specific issues with actionable corrections

---

### `/writing-checks [text]`

Run the full Writing Checks checklist from CLAUDE.md against text.

**Output**: Pass/fail for each check with specific examples

---

## Research Commands

### `/concept-lookup [term]`

Quick reference for a philosophical term.

**Sources**: `research/research.md` terminology tables

**Output**: Definition, source philosopher, narrative application

---

### `/quote-find [concept]`

Find relevant quotations for a concept (for potential epigraphs or reference).

**Example**: `/quote-find affirmation-despite-dissolution`

---

## Worldbuilding Commands

### `/worldbuild [era] [aspect]`

Develop a specific aspect of worldbuilding for an era.

**Aspects**: technology, society, environment, economy, daily-life

**Example**: `/worldbuild near-future integration-industry-economics`

---

### `/sensory-palette [era]`

Generate the sensory details characteristic of an era.

**Output**: Sights, sounds, smells, textures, tastes specific to that time period

---

## Workflow: Starting a Writing Session

1. Check `Notes.md` for current development priorities
2. Review relevant voice file if drafting
3. Check `brainstorm1.md` for mechanism/character details needed
4. Draft with voice consistency as primary concern
5. Run `/philosophy-check` on completed draft
6. Run `/writing-checks` before finalizing

---

## Workflow: Developing a New Scene

1. `/place-scene [description]` - determine structural position
2. Load relevant voice and character files
3. Identify any rhyming moments this scene should connect to
4. Draft scene
5. `/voice-check` - verify thread consistency
6. `/critique` - identify issues
7. Revise and finalize

---

## Workflow: Working on Movement Three

Movement Three requires special handling due to the dissolution technique.

1. Map current position in the three phases (paragraph/sentence/fragment)
2. Load ALL THREE voice files simultaneously
3. Draft with progressive blending
4. Check that sensory echoes (geometric form, frequency) are present
5. Read aloud to test disorientation vs. confusion
6. Verify the Augenblick trigger is properly placed

---

## Workflow: Philosophical Alignment Review

For any substantial draft section:

1. `/philosophy-check [text]`
2. Address any Four Shackles violations first
3. Verify recognition works through intensity
4. Check active/reactive force depiction
5. Ensure technical substrate is present
6. Confirm pharmakon double nature appears where relevant
7. Final read for philosophical coherence

---

## Emergency Reference

### If voice is drifting:
→ Re-read `voices/[thread].md`
→ Write a 200-word voice exercise before continuing

### If scene feels philosophically hollow:
→ Check `research/research.md` Section VI (Narrative Operationalization)
→ Identify which concept should be dramatized
→ Rewrite with specific philosophical grounding

### If structure is unclear:
→ Check `Notes.md` Movement breakdown
→ Use `/spiral-map` to visualize position
→ Identify preceding/following scenes for continuity

### If the three are starting to feel "the same":
→ STOP
→ Re-read the Four Shackles section
→ Check for resemblance/identity language
→ Rewrite emphasizing DIFFERENCE, not similarity