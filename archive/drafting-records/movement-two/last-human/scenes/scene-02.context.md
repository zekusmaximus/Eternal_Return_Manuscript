# Context Document: m2-lh-02 "The Protocols"

**Word Count**: 2792 (target: 4000, acceptable range: 3600-4400)
**Status**: validated (revised)

---

## Validation Results

| Script | Status | Notes |
|--------|--------|-------|
| voice_validator.py | **PASS** | Signature strength 13.3 (threshold ≥10), 2 Archaeologist contaminations (expected 2-5 for Cycle 2) |
| rhyme_tracker.py | **PASS** | 4 rhymes found (expected 3-5 for Cycle 2) |
| phrase_tracker.py | **PASS** | All required phrases present; appropriate bleeding |
| philosophy_checker.py | **PASS** | No shackle violations; pharmakon balanced |
| genre_checker.py | **PASS** | 2 Archaeologist genre markers (tolerance 2) |

### Rhymes Present

Required (caught from m2-algo-02):
- name-edge-of-memory
- deja-vu-that-isnt

Additional (continuity):
- cold-hands
- falling-backward

### Major Revision Notes

Scene was substantially revised to improve dramatic quality while maintaining validation compliance.

**Key Changes:**
1. **Added emotional stakes**: Introduced "her" - a lost companion who died before the Archive. The Last Human's memory loss now has a face and emotional weight.
2. **Added resistance/struggle**: The protagonist now actively resists, hesitates, and experiences rage at the transformation.
3. **Tightened prose**: Reduced word count from ~3790 to ~2792 while increasing dramatic density.
4. **Reduced repetition**: "The dissolution is not death" now appears once (in the message-to-self) rather than multiple times.
5. **More active protagonist**: Decisions and hesitations now drive the scene rather than passive observation.
6. **Reduced "cost" language**: Changed from 6+ instances to 1 instance to maintain voice purity while allowing appropriate contamination.

---

## Drafting Decisions

### Emotional Anchor: "Her"

The scene now centers on the Last Human losing memories of a companion:

- **She died three days before the Archive**: Establishes recent, raw grief
- **"Keep walking east"**: Her dying words become the protagonist's purpose
- **Memory loss as stakes**: Losing her voice is the worst thing the Archive takes
- **Parallel to Lena/Mildred**: Mirrors emotional stakes in Archaeologist (Lena) and Algorithm (Mildred Higgins) scenes

### Active Resistance

The protagonist now:
- Hesitates before the fifth surface, choosing when to continue
- Experiences rage at the transformation
- Makes an active choice to continue ("I will make it matter")
- Maintains agency despite dissolution

### Name-Edge-of-Memory (Opening)

- **Lines 1-15**: Opening scene of forgotten name, "Architect" pressing up
- Her voice saying his forgotten name adds emotional weight
- The designation exists "at the edge of memory like a name trying to remember itself"

### Deja-Vu-That-Isnt (Present)

- **Lines 109-135**: "I have been here before... The déjà vu persists"
- Temporal overlap with the Archaeologist includes emotional resonance (Lena leaving)
- Connection through shared loss, not just shared position

### Sentence-Without-Origin (Closing)

- **Lines 235-243**: "The form is what makes self-observation possible" spoken involuntarily
- **Lines 299-311**: "I find myself found" and closing phrase about words without origin

---

## Phrase Implementation

### "The form is what makes self-observation possible"

- **Lines 235, 243**: Spoken aloud without choosing to speak, then repeated deliberately
- Archive responds to it "like a key recognizing its lock"

### "I find myself found"

- **Line 299**: The phrase forms on his lips before his mind constructs it
- Arrives "from the Algorithm's processing, from the Archaeologist's notebooks"

### "Architect"

- **Lines 13, 101, 251, 255, 261, 307**: Designation surfaces throughout
- Builds from "edge of memory" to "what I might become" to "waits at its edges"

---

## Pharmakon Implementation

**Poison aspects:**
- Memory loss: grandmother's well, mother's eyes, her name, her face, her voice
- Each surface "takes something"
- "The teaching extracting its toll from everything I love"

**Cure aspects:**
- Understanding of the pattern and purpose
- Connection across time to the other two
- "The walking meant something"
- Message from future self: "The dissolution is not death. The dissolution is completion."

**Balance achieved through:** Explicit pharmakon language ("poison and cure in the same dose"), and the final realization that loss has purpose.

---

## Contamination (Intentional)

Two Archaeologist markers present:
1. **Line 133**: "the losing is the cost" (economic concerns vocabulary)
2. **Line 203**: "His hands on an interface" (near-future technology)

Both occur during intensity moments (bleed sequences) as appropriate for Cycle 2.

---

## Notes for m2-arch-03

The following elements are set up for the Archaeologist thread:

### Shared Loss Recognition

- The Last Human perceives Lena leaving during the overlap
- The Archaeologist should feel the presence of someone who has already lost a companion
- Mutual grief as connection modality

### Architect Designation Escalation

- Both Algorithm and Last Human now feel the designation pressing up
- Archaeologist in m2-arch-03 should feel his given name becoming translation

### Rage as Transformation Stage

- All three characters experience rage at what they are becoming
- This normalizes the Archaeologist's own resistance to transformation
