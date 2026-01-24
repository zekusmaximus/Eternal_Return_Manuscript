# Scene Lifecycle Protocol

## Overview

This protocol defines the complete lifecycle management for scenes in *The Eternal Return of the Digital Self*, structuring how scenes progress from conception through final manuscript-ready status. It is designed to align with how Claude Code and AI agents process tasks, providing clear decision trees, validation checkpoints, and handoff procedures.

**Status Progression**:
```
not_started → draft → validated → revised → polished → final
```

Each phase has specific entry criteria, required actions, validation steps, and exit criteria.

---

## Phase 1: Creation (not_started → draft)

### Entry Criteria
- Scene metadata exists in `drafts/manifest.json`
- Scene ID, thread, movement, and target word count are defined
- Previous scene in thread (if any) is at least in `draft` status
- Required context files exist:
  - `voices/{thread}.md`
  - `scaffolding/rhymes/registry.md`
  - `scaffolding/genre-pressure.md`
  - `protocols/philosophy-constraints.md`

### Task Definition for AI Agent

When creating a new scene, the agent must:

#### Step 1: Context Assembly
Assemble context using `protocols/prompt-template.md` structure:
1. Load scene metadata from `drafts/manifest.json`
2. Load voice reference from `voices/{thread}.md`
3. Load rhyme requirements from `scaffolding/rhymes/registry.md`
4. Load genre pressure from `scaffolding/genre-pressure.md`
5. Load philosophy constraints from `protocols/philosophy-constraints.md`
6. Review preceding scene for narrative continuity
7. Identify any rhyme handoffs from previous scene

#### Step 2: Pre-Draft Planning
Before writing, determine:
- Opening hook strategy
- Key narrative beats for this scene
- Required rhyming moments (1-2 for Movement 1, 2-3 for Movement 2+)
- Genre markers to include
- Closing momentum/handoff
- Specific philosophical concepts to dramatize

#### Step 3: Draft Generation
Write to target word count ±10% with:
- **Voice Priority**: Voice consistency is paramount
- **Sensory Specificity**: Concrete, specific sensory details
- **Present Texture**: Thread-specific environmental texture
- **Rhyme Integration**: Natural, not forced
- **Genre Markers**: Appropriate to thread and movement
- **Philosophy**: Dramatize, don't explain

#### Step 4: Self-Review
Before validation, agent should:
- Read draft aloud (internally) for rhythm
- Check for voice consistency
- Verify rhyme integration
- Confirm philosophy alignment
- Check word count (2700-3300 for 3000 target)

### Exit Criteria
- Scene file created at specified path
- Word count within ±10% of target
- Agent believes all voice, rhyme, genre, and philosophy requirements are met
- Ready for validation phase

### Outputs
- `{scene-id}.md` - Pure prose file
- `{scene-id}.context.md` - Metadata and drafting notes
- Update `drafts/manifest.json` with:
  ```json
  {
    "status": "draft",
    "actual_words": [count]
  }
  ```

---

## Phase 2: Validation (draft → validated)

### Entry Criteria
- Scene status is `draft`
- Scene file exists and contains prose
- Word count is within acceptable range

### Task Definition for AI Agent

#### Step 1: Environment Setup
1. Verify `scripts/movement_config.json` has correct cycle setting
2. Prepare validation script execution

#### Step 2: Run Validation Scripts
Execute in order (fail fast - stop on first failure):

```bash
# 1. Voice validation
python scripts/voice_validator.py [scene-path] --thread [thread] --pretty

# 2. Rhyme validation
python scripts/rhyme_tracker.py [scene-path] --pretty

# 3. Phrase validation
python scripts/phrase_tracker.py [scene-path] --thread [thread] --pretty

# 4. Philosophy validation
python scripts/philosophy_checker.py [scene-path] --thread [thread] --pretty

# 5. Genre validation
python scripts/genre_checker.py [scene-path] --thread [thread] --pretty
```

#### Step 3: Analyze Results
For each failed validation:
1. Read specific issues from script output
2. Identify problematic lines/sections
3. Understand the nature of the violation

#### Step 4: Iteration
If any validation fails:
1. Revise the flagged lines/sections
2. Maintain voice consistency during revisions
3. Re-run only the failed validation(s)
4. Repeat until all validations pass
5. **Critical**: Do NOT proceed to exit until all validations pass

#### Step 5: Manual Validation
After scripts pass, agent should manually verify:
- Opening hook is effective
- Closing provides momentum
- Narrative beats are clear
- Sensory details are specific
- No clichés or dead metaphors
- Prose rhythm varies appropriately

