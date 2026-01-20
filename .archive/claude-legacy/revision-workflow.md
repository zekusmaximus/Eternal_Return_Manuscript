# Revision Workflow

## Overview

This document defines the multi-pass revision system for *The Eternal Return of the Digital Self*. Each scene progresses through defined stages with specific checks at each level.

---

## Status Progression

```
not_started → draft → voice_pass → philosophy_pass → revised → polished → final
```

| Status | Criteria | Who Reviews |
|--------|----------|-------------|
| `not_started` | No content exists | — |
| `draft` | First complete draft exists | Self |
| `voice_pass` | Voice consistency verified | Claude + Self |
| `philosophy_pass` | Philosophical alignment verified | Claude + Self |
| `revised` | Structural/content revisions complete | Self |
| `polished` | Line-level prose editing complete | Self |
| `final` | Ready for final manuscript | Self |

---

## Pass 1: Draft Completion

### Purpose
Get content on the page. Prioritize completion over perfection.

### Process
1. Load voice file for target thread (`voices/[thread].md`)
2. Check scene's position in manifest for context
3. Reference relevant sections of `brainstorm1.md`
4. Write to target word count (±10%)
5. Don't self-edit during drafting

### Output
- Scene file with `status: draft`
- Actual word count recorded in manifest

### Commands
```
/draft [thread] [scene-description]
```

---

## Pass 2: Voice Consistency Check

### Purpose
Verify the thread is immediately identifiable by prose style alone, without labels.

### Checklist

#### Archaeologist Thread
- [ ] Tense: Present throughout (no drift to past)
- [ ] Syntax: Concrete, specific, active verbs
- [ ] Texture: Physical world details present (hardware, smells, weight)
- [ ] Concerns: Economic, relational, bodily stakes evident
- [ ] No nested clauses (Algorithm contamination)
- [ ] No fragments (Last Human contamination)

#### Algorithm Thread
- [ ] Tense: Shifts appropriately (present for processing, past for memories, conditional for projections)
- [ ] Syntax: Nested clauses, if-then structures, parallel constructions
- [ ] Texture: Data topology, maintenance rhythms present
- [ ] Concerns: Optimization, integrity, emergence
- [ ] No grounded tactile details (Archaeologist contamination)
- [ ] No elegiac sparseness (Last Human contamination)

#### Last Human Thread
- [ ] Tense: Past-inflected present maintained
- [ ] Syntax: Short sentences, fragments, occasional long passages
- [ ] Texture: Silence, ruins, absence weighted
- [ ] Concerns: Survival, memory, meaning, legacy
- [ ] No economic concerns (Archaeologist contamination)
- [ ] No recursive self-questioning (Algorithm contamination)

### Process
1. Read scene aloud (or use text-to-speech)
2. Mark any sentence where voice drifts
3. Rewrite flagged sentences in correct register
4. Re-read until no drift detected

### Commands
```
/voice-check [thread] [file-or-text]
```

### Output
- Scene file with `voice_check: passed`
- Status updated to `voice_pass`

---

## Pass 3: Philosophical Alignment Check

### Purpose
Verify content embodies the novel's Deleuzian/Klossowskian framework rather than betraying it.

### The Four Shackles (MUST AVOID)

| Shackle | Violation Example | Correction |
|---------|-------------------|------------|
| **Identity** | "He recognized himself in the Algorithm" | Recognition through intensity/tonality, not sameness |
| **Opposition** | "Unlike the AI, he was still human" | Difference is productive, not binary |
| **Analogy** | "The Algorithm functioned like a human mind" | Each is genuinely different, not functionally similar |
| **Resemblance** | "Something about the pattern reminded him of his own thoughts" | Connection through structural intensity, not similarity |

### Core Checks

- [ ] No identity language between the three characters
- [ ] Recognition works through intensity/tonality, not memory/resemblance
- [ ] Technical substrate present as material condition
- [ ] Affirmation is active willing, not passive acceptance
- [ ] Augenblick is rupture of time, not point in time
- [ ] Pharmakon double nature visible (poison and cure)
- [ ] Reactive forces being eliminated by selective principle
- [ ] No transmission metaphors for temporal mechanism

### Process
1. Highlight all passages involving:
   - Recognition between threads
   - Character self-understanding
   - The protocols / temporal mechanism
   - Choices or affirmations
