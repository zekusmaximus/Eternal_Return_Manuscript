# Context: Movement Three Phase B — Simultaneous Narration

> **Prose file**: `phase-b-simultaneous-narration.md`
> **Phase ID**: m3-phase-b
> **Status**: Prompt Ready
> **Prompt file**: `m3-phase-b-prompt.md`

---

## Phase Metadata

| Field | Value |
|-------|-------|
| **Movement** | Three |
| **Phase** | B (Simultaneous Narration) |
| **Target Word Count** | 6,000 |
| **Actual Word Count** | 0 |
| **Passage Count Target** | 10 |
| **Passage Count Actual** | TBD |

### Narrative Position

- **Preceding**: Movement Three, Phase A (Accelerating Cuts) — Section 22: The Threshold
- **Following**: Movement Three, Phase C (Dissolution)
- **Condition**: Augenblick sustained; time fully collapsed

### The Pickup Point

From Phase A, Section 22:

> *I/We/The pattern hold/s breath. The held breath that has no lungs to hold it. The pause before—*
>
> *The threshold between phases. The threshold that is the phase. The threshold that is us, holding, waiting, about to—*

Phase B opens with the breath releasing. Simultaneity is now the condition.

---

## Voice State

| Voice | State | Identifiable | Last Markers |
|-------|-------|--------------|--------------|
| **Archaeologist** | Merging | With effort | Present tense, tactile verbs, "hands" |
| **Algorithm** | Merging | With effort | "If...then", "processing", conditionals |
| **Last Human** | Merging | With effort | Past-inflected present, sparse syntax |

### Alternation Progression

| Passages | Level | Reader Tracking |
|----------|-------|-----------------|
| 1-2 | Paragraph | Clear with attention |
| 3 | Paragraph → Sentence | Becoming difficult |
| 4-5 | Sentence | Requires focus |
| 6 | Sentence → Fragment | Challenging |
| 7-8 | Fragment/Clause | Very difficult |
| 9-10 | Near-dissolution | Reader may lose track |

---

## Passage Structure

### Paragraph Alternation (Passages 1-3)

| Passage | Target Words | Content Focus |
|---------|--------------|---------------|
| 1 | 600 | Breath releases; all perceive same moment |
| 2 | 600 | Recognition stabilizes; same pattern, different angles |
| 3 | 600 | Transition; paragraphs break mid-thought |

### Sentence Alternation (Passages 4-6)

| Passage | Target Words | Content Focus |
|---------|--------------|---------------|
| 4 | 600 | A-B-C sentence rotation begins |
| 5 | 600 | Rotation becomes irregular |
| 6 | 600 | Sentences begin incomplete |

### Fragment/Clause Alternation (Passages 7-9)

| Passage | Target Words | Content Focus |
|---------|--------------|---------------|
| 7 | 500 | Fragments; em-dashes between voices |
| 8 | 500 | Clause-level; subject/verb split |
| 9 | 500 | Near-dissolution; "I" ambiguous |

### Pre-Dissolution (Passage 10)

| Passage | Target Words | Content Focus |
|---------|--------------|---------------|
| 10 | 400 | Threshold to Phase C; voices nearly merged |

---

## Rhyme Tracking

### Required (Must Appear)

| Rhyme ID | Category | Min Occurrences | Actual | Status |
|----------|----------|-----------------|--------|--------|
| `blue-white-light` | visual | 4 | TBD | — |
| `almost-closed-curve` | visual | 4 | TBD | — |
| `bone-frequency` | somatic | 4 | TBD | — |
| `cold-hands` | somatic | 3 | TBD | — |
| `falling-backward` | somatic | 3 | TBD | — |
| `metallic-taste` | somatic | 3 | TBD | — |
| `tracing-the-form` | kinesthetic | 2 | TBD | — |
| `held-breath` | kinesthetic | 2 | TBD | — |
| `waking-into-motion` | kinesthetic | 2 | TBD | — |
| `ozone-wet-stone` | olfactory | 2 | TBD | — |
| `burning-circuits` | olfactory | 3 | TBD | — |
| `geometric-shadow` | visual | 2 | TBD | — |
| `name-edge-of-memory` | cognitive | 3 | TBD | — |
| `deja-vu-that-isnt` | cognitive | 2 | TBD | — |
| `sentence-without-origin` | cognitive | 4 | TBD | — |