### Exit Criteria
- All five validation scripts report `"status": "pass"`
- Manual verification complete
- Agent has confidence in scene quality

### Outputs
- Updated scene file (if revisions were needed)
- Update `drafts/manifest.json` with:
  ```json
  {
    "status": "validated",
    "voice_check": "passed",
    "philosophy_check": "passed",
    "rhyme_check": "passed",
    "genre_check": "passed",
    "phrase_check": "passed"
  }
  ```
- Updated `{scene-id}.context.md` with validation notes

### Validation Failure Handling

If validation cannot be achieved after 3 revision attempts:
1. Document specific blockers in context file
2. Flag scene for human review
3. Create issue summary for author
4. Do NOT mark as validated

---

## Phase 3: Review (validated → revised)

### Entry Criteria
- Scene status is `validated`
- All validation scripts pass
- Human review is requested

### Task Definition for AI Agent

This phase uses **Mode B: Human Review** from `protocols/drafting-workflow.md`.

#### Step 1: Context Loading
1. Load voice reference for thread
2. Load rhyme registry for usage tracking
3. Load genre pressure guidelines
4. Load philosophy constraints
5. Review scene metadata and notes

#### Step 2: Structured Analysis
Analyze beyond script validation:

**Narrative Level**:
- Does opening establish situation effectively?
- Are character motivations clear?
- Does pacing match movement requirements?
- Does closing provide appropriate momentum?

**Prose Level**:
- Sentence rhythm and variety
- Verb strength and precision
- Metaphor originality
- Sensory detail specificity
- Paragraph flow and structure

**Thread Consistency**:
- Voice maintained throughout
- Thread-specific concerns present
- Texture consistent with world
- Genre elevation effective

#### Step 3: Generate Review
Use format from `protocols/review-protocol.md`:

```markdown
# Scene Review: [Scene ID]

**Thread**: [thread]
**Movement**: [movement]
**Word Count**: [actual] / [target]
**Overall Assessment**: [Strong/Needs Work/Major Revision]

## Validation Results
[Table of script results]

## Specific Issues
[Categorized by severity: Critical, Major, Minor, Note]

## Recommendations
[Prioritized action items]
```

#### Step 4: Present to User
- Submit review following protocol format
- Await human decision (accept/revise/request changes)

### Exit Criteria
- Human author has reviewed scene
- Any requested changes are made
- Human author marks scene as `revised`

### Outputs
- Review document (`.review.md` file or direct feedback)
- If changes made: updated scene file
- Update `drafts/manifest.json` with:
  ```json
  {
    "status": "revised"
  }
  ```

---

## Phase 4: Polishing (revised → polished)

### Entry Criteria
- Scene status is `revised`
- Major narrative and structural issues resolved
- Focus shifts to line-level craft

### Task Definition for AI Agent

#### Step 1: Line-Level Review
Read scene for:
- **Rhythm**: Sentence length variation, paragraph breathing
- **Precision**: Word choice, verb strength, adjective necessity
- **Clarity**: Ambiguous references, unclear antecedents
- **Consistency**: Tense, perspective, world details
- **Flow**: Transition smoothness, paragraph connections

#### Step 2: Micro-Revisions
Focus on:
- Replacing weak verbs (is/was/has) with active verbs
- Cutting unnecessary words (very, really, just, actually)
- Strengthening metaphors
- Varying sentence openings
- Improving sensory specificity
- Smoothing dialogue attribution
- Enhancing rhythm

#### Step 3: Final Voice Pass
Ensure voice consistency through:
- Reading aloud for rhythm
- Checking forbidden patterns haven't crept in
- Verifying thread-specific texture remains strong
- Confirming tense consistency

#### Step 4: Final Validation
Re-run validation scripts to ensure polishing didn't introduce issues:
```bash
python scripts/voice_validator.py [scene-path] --thread [thread] --pretty
python scripts/philosophy_checker.py [scene-path] --thread [thread] --pretty
```

### Exit Criteria
- Line-level revisions complete
- Voice validation passes
- Philosophy validation passes
- Scene is manuscript-ready quality

### Outputs
- Polished scene file
- Update `drafts/manifest.json` with:
  ```json
  {
    "status": "polished"
  }
  ```

---

## Phase 5: Finalization (polished → final)

### Entry Criteria
- Scene status is `polished`
- All validation scripts pass
- Human author approves for final manuscript

### Task Definition for AI Agent

#### Step 1: Final Consistency Check
Verify:
- Scene integrates with surrounding scenes
- Character details match established facts
- World details consistent with era
- Rhymes properly tracked in registry
- Genre markers appropriate

