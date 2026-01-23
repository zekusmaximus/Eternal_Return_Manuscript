# Drafting Workflow

## Overview

This document defines the dual-mode workflow for drafting *The Eternal Return of the Digital Self*. All agents should reference this file when entering a drafting or review session.

---

## Mode A: AI-Driven Drafting

### When to Use

- Drafting new scenes from scratch
- Generating voice samples or exercises
- Creating rhyming moment variations

### Workflow

```
1. CONTEXT ASSEMBLY
   ↓
2. DRAFT GENERATION
   ↓
3. VALIDATION (voice → philosophy → rhyme → genre)
   ↓
4. ITERATION (if any check fails)
   ↓
5. USER REVIEW
```

### Step 1: Context Assembly

Before drafting, the agent MUST assemble context from these sources:

| Source | Location | Required For |
|--------|----------|--------------|
| Scene metadata | `drafts/manifest.json` | Word count target, position, notes |
| Voice reference | `voices/{thread}.md` | Tense, syntax, texture, forbidden patterns |
| Rhyme registry | `scaffolding/rhymes/registry.md` | Available rhymes, intensity level |
| Genre pressure | `scaffolding/genre-pressure.md` | Genre markers for this thread/movement |
| Philosophy constraints | `protocols/philosophy-constraints.md` | Four Shackles, writing checks |

Use the prompt template in `protocols/prompt-template.md` to structure this context.

### Step 2: Draft Generation

- Draft to target word count ±10%
- Maintain voice consistency as primary concern
- Include at least one rhyme appropriate to movement intensity
- Apply genre pressure per thread register

### Step 3: Validation

**Before running scripts**: Set cycle in `scripts/movement_config.json`. All scripts read from this config.

Run validation scripts in order:

```bash
# From project root
python scripts/voice_validator.py drafts/path/to/scene.md --thread archaeologist --pretty
python scripts/rhyme_tracker.py drafts/path/to/scene.md --pretty
python scripts/phrase_tracker.py drafts/path/to/scene.md --thread archaeologist --pretty
python scripts/philosophy_checker.py drafts/path/to/scene.md --thread archaeologist --pretty
python scripts/genre_checker.py drafts/path/to/scene.md --thread archaeologist --pretty
```

**For scene handoffs** (validating rhyme echoes from previous scene):

```bash
python scripts/rhyme_tracker.py drafts/path/to/scene.md --previous-closing '["bone-frequency","cold-hands"]' --pretty
```

All scripts output JSON (or formatted text with `--pretty`). A scene passes when all scripts report `"status": "pass"`.

### Step 4: Iteration

If any validation fails:

1. Read specific issues from script output
2. Revise the flagged lines/sections
3. Re-run failed validation
4. **Repeat until all scripts report `"status": "pass"`**

> **CRITICAL**: Do not submit scene to USER until all validations pass. Revise and re-validate iteratively.

### Step 5: User Review

Once all validations pass:

1. Update `drafts/manifest.json` with:
   - `status`: "draft"
   - `actual_words`: word count
   - `voice_check`: "passed"
   - `philosophy_check`: "passed"
   - `rhyme_check`: "passed"  
   - `genre_check`: "passed"
2. Present scene to user for review
3. User accepts, edits, or requests revision

---

## Mode B: Human Review

### When to Use

- User has drafted a scene or section
- User has made manual edits to an AI-drafted scene
- User wants feedback on a specific passage

### Workflow

```
1. USER SUBMITS DRAFT
   ↓
2. CONTEXT IDENTIFICATION
   ↓
3. VALIDATION SCRIPTS
   ↓
4. DETAILED ANALYSIS
   ↓
5. STRUCTURED FEEDBACK
```

### Step 1: User Submission

User provides:

- The draft text (as file path or inline)
- Target thread (archaeologist/algorithm/last_human)
- Target movement (one/two/three/four)
- Scene ID (if applicable)

### Step 2: Context Identification

Agent loads:

- Voice reference for the specified thread
- Rhyme registry for usage tracking
- Genre pressure guidelines for thread/movement
- Philosophy constraints

### Step 3: Validation Scripts

**Set cycle in `scripts/movement_config.json` first.**

Run all validation scripts:

```bash
python scripts/voice_validator.py [file] --thread [thread] --pretty
python scripts/rhyme_tracker.py [file] --pretty
python scripts/phrase_tracker.py [file] --thread [thread] --pretty
python scripts/philosophy_checker.py [file] --thread [thread] --pretty
python scripts/genre_checker.py [file] --thread [thread] --pretty
```

### Step 4: Detailed Analysis

Beyond script output, agent manually checks:

- Opening hook effectiveness
- Closing momentum/closure
- Sensory density and specificity
- Prose rhythm and sentence variety
- Line-level craft issues

### Step 5: Structured Feedback

Use the format in `protocols/review-protocol.md`:

```markdown
## Review Summary
[Overall assessment: Strong/Needs Work/Major Revision]

## Validation Results
- Voice: PASS/FAIL
- Philosophy: PASS/FAIL
- Rhyme: PASS/FAIL
- Genre: PASS/FAIL

## Specific Issues
1. [Line X]: [Issue] → [Suggested fix]
2. [Line Y]: [Issue] → [Suggested fix]

## Recommendations
- [Priority 1 action]
- [Priority 2 action]
```

---

## Status Progression

Scenes progress through these statuses:

```
not_started → draft → validated → revised → polished → final
```

| Status | Meaning |
|--------|---------|
| `not_started` | No content |
| `draft` | First draft exists, validations in progress |
| `validated` | All automated checks pass |
| `revised` | User has reviewed and made content edits |
| `polished` | Line-level prose editing complete |
| `final` | Ready for manuscript |

---

## Quick Reference

### Validation Script Locations

```
scripts/
├── movement_config.json   # Edit "cycle" here before running validators
├── voice_validator.py     # Voice + contamination
├── rhyme_tracker.py       # Rhymes + handoffs
├── phrase_tracker.py      # Key phrase bleeding
├── philosophy_checker.py  # Pharmakon + shackles
└── genre_checker.py       # Genre + bleed tolerance
```

### Key Reference Files

```
voices/
├── archaeologist.md
├── algorithm.md
└── last-human.md

scaffolding/
├── rhymes/registry.md
└── genre-pressure.md

protocols/
├── drafting-workflow.md (this file)
├── prompt-template.md
├── review-protocol.md
└── philosophy-constraints.md
```