2. Check each against relevant framework section in `research/Framework`
3. Rewrite violations to embody rather than describe philosophy

### Commands
```
/philosophy-check [file-or-text]
/concept-dramatize [concept] — if section feels abstract
```

### Output
- Scene file with `philosophy_check: passed`
- Status updated to `philosophy_pass`

---

## Pass 4: Structural Revision

### Purpose
Address content, pacing, and structure issues that emerged during drafting.

### Checklist

- [ ] Scene achieves its narrative function (per manifest notes)
- [ ] Word count within target range
- [ ] Opening hooks reader appropriately
- [ ] Closing provides appropriate momentum/closure
- [ ] Rhyming moments connect properly to other threads
- [ ] No plot inconsistencies with adjacent scenes
- [ ] Sensory echo markers present where expected (frequency, geometric form)

### Process
1. Review scene in context of full movement outline
2. Check continuity with preceding/following scenes
3. Verify rhyming moments align with registry
4. Restructure or add/cut content as needed
5. May require significant rewriting

### Output
- Status updated to `revised`

---

## Pass 5: Line-Level Polish

### Purpose
Prose-level refinement. Sentence rhythm, word choice, precision.

### Checklist

- [ ] No clichés or dead metaphors
- [ ] Verbs are specific and active
- [ ] Sensory details are precise, not generic
- [ ] Dialogue (if present) sounds natural to character
- [ ] Paragraph rhythm varies appropriately
- [ ] No unnecessary words
- [ ] Technical terminology used correctly

### Forbidden Patterns
- Adverb overuse ("he said quietly")
- Weak verbs + adverbs instead of strong verbs
- "Began to" / "started to" when action is immediate
- Filter words ("he saw that," "she felt that")
- Repetitive sentence structures

### Process
1. Read sentence by sentence
2. Question every word: is this the right word?
3. Read aloud for rhythm
4. Cut 10% (aim for tighter prose)

### Commands
```
/line-edit [file]
```

### Output
- Status updated to `polished`

---

## Pass 6: Final Review

### Purpose
Confirm scene is ready for final manuscript.

### Checklist

- [ ] Voice check still passes after revisions
- [ ] Philosophy check still passes after revisions
- [ ] No outstanding notes or TODOs
- [ ] Word count recorded accurately
- [ ] File properly formatted per template

### Output
- Status updated to `final`

---

## Movement-Level Checks

After all scenes in a movement reach `polished` status:

### Movement One
- [ ] Each thread establishes distinct, identifiable voice
- [ ] Stakes are clear for each character
- [ ] Anomaly/mystery introduced in each thread
- [ ] Decreasing section length creates acceleration (15k → 12k → 10k)

### Movement Two
- [ ] Rotation pattern (A-B-C) maintained
- [ ] Rhyming moments create thematic resonance
- [ ] Entanglement intensifies progressively
- [ ] Section lengths consistent (3-5k each)

### Movement Three
- [ ] Phase transitions smooth (paragraph → sentence → fragment)
- [ ] Dissolution is disorienting but not confusing
- [ ] Sensory echoes anchor reader
- [ ] Augenblick trigger properly placed

### Movement Four
- [ ] Reverse order from Movement One (LH → Algo → Arch)
- [ ] Each voice transformed but still distinct
- [ ] Separation-after-unity achieved
- [ ] Mystery persists at end

---

## Continuity Check Commands

```
/continuity-check [movement]    — Verify coherence across movement
/rhyme-audit                    — Check rhyming moment consistency
/character-status [character]   — Summarize arc progression
```

---

## Workflow Commands Summary

| Stage | Command | Purpose |
|-------|---------|---------|
| Draft | `/draft [thread] [scene]` | Generate initial content |
| Voice | `/voice-check [thread] [text]` | Verify voice consistency |
| Philosophy | `/philosophy-check [text]` | Verify philosophical alignment |
| Concept | `/concept-dramatize [concept]` | Generate philosophy-embodying scene |
| Polish | `/line-edit [file]` | Prose-level refinement |
| Structure | `/continuity-check [movement]` | Cross-scene coherence |
| Rhyming | `/rhyme-audit` | Rhyming moment tracking |

---

## Recording Progress

After each pass, update:

1. **Scene file metadata**: Update status field in YAML frontmatter
2. **Manifest**: Update scene status and word counts in `drafts/manifest.json`
3. **Progress**: Add session notes to `progress.md`