#### Step 2: Metadata Finalization
Ensure complete in `drafts/manifest.json`:
- Final word count
- All rhyming moments documented
- All validation checks recorded
- Any notes for future reference

#### Step 3: Archive Context
Move or update:
- Context file with complete history
- Validation outputs preserved
- Review notes archived

### Exit Criteria
- Scene is manuscript-ready
- All metadata is complete
- Context is archived

### Outputs
- Update `drafts/manifest.json` with:
  ```json
  {
    "status": "final"
  }
  ```
- Archived context and validation files

---

## Special Scenarios

### Scenario: Scene Handoff (Rhyme Continuation)

When a scene must catch a rhyme from a previous scene:

#### Detection
Check if:
- Previous scene in different thread has closing rhymes
- Movement tracking indicates rhyme handoff
- Manifest notes specify rhyme continuation

#### Action
1. Identify closing rhymes from previous scene
2. Use `--previous-closing` flag with rhyme tracker:
   ```bash
   python scripts/rhyme_tracker.py [scene-path] --previous-closing '["rhyme-1","rhyme-2"]' --pretty
   ```
3. Ensure new scene catches at least one of the rhymes
4. Intensity should match or slightly increase

#### Validation
- Rhyme tracker confirms rhyme caught
- Registry updated with handoff chain
- Movement tracking reflects continuation

### Scenario: Multi-Voice Scene (Movement 3+)

When scene contains multiple consciousness voices:

#### Additional Requirements
- Use `voices/quick-reference.md` for rapid context switching
- Track voice transitions explicitly
- Ensure each voice section passes validation independently

#### Validation Approach
1. Extract each voice section separately
2. Validate each section with appropriate thread flag
3. Verify transitions are clean (no voice bleed unless intentional)
4. Check Movement 3+ bleed patterns are appropriate

### Scenario: Validation Deadlock

If scene cannot pass validation after multiple attempts:

#### Diagnosis
1. Identify which validation consistently fails
2. Determine if issue is:
   - Voice contamination (rewrite with fresh voice reference)
   - Philosophy violation (reframe the approach)
   - Rhyme integration (choose different rhyme)
   - Genre mismatch (adjust markers)

#### Resolution Paths
1. **Voice Issues**: Start fresh paragraph using voice samples as templates
2. **Philosophy Issues**: Consult `protocols/philosophy-constraints.md` for alternatives
3. **Rhyme Issues**: Switch to rhyme with lower difficulty or different modality
4. **Genre Issues**: Review `scaffolding/genre-pressure.md` for thread-appropriate markers

#### Escalation
If resolution paths fail:
1. Document the specific conflict
2. Flag for human author decision
3. Propose alternative approaches
4. **Do NOT** force validation by lowering standards

### Scenario: Status Regression

If scene needs to move backwards in status:

#### Triggers
- Human author identifies major structural issue
- New narrative development requires scene rewrite
- Philosophy drift detected across multiple scenes

#### Process
1. Update `drafts/manifest.json` with:
   - New status (may regress to `draft`)
   - Note explaining reason for regression
   - Preserve previous validation results for reference
2. Re-enter lifecycle at appropriate phase
3. Apply lessons from previous iteration

---

## Agent Decision Tree

### For Creation Phase

```
START: Scene marked as "not_started"
  ↓
  ├─ All context files available?
  │  ├─ YES → Proceed to Context Assembly
  │  └─ NO → Flag missing files, request creation
  ↓
  ├─ Context Assembly complete?
  │  ├─ YES → Proceed to Pre-Draft Planning
  │  └─ NO → Request additional context
  ↓
  ├─ Planning complete?
  │  ├─ YES → Generate Draft
  │  └─ NO → Clarify narrative beats
  ↓
  ├─ Draft meets requirements?
  │  ├─ YES → Self-Review
  │  └─ NO → Revise draft
  ↓
  ├─ Self-Review passed?
  │  ├─ YES → Mark as "draft", proceed to Validation Phase
  │  └─ NO → Revise and repeat self-review
  ↓
END: Scene marked as "draft"
```

### For Validation Phase

