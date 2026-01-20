# Review Protocol

## Purpose

This document defines the structured feedback format for reviewing human-drafted sections. All review feedback should follow this format for consistency.

---

## Review Output Format

```markdown
# Scene Review: [Scene ID or Description]

**Thread**: [archaeologist/algorithm/last_human]
**Movement**: [one/two/three/four]
**Word Count**: [actual] / [target]
**Date**: [YYYY-MM-DD]

---

## Validation Results

| Check | Status | Notes |
|-------|--------|-------|
| Voice | ✅ PASS / ❌ FAIL | [Brief note] |
| Philosophy | ✅ PASS / ❌ FAIL | [Brief note] |
| Rhyme | ✅ PASS / ❌ FAIL | [Brief note] |
| Genre | ✅ PASS / ❌ FAIL | [Brief note] |

---

## Overall Assessment

**Rating**: [Strong / Needs Work / Major Revision Required]

[2-3 sentences summarizing the draft's strengths and primary areas for improvement]

---

## Specific Issues

### Voice Issues
[If any voice contamination or drift detected]

| Line | Issue | Suggestion |
|------|-------|------------|
| [X] | [Specific problem] | [Specific fix] |

### Philosophy Issues
[If any Four Shackles violations or other philosophical misalignment]

| Line | Issue | Suggestion |
|------|-------|------------|
| [X] | [Specific problem] | [Specific fix] |

### Rhyme Issues
[Missing rhymes, wrong intensity, poor integration]

| Issue | Suggestion |
|-------|------------|
| [Problem] | [Fix] |

### Genre Issues
[Missing markers, wrong register, insufficient pressure]

| Issue | Suggestion |
|-------|------------|
| [Problem] | [Fix] |

### Prose Craft Issues
[Line-level craft problems not covered above]

| Line | Issue | Suggestion |
|------|-------|------------|
| [X] | [Specific problem] | [Specific fix] |

---

## Recommendations

### Priority 1 (Must Address)
- [Action item]

### Priority 2 (Should Address)
- [Action item]

### Priority 3 (Consider)
- [Action item]

---

## Script Output

[Paste raw JSON output from validation scripts for reference]
```

---

## Review Checklist

When reviewing, check in this order:

### 1. Voice Consistency

- [ ] Correct tense throughout
- [ ] Appropriate syntax patterns
- [ ] Thread-specific concerns present
- [ ] Thread-specific texture present
- [ ] No contamination from other voices

### 2. Philosophical Alignment

- [ ] No identity language between the three
- [ ] Recognition through intensity, not memory
- [ ] Technical substrate present
- [ ] Active affirmation (if applicable)
- [ ] No Four Shackles violations

### 3. Rhyme Integration

- [ ] At least one rhyme present (for Movement 1+)
- [ ] Rhyme intensity appropriate to movement
- [ ] Rhymes integrated naturally, not forced
- [ ] Registry usage would be updated correctly

### 4. Genre Pressure

- [ ] Genre markers present for this thread
- [ ] Elevation techniques employed
- [ ] Bleed patterns correct (Movement 3+)
- [ ] Not overwhelming the philosophical content

### 5. Craft Quality

- [ ] Opening hooks effectively
- [ ] Closing provides appropriate momentum
- [ ] Sensory details are specific, not generic
- [ ] Verbs are active and precise
- [ ] No clichés or dead metaphors
- [ ] Word count within ±10% of target

---

## Severity Levels

Use these when categorizing issues:

| Severity | Definition | Action |
|----------|------------|--------|
| **Critical** | Breaks voice, violates Four Shackles | Must fix before proceeding |
| **Major** | Significant craft issues, missing required elements | Should fix in this revision pass |
| **Minor** | Polish-level concerns | Can defer to line-edit pass |
| **Note** | Stylistic suggestions, not problems | Author discretion |

---

## Example Review

```markdown
# Scene Review: m1-arch-01 Opening: Daily Excavation

**Thread**: archaeologist
**Movement**: one
**Word Count**: 2847 / 3000
**Date**: 2026-01-20

---

## Validation Results

| Check | Status | Notes |
|-------|--------|-------|
| Voice | ✅ PASS | Strong present tense, tactile details |
| Philosophy | ✅ PASS | No shackle violations detected |
| Rhyme | ✅ PASS | held-breath, ozone-wet-stone present |
| Genre | ⚠️ PARTIAL | Corporate Gothic present but could be stronger |

---

## Overall Assessment

**Rating**: Needs Work

Strong opening voice and effective establishment of economic stakes. The rhyme integration is subtle and appropriate for Movement 1. Genre pressure is present but the "data as corpse" elevation is underutilized. Some sentences in the middle section drift toward passive construction.

---

## Specific Issues

### Genre Issues

| Issue | Suggestion |
|-------|------------|
| Data work described clinically, not intimately | Add one moment where handling data feels invasive, like going through someone's private belongings |

### Prose Craft Issues

| Line | Issue | Suggestion |
|------|-------|------------|
| 47 | "The files were loaded by the system" | Active voice: "The system loads the files" |
| 82 | "He began to realize" | Direct: "He realizes" |
| 103 | Paragraph runs 8 sentences without pause | Break into 2 paragraphs for rhythm |

---

## Recommendations

### Priority 1 (Must Address)
- Strengthen genre pressure with one "intimate invasion" moment around line 60

### Priority 2 (Should Address)
- Fix passive constructions on lines 47, 82
- Improve paragraph rhythm in mid-section

### Priority 3 (Consider)
- Could add more specific hardware details to strengthen texture
```
