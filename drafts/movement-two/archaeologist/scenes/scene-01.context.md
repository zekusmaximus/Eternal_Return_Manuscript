# m2-arch-01 "The Bleed" - Context Documentation

## Drafting Date
2026-01-23

## Key Decisions

### Saturday Resolution
**Option A chosen**: Saturday (Lena's mother's 70th birthday) has passed. The scene shows aftermath through:
- Lena's silences and distance in the morning
- Retrospective dialogue about his behavior at the party ("You kept touching your chest," "You called Marcus by the wrong name")
- His inability to remember most of the party, only fragments surfacing through fog
- The moment he couldn't remember his mother's middle name

This approach grounds the cosmic in the relational and shows consequences rather than anticipation.

### First Bleed Integration
The ~1200 words from `first-bleed.md` were distributed throughout the scene rather than front-loaded:

**Preserved verbatim or near-verbatim:**
- "The panic thinks I am vast" (line 59)
- The drowning-fall vertigo description (adapted, line 51)
- "I am maintaining something. Many somethings." (adapted, line 67-68)
- The spiral tracing mention (adapted to match reduced rhyme count)
- "Something is watching me work. Something is grateful that he hasn't stopped." (closing lines 268-270)

**Adapted/expanded:**
- The Algorithm's perspective during bleeds - toned down cosmic horror elements for Cycle 1 tolerance
- Lena finding him in kitchen/break room - relocated to his home, expanded with Saturday aftermath
- The coffee tasting like metal - removed to reduce rhyme density

### Lena Arc Positioning
**Cycle 1 - Concern and Noticing phase:**
- Opens with her absence (early shift) but presence through coffee, silences
- Physical concern: "You're freezing" when she touches him
- Offers rational explanation: "Depersonalization. Classic overwork symptom."
- Still trying to reach him, still in the relationship
- Ends with "I'm not leaving. But I'm also not going to pretend this is okay."

This positions her for Cycle 2's confrontation/breaking point.

### Rhyme Placement
Final validated rhymes (4 total, within 2-4 expected range):

| Rhyme | Location | Line |
|-------|----------|------|
| `cold-hands` | Opening (first 500 words) | 7 |
| `falling-backward` | First Bleed | 51 |
| `waking-into-motion` | Second Bleed aftermath | 192, 194 |
| `bone-frequency` | Closing | 260 |

**Removed during revision** to meet Cycle 1 rhyme density:
- `blue-white-light` (2 instances removed)
- `almost-closed-curve` (3 instances removed)
- `tracing-the-form` (2 instances removed)
- `ozone-wet-stone` (removed)
- `metallic-taste` (removed)
- `deja-vu-that-isnt` (removed)

### Contamination Moments
Algorithm voice bleeds in during three clearly marked intrusions:

1. **First Bleed** (lines 67-72): Perspective shift, "I am maintaining something..."
2. **Second Bleed** (lines 165-190): Full Algorithm perspective, including code-style comments
3. **Code comments** (lines 77, 173-175, 187-190): `*// the watcher finds himself watching*`, `*// query: who is the writer*`

Return to grounded voice marked by:
- Physical sensations: "I come back to my body with a gasp. Feel the weight of my hands, the pressure of the chair against my back, the cold air on my face."
- Concrete details: timestamps, room descriptions, Lena's presence
- Active verb construction returning

### Pharmakon Implementation
Explicit poison/cure duality appears in two key passages:

1. Lines 81-86: "The bleed is terrifying—this dissolution of boundaries, this erosion of the self... But it's also something else. The Martinez extraction is better than it was an hour ago... Poison and cure in the same dose."

2. Lines 252-255: "Whatever this is, it's making me better at what I do. The same process that's dissolving my sense of self is also sharpening my craft. The same poison that's changing me is curing the Martinez extraction of errors I couldn't have seen before."

## Deviations from Prompt

1. **Reduced rhyme count**: Prompt suggested including `tracing-the-form`, `ozone-wet-stone`, `metallic-taste` as echoes from M1. These were removed during validation to meet Cycle 1's 2-4 rhyme expectation.

2. **Cosmic horror elements toned down**: The Algorithm's perspective during bleeds was softened to meet genre bleed tolerance of 1 for Cycle 1.

3. **Martinez extraction status**: Kept ongoing rather than completed, providing continuity with work context and demonstrating pharmakon (the code improving even as he dissolves).

## Handoff Notes for m2-algo-01

### Moments to Echo
- The specific timestamp of the first bleed (9:47 AM) could resonate as a processing anomaly
- The "watching from inside the watching" concept should appear from Algorithm's side
- The Archaeologist's choice to continue should register as relief/gratitude

### Rhymes to Carry
- `bone-frequency` (this scene's closing rhyme) → should appear in m2-algo-01's opening
- `cold-hands` → should appear in memories Algorithm accesses
- `falling-backward` → vertigo of self-recognition from Algorithm's perspective

### Perspective-Flip Opportunities
1. The moment "I find myself" surfaces (line 165) - Algorithm experiences this as a past-signal
2. The code comments during second bleed - these should appear as the Algorithm's actual processing
3. "Something is watching me work" - the Algorithm IS the something

## Validation Results

### Initial Validation Issues
1. **Voice validator**: Initially weak signature (9.8), strengthened to 11.4 by adding tactile vocabulary
2. **Rhyme tracker**: Initially 9 rhymes, reduced to 4 through targeted removal
3. **Philosophy checker**: Pharmakon markers added ("Poison and cure in the same dose")
4. **Genre checker**: Genre bleed initially 4, reduced to 1 by softening cosmic horror elements

### Final Validation Status
| Script | Status |
|--------|--------|
| voice_validator.py | PASS |
| rhyme_tracker.py | PASS |
| phrase_tracker.py | PASS |
| philosophy_checker.py | PASS (with warn on secondary pharmakon analysis) |
| genre_checker.py | PASS |

### Word Count
- Target: 4000 (±10%: 3600-4400)
- Actual: 4026
- Status: Within target range