```
START: Scene marked as "draft"
  ↓
  ├─ Environment configured?
  │  ├─ YES → Run Validation Scripts
  │  └─ NO → Set movement_config.json
  ↓
  ├─ Voice validation passed?
  │  ├─ YES → Continue
  │  └─ NO → Revise for voice, re-run voice validation
  ↓
  ├─ Rhyme validation passed?
  │  ├─ YES → Continue
  │  └─ NO → Adjust rhymes, re-run rhyme validation
  ↓
  ├─ Phrase validation passed?
  │  ├─ YES → Continue
  │  └─ NO → Fix phrase issues, re-run phrase validation
  ↓
  ├─ Philosophy validation passed?
  │  ├─ YES → Continue
  │  └─ NO → Revise philosophy, re-run philosophy validation
  ↓
  ├─ Genre validation passed?
  │  ├─ YES → Manual Validation
  │  └─ NO → Adjust genre markers, re-run genre validation
  ↓
  ├─ Manual validation passed?
  │  ├─ YES → Mark as "validated"
  │  └─ NO → Revise and repeat manual validation
  ↓
  ├─ All validations passed?
  │  ├─ YES → Mark as "validated", exit phase
  │  └─ NO → Return to appropriate revision step
  ↓
END: Scene marked as "validated"
```

### For Review Phase

```
START: Scene marked as "validated", human review requested
  ↓
  ├─ Load all context files
  ↓
  ├─ Perform structured analysis
  ↓
  ├─ Generate review using protocol format
  ↓
  ├─ Present review to human author
  ↓
  ├─ Human decision:
  │  ├─ Accept → Mark as "revised"
  │  ├─ Revise → Make changes, return to validation
  │  └─ Request changes → Implement, validate, re-submit
  ↓
END: Scene marked as "revised" or returned to earlier phase
```

---

## Integration with Existing Workflows

### Connection to drafting-workflow.md

This protocol provides **task-level structure** for the **status progression** defined in `drafting-workflow.md`:

- **Mode A (AI-Driven Drafting)** maps to Creation + Validation phases
- **Mode B (Human Review)** maps to Review phase
- Polishing and Finalization extend the workflow to completion

### Connection to validation scripts

All validation scripts are integrated into the Validation Phase:
- `voice_validator.py` - Checks tense, syntax, contamination
- `rhyme_tracker.py` - Verifies rhyme integration and handoffs
- `phrase_tracker.py` - Tracks key phrase bleeding between threads
- `philosophy_checker.py` - Enforces Four Shackles and philosophy constraints
- `genre_checker.py` - Validates genre markers and bleed patterns

### Connection to manifest.json

Scene lifecycle status is tracked in `drafts/manifest.json`:
```json
{
  "id": "m1-arch-01",
  "status": "not_started|draft|validated|revised|polished|final",
  "voice_check": "passed|failed|warn",
  "philosophy_check": "passed|failed|warn",
  "rhyme_check": "passed|failed|warn",
  "genre_check": "passed|failed|warn",
  "phrase_check": "passed|failed|warn"
}
```

---

## Best Practices

### For AI Agents

1. **Trust the Process**: Follow each phase completely before proceeding
2. **Don't Skip Validation**: Even if you're confident, run all scripts
3. **Iterate Gracefully**: Validation failures are normal; revise and retry
4. **Maintain Voice**: Voice consistency is the highest priority
5. **Document Context**: Keep detailed notes in `.context.md` files
6. **Respect Philosophy**: The Four Shackles are non-negotiable
7. **Preserve Quality**: Never lower standards to pass validation faster

### For Human Authors

1. **Trust the Validation**: If scripts pass, voice and philosophy are likely solid
2. **Focus on Narrative**: Use review phase for story and character issues
3. **Let Polish Be Polish**: Don't over-edit during early phases
4. **Update Manifest**: Keep status tracking current
5. **Preserve Context**: Context files are valuable for understanding choices

### For the Project

1. **Consistency**: All scenes follow same lifecycle for quality assurance
2. **Trackability**: Clear status enables progress monitoring
3. **Scalability**: Process works for any number of scenes/agents
4. **Quality**: Multiple validation layers ensure manuscript-ready output
5. **Flexibility**: Phases can be repeated or regressed as needed

---

## Quick Reference Card

| Phase | Entry Status | Exit Status | Key Actions | Critical Checks |
|-------|--------------|-------------|-------------|-----------------|
| **Creation** | not_started | draft | Assemble context, generate prose | Word count, self-review |
| **Validation** | draft | validated | Run 5 validation scripts, iterate | All scripts pass |
| **Review** | validated | revised | Structured analysis, feedback | Human approval |
| **Polishing** | revised | polished | Line-level edits, final pass | Voice & philosophy scripts |
| **Finalization** | polished | final | Consistency check, archive | Metadata complete |

---

## Version History

- **v1.0** (2026-01-24): Initial Scene Lifecycle Protocol definition
  - Established five-phase lifecycle
  - Integrated with existing validation scripts
  - Defined task structures for AI agents
  - Created decision trees and best practices