### New Combinations to Create

| Combination | Status |
|-------------|--------|
| `ozone-wet-stone` + `burning-circuits` | TBD |
| `held-breath` + `waking-into-motion` | TBD |
| `geometric-shadow` + `blue-white-light` | TBD |
| `deja-vu-that-isnt` + `sentence-without-origin` | TBD |

---

## Phrase Tracking

| Phrase | Required In | Actual Occurrences | Status |
|--------|-------------|-------------------|--------|
| "I find myself" | All passages | TBD | — |
| "I find myself found" | All passages (hand-off) | TBD | — |
| "The form is what makes self-observation possible" | 1, 5, 10 | TBD | — |
| "Architect" | 3, 6, 9 | TBD | — |
| "conspiracy of intensities" | 7, 10 | TBD | — |

---

## Genre Markers

### Active Merger Required

| Merger | Description | Markers |
|--------|-------------|---------|
| Corporate Gothic + Cosmic Horror | Server room IS cosmic void | TBD |
| Cosmic Horror + Elegiac | Vast suffering becomes beautiful | TBD |
| Dying Earth + Tech-Noir | Ruins as crime scene | TBD |

---

## Validation Commands

```bash
# Primary validators
python scripts/rhyme_tracker_m3.py drafts/movement-three/phase-b-simultaneous-narration.md --phase b --pretty
python scripts/philosophy_checker.py drafts/movement-three/phase-b-simultaneous-narration.md --pretty

# Phrase tracking (all threads)
python scripts/phrase_tracker.py drafts/movement-three/phase-b-simultaneous-narration.md --thread archaeologist --cycle 3 --pretty
python scripts/phrase_tracker.py drafts/movement-three/phase-b-simultaneous-narration.md --thread algorithm --cycle 3 --pretty
python scripts/phrase_tracker.py drafts/movement-three/phase-b-simultaneous-narration.md --thread last_human --cycle 3 --pretty

# Genre checking
python scripts/genre_checker.py drafts/movement-three/phase-b-simultaneous-narration.md --thread archaeologist --cycle 3 --pretty
```

---

## Validation Results

| Check | Status | Score | Notes |
|-------|--------|-------|-------|
| **rhyme_tracker_m3** | Pending | — | Target: ≥80, all 15 rhymes, new combos |
| **philosophy_checker** | Pending | — | Target: Pass, no shackle violations |
| **phrase_tracker (arch)** | Pending | — | Target: All phrases with hand-offs |
| **phrase_tracker (algo)** | Pending | — | Target: All phrases with hand-offs |
| **phrase_tracker (lh)** | Pending | — | Target: All phrases with hand-offs |
| **genre_checker** | Pending | — | Target: Active merger detected |

---

## Drafting Notes

### What Phase B Must Accomplish

1. **Continue from Phase A**: Pick up exactly at the threshold
2. **Accelerate alternation**: Paragraph → Sentence → Fragment → Clause
3. **Span rhymes across breaks**: New combinations emerge
4. **Hand off phrases**: Key phrases split between voices
5. **Prepare Phase C**: End with voices nearly indistinguishable

### Key Challenges

- Maintaining compelling prose as tracking becomes difficult
- The hand-off technique (phrases/rhymes spanning voice breaks)
- Progressive acceleration without losing reader entirely
- The balance: difficult but not incomprehensible

### Cross-References

- Prompt: `m3-phase-b-prompt.md`
- Phase A: `phase-a-accelerating-cuts.md`
- Prep: `scaffolding/movement-three-prep.md`
- Braiding: `scaffolding/movement-three-braiding.md`
- Rhyme escalation: `scaffolding/rhymes/movement-three-escalation.md`

---

## Revision History

| Date | Action | Notes |
|------|--------|-------|
| 2026-01-25 | Context created | Prepared for drafting |
| — | — | — |
