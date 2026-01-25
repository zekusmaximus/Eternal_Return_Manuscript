# Context: Movement Three Phase A — Accelerating Cuts

> **Prose file**: `phase-a-accelerating-cuts.md`
> **Phase ID**: m3-phase-a
> **Status**: Not Started
> **Prompt file**: `m3-phase-a-prompt.md`

---

## Phase Metadata

| Field | Value |
|-------|-------|
| **Movement** | Three |
| **Phase** | A (Accelerating Cuts) |
| **Target Word Count** | 6,000 |
| **Actual Word Count** | 0 |
| **Section Count Target** | 18-22 |
| **Section Count Actual** | TBD |

### Narrative Position

- **Preceding**: Movement Two, Cycle Three, Scene 9 (m2-lh-03 "The Interface")
- **Following**: Movement Three, Phase B (Simultaneous Narration)
- **Trigger**: Last Human's hand touches the interface; Augenblick begins

### The Pickup Point

From M2-LH-03, the final lines:

> *My hand—*
> *The cold in my hands meets the cold of the form.*
> *The threshold—*

Phase A opens with the completion of this gesture. The touch happens.

---

## Voice State

| Voice | State | Identifiable | Contamination Level |
|-------|-------|--------------|---------------------|
| **Archaeologist** | Distinct but contaminated | Yes (first sentence) | Heavy (6-8 markers/section) |
| **Algorithm** | Distinct but contaminated | Yes (first sentence) | Heavy (6-8 markers/section) |
| **Last Human** | Distinct but contaminated | Yes (first sentence) | Heavy (6-8 markers/section) |

### Contamination Markers to Track

**Archaeologist acquires from**:
- Algorithm: conditional syntax, processing vocabulary
- Last Human: sentence fragments, past-inflection

**Algorithm acquires from**:
- Archaeologist: tactile verbs, economic language
- Last Human: sparse syntax, silence awareness

**Last Human acquires from**:
- Archaeologist: present tense, dense description
- Algorithm: probability language, conditionals

---

## Section Structure

### Opening Trio (Sections 1-3)

| Section | Voice | Target Words | Content Focus |
|---------|-------|--------------|---------------|
| 1 | Last Human | 500 | Touch completes; frequency peaks; others flood in |
| 2 | Algorithm | 500 | Ghost becomes actual; perceives both others |
| 3 | Archaeologist | 500 | Bleed total; at workstation and not; sees others |

### Middle Collision (Sections 4-12)

| Section | Voice | Target Words | Content Focus |
|---------|-------|--------------|---------------|
| 4 | Algorithm | 400 | Processing Archaeologist's data-self |
| 5 | Archaeologist | 400 | Speaking Algorithm syntax; writing as prayer |
| 6 | Last Human | 350 | Interface holds him; name dissolves |
| 7 | Archaeologist | 350 | Merge accelerating; Lena absence |
| 8 | Algorithm | 300 | Recursive self-reference; the break |
| 9 | Last Human | 300 | Dreams are memories are present |
| 10 | Algorithm | 250 | All hands are same gesture |
| 11 | Archaeologist | 250 | Phrases without origin |
| 12 | Last Human | 250 | Frequency is harmony; says yes |

### Transition Strobe (Sections 13-18+)

| Section | Voice | Target Words | Content Focus |
|---------|-------|--------------|---------------|
| 13 | Archaeologist | 200 | Hands on interface/keyboard |
| 14 | Last Human | 150 | Hands on interface |
| 15 | Algorithm | 150 | Hands as topology |
| 16 | Archaeologist | 150 | Speaking LH's sentence |
| 17 | Last Human | 150 | Completing Algo's thought |
| 18 | Algorithm | 200 | Processing as memory |

---

## Rhyme Tracking

### Required (Must Appear)

| Rhyme ID | Category | Min Occurrences | Actual | Sections |
|----------|----------|-----------------|--------|----------|
| `blue-white-light` | visual | 3 | TBD | TBD |
| `almost-closed-curve` | visual | 3 | TBD | TBD |
| `bone-frequency` | somatic | 3 | TBD | TBD |
| `cold-hands` | somatic | 3 | TBD | TBD |
| `falling-backward` | somatic | 2 | TBD | TBD |
| `metallic-taste` | somatic | 2 | TBD | TBD |
| `tracing-the-form` | kinesthetic | 1 | TBD | TBD |
| `held-breath` | kinesthetic | 1 | TBD | TBD |
| `waking-into-motion` | kinesthetic | 1 | TBD | TBD |
| `ozone-wet-stone` | olfactory | 1 | TBD | TBD |
| `burning-circuits` | olfactory | 1 | TBD | TBD |
| `geometric-shadow` | visual | 1 | TBD | TBD |
| `name-edge-of-memory` | cognitive | 2 | TBD | TBD |
| `deja-vu-that-isnt` | cognitive | 1 | TBD | TBD |
| `sentence-without-origin` | cognitive | 2 | TBD | TBD |

