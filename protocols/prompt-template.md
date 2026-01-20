# Prompt Template for AI Drafting

## Usage

When an AI agent is tasked with drafting a scene, it should assemble context using this template structure. Each section should be populated from the relevant source files.

---

## Template Structure

```markdown
# DRAFTING CONTEXT FOR: [Scene ID]

## Scene Metadata
- **Scene ID**: [from manifest.json]
- **Thread**: [archaeologist/algorithm/last_human]
- **Movement**: [one/two/three/four]
- **Target Word Count**: [from manifest.json]
- **Scene Title**: [from manifest.json]
- **Scene Notes**: [from manifest.json]

### Narrative Position
- **Preceding Scene**: [title and brief summary]
- **Following Scene**: [title and brief summary, if known]
- **Rhyming Moments Required**: [from manifest.json rhyming_moments field]

---

## Voice Reference

[PASTE FULL CONTENT FROM voices/{thread}.md]

### Quick Reminders
- **Tense**: [specific for this thread]
- **Syntax**: [specific for this thread]
- **Texture**: [specific for this thread]

### Forbidden Patterns (MUST AVOID)
[List from voice file's Forbidden Patterns section]

---

## Rhyme Injection

### Movement Intensity
[Current movement's intensity level from registry]

### Required Rhymes for This Scene
[If rhyming_moments are specified in manifest, include the full rhyme entries]

### Available Rhymes
[List rhymes at appropriate intensity_peak for this movement with low usage counts]

### Integration Examples
[Include voice-specific paragraph examples from registry.md for selected rhymes]

---

## Genre Pressure

### Thread Genre Register
[From scaffolding/genre-pressure.md - this thread's genre]

### Movement-Specific Pressure
[Intensity and bleed notes for current movement]

### Markers to Include
[List of specific genre markers from genre-pressure.md]

---

## Philosophy Constraints

### The Four Shackles (MUST AVOID)
1. **Identity**: Do not describe the three as "the same person"
2. **Opposition**: Do not frame difference as binary opposition
3. **Analogy**: Do not say one "functions like" another
4. **Resemblance**: Do not use recognition through resemblance/memory

### Key Concepts for This Scene
[If scene notes mention specific concepts to dramatize]

### Writing Checks
- [ ] Voice distinct and identifiable without labels
- [ ] Recognition through intensity/tonality, not memory/resemblance
- [ ] Technical substrate present as material condition
- [ ] Affirmation as active willing, not passive acceptance
- [ ] Augenblick as rupture of time, not point in time
- [ ] Pharmakon double nature (poison/cure) if relevant
- [ ] No identity/resemblance language between the three

---

## Drafting Instructions

1. Write to target word count ±10%
2. Maintain voice consistency as primary concern
3. Include at least [N] rhymes at appropriate intensity
4. Apply genre pressure markers naturally
5. Avoid all Four Shackles
6. End with appropriate momentum/closure for scene position

BEGIN DRAFT:
```

---

## Example: Assembling Context for m1-arch-01

```markdown
# DRAFTING CONTEXT FOR: m1-arch-01

## Scene Metadata
- **Scene ID**: m1-arch-01
- **Thread**: archaeologist
- **Movement**: one
- **Target Word Count**: 3000
- **Scene Title**: Opening: Daily Excavation
- **Scene Notes**: Establish profession, economic stakes, tactile voice

### Narrative Position
- **Preceding Scene**: None (opening scene)
- **Following Scene**: m1-arch-02 "The Client: Integration Prep" - Show integration process, introduce Lena
- **Rhyming Moments Required**: None specified

---

## Voice Reference

[Full content of voices/archaeologist.md would be pasted here]

### Quick Reminders
- **Tense**: Present
- **Syntax**: Concrete, specific, active verbs
- **Texture**: Hardware, data centers, weight of objects

### Forbidden Patterns
- ❌ Nested conditional clauses
- ❌ Self-referential processing language
- ❌ Sentence fragments
- ❌ Elegiac tone

---

## Rhyme Injection

### Movement Intensity
Movement One: Single occurrence per thread - establishing vocabulary. Subtle, dismissable, possibly unnoticed by characters.

### Required Rhymes
None specifically required for this scene.

### Available Rhymes (Low Usage, Appropriate Intensity)
- `held-breath` (kinesthetic) - "Old habit—I hold my breath until I hear data moving"
- `ozone-wet-stone` (olfactory) - Server room atmosphere
- `cold-hands` (somatic) - Working late, server chill

### Integration Examples
[Archaeologist paragraph examples for these rhymes from registry.md]

---

## Genre Pressure

### Thread Genre Register
Corporate Gothic / Tech-Noir
- Clean surfaces, dirty secrets
- High-gloss interfaces hiding rot
- Digital archaeology as grave robbing

### Movement One Pressure
Full genre presence. Establish the vibe thoroughly.

### Markers to Include
- Data work described as intimate/invasive
- Economic stakes clear
- Server room as morgue-like space
- Technology as cold, clinical

---

## Philosophy Constraints

### The Four Shackles
[Standard list]

### Key Concepts for This Scene
- Tertiary retention (data as externalized memory)
- Technical substrate as material condition

### Writing Checks
[Standard checks]

---

## Drafting Instructions

1. Write to 3000 words ±10% (2700-3300)
2. Establish archaeologist voice from first sentence
3. Include 1-2 rhymes subtly (held-breath, ozone-wet-stone recommended)
4. Apply Corporate Gothic markers throughout
5. Ground the reader in economic and relational stakes

BEGIN DRAFT:
```

---

## Notes for Agents

1. **Always assemble context first** - Do not draft without loading the relevant reference files
2. **Paste full voice reference** - Don't summarize; voice contamination is the biggest risk
3. **Check rhyme usage** - Query registry.md to avoid overusing any single rhyme
4. **Update manifest after drafting** - Record actual word count and check statuses