### Stacking Targets

- **Sections 1-3**: 4 rhymes each (sequential)
- **Sections 4-12**: 3-4 rhymes each
- **Sections 13-18**: 2-3 rhymes each (overlap begins)

---

## Phrase Tracking

| Phrase | Required In | Actual Occurrences |
|--------|-------------|-------------------|
| "I find myself" | All 3 voices | TBD |
| "I find myself found" | All 3 voices | TBD |
| "The form is what makes self-observation possible" | 2+ voices | TBD |
| "Architect" | All 3 voices | TBD |
| "conspiracy of intensities" | 1+ voice | TBD |

---

## Genre Markers

### Per Section Target: 4-5 markers with cross-contamination

| Genre | Thread Origin | Bleeds Into | Markers to Use |
|-------|--------------|-------------|----------------|
| Corporate Gothic | Archaeologist | Algorithm, LH | server rooms, sterile light, data work |
| Cosmic Horror | Algorithm | Archaeologist, LH | scale paralysis, phantom sensation, sublime |
| Dying Earth | Last Human | Archaeologist, Algo | ruins, silence, temporal weight |

---

## Validation Commands

```bash
# Primary validators
python scripts/rhyme_tracker_m3.py drafts/movement-three/phase-a-accelerating-cuts.md --phase a --pretty
python scripts/philosophy_checker.py drafts/movement-three/phase-a-accelerating-cuts.md --pretty

# Phrase tracking (all threads)
python scripts/phrase_tracker.py drafts/movement-three/phase-a-accelerating-cuts.md --thread archaeologist --cycle 3 --pretty
python scripts/phrase_tracker.py drafts/movement-three/phase-a-accelerating-cuts.md --thread algorithm --cycle 3 --pretty
python scripts/phrase_tracker.py drafts/movement-three/phase-a-accelerating-cuts.md --thread last_human --cycle 3 --pretty

# Genre checking (all threads)
python scripts/genre_checker.py drafts/movement-three/phase-a-accelerating-cuts.md --thread archaeologist --cycle 3 --pretty
python scripts/genre_checker.py drafts/movement-three/phase-a-accelerating-cuts.md --thread algorithm --cycle 3 --pretty
python scripts/genre_checker.py drafts/movement-three/phase-a-accelerating-cuts.md --thread last_human --cycle 3 --pretty
```

---

## Validation Results

| Check | Status | Score | Notes |
|-------|--------|-------|-------|
| **rhyme_tracker_m3** | Pending | — | Target: ≥70, all 15 rhymes |
| **philosophy_checker** | Pending | — | Target: Pass, no shackle violations |
| **phrase_tracker (arch)** | Pending | — | Target: All phrases present |
| **phrase_tracker (algo)** | Pending | — | Target: All phrases present |
| **phrase_tracker (lh)** | Pending | — | Target: All phrases present |
| **genre_checker (arch)** | Pending | — | Target: Bleed detected |
| **genre_checker (algo)** | Pending | — | Target: Bleed detected |
| **genre_checker (lh)** | Pending | — | Target: Bleed detected |

---

## Drafting Notes

### What Phase A Must Accomplish

1. **Complete the trigger**: The touch from M2-LH-03 finalizes
2. **Establish collision**: All three perceive each other directly
3. **Accelerate rotation**: A-B-C becomes irregular, sections shorten
4. **Heavy contamination**: Voices distinct but thoroughly interpenetrated
5. **Prepare Phase B**: End ready for sentence-level alternation

### Key Challenges

- Maintaining readability despite heavy contamination
- Progressive section shortening without losing content
- The strobe effect at end (voices almost indistinguishable)
- Ensuring all rhymes and phrases appear naturally

### Cross-References

- Prompt: `m3-phase-a-prompt.md`
- Prep: `scaffolding/movement-three-prep.md`
- Braiding: `scaffolding/movement-three-braiding.md`
- Rhyme escalation: `scaffolding/rhymes/movement-three-escalation.md`

---

## Revision History

| Date | Action | Notes |
|------|--------|-------|
| 2026-01-25 | Context created | Prepared for drafting |
| — | — | — |
