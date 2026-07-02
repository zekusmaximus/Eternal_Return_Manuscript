# Validation Script Review and Optimization Task

## OBJECTIVE
Test the Movement Two validation scripts against completed scene-01 files for all three threads (archaeologist, algorithm, last-human), then compile a comprehensive report with improvement recommendations.

## CRITICAL CONTEXT

**What Has Been Completed:**
- Movement One: All scenes finalized
- Movement Two Cycle 1: scene-01.md completed for archaeologist, algorithm, and last-human threads
- Location: `drafts/movement-two/{thread}/scenes/scene-01.md`

**Scripts to Test:**
- `scripts/genre_checker.py` - Validates genre markers with cycle-aware bleed tolerance
- `scripts/philosophy_checker.py` - Validates against Four Shackles, checks pharmakon
- `scripts/rhyme_tracker.py` - Tracks sensory rhyme usage with position awareness
- `scripts/voice_validator.py` - Validates voice with controlled contamination awareness
- `scripts/movement_config.json` - Unified configuration for all scripts

**Key Configuration:**
- Current state: Movement Two, Cycle 1
- Contamination tolerance: LOW (intensity moments only, 1-3 instances expected)
- Rhyme requirements: 2-4 rhymes per scene, opening and closing rhymes REQUIRED
- Voice contamination: Allowed during intensity moments only

## PHASE 1: UNDERSTAND THE PROJECT

### Read These Files to Understand Goals (in this order):

1. **Primary Framework:**
   - `research/framework.md` - Core philosophical framework (Deleuze, Klossowski, Heidegger, Stiegler)
   - `Notes.md` - Project overview, three consciousnesses, dramatic questions
   
2. **Movement Two Specifications:**
   - `scaffolding/movement-two-braiding.md` - How Movement Two differs from One, braiding mechanics
   - `scaffolding/movement-two-prep.md` (if exists) - Additional preparation notes
   
3. **Voice and Genre Guidelines:**
   - `voices/archaeologist.md` - Archaeologist voice patterns
   - `voices/algorithm.md` - Algorithm voice patterns
   - `voices/last-human.md` - Last Human voice patterns
   - `voices/quick-reference.md` - Voice comparison table
   - `scaffolding/genre-pressure.md` - Genre definitions and bleed mechanics
   
4. **Rhyme System:**
   - `scaffolding/rhymes/registry.md` - All sensory rhymes with metadata and usage tracking
   - `scaffolding/rhymes/movement-tracking.md` (if exists) - Movement-specific rhyme guidance
   
5. **Worldbuilding Context:**
   - `worldbuilding/near-future.md` - Archaeologist's era
   - `worldbuilding/mid-future.md` - Algorithm's era
   - `worldbuilding/deep-future.md` - Last Human's era
   - `worldbuilding/Phantasm.md` - The geometric form at the center of the entanglement

### Key Concepts to Understand:

**The Four Shackles (what scripts MUST catch):**
1. **Identity** - Collapsing difference into sameness ("they're the same person")
2. **Opposition** - Human/AI or flesh/digital binaries
3. **Resemblance** - "This reminds me of..." comparisons
4. **Analogy** - "This functions like that" structural parallels

**The Pharmakon (what scripts should recognize):**
- Poison AND cure aspects shown simultaneously
- The entanglement both destroying and completing them
- Not a balance, but dual operation

**Movement Two Braiding Mechanics:**
- Rhymes must HANDOFF: end of one scene → opening of next scene in different thread
- Voice contamination is INTENTIONAL: characters beginning to bleed into each other
- Genre bleed escalates through cycles: Cycle 1 (subtle), Cycle 2 (contamination begins), Cycle 3 (pervasive)

**Phrase Tracking:**
- Core phrases: "I find myself," "I find myself found," "The form is what makes self-observation possible"
- These should BEGIN CROSSING threads in Movement Two

## PHASE 2: RUN THE VALIDATION SCRIPTS

### For Each Scene-01 File (3 total):

**Archaeologist:**
```bash
cd scripts
python genre_checker.py ../drafts/movement-two/archaeologist/scenes/scene-01.md --thread archaeologist
python philosophy_checker.py ../drafts/movement-two/archaeologist/scenes/scene-01.md
python rhyme_tracker.py ../drafts/movement-two/archaeologist/scenes/scene-01.md
python voice_validator.py ../drafts/movement-two/archaeologist/scenes/scene-01.md --thread archaeologist
```

**Algorithm:**
```bash
cd scripts
python genre_checker.py ../drafts/movement-two/algorithm/scenes/scene-01.md --thread algorithm
python philosophy_checker.py ../drafts/movement-two/algorithm/scenes/scene-01.md
python rhyme_tracker.py ../drafts/movement-two/algorithm/scenes/scene-01.md
python voice_validator.py ../drafts/movement-two/algorithm/scenes/scene-01.md --thread algorithm
```

**Last Human:**
```bash
cd scripts
python genre_checker.py ../drafts/movement-two/last-human/scenes/scene-01.md --thread last_human
python philosophy_checker.py ../drafts/movement-two/last-human/scenes/scene-01.md
python rhyme_tracker.py ../drafts/movement-two/last-human/scenes/scene-01.md
python voice_validator.py ../drafts/movement-two/last-human/scenes/scene-01.md --thread last_human
```

### Critical Testing Notes:

**If you get Python errors:**
- Configure the Python environment first using appropriate tools
- Install dependencies if needed (check for requirements.txt or imports in scripts)

**About Truncated Responses:**
- If script output is getting cut off, this might be due to:
  1. JSON output being too large for terminal display
  2. Scripts not implementing pagination or summary modes
  3. Verbose regex match reporting
- Document where truncation occurs and suggest solutions

**Expected vs. Actual:**
- Scripts should validate against Movement Two Cycle 1 expectations
- Cross-reference findings with `movement_config.json` tolerances
- Check if scripts properly handle the intentional contamination that Movement Two requires

## PHASE 3: CROSS-VALIDATION ANALYSIS

### Rhyme Handoffs (Critical for Movement Two):

The scene-01 files were written to establish the braiding pattern. Check:

1. **Closing Rhymes:** What rhyme(s) does each scene-01 END with?
   - Read the last 2-3 paragraphs of each scene-01.md
   - Identify which rhymes are "released" for the next thread to catch
   
2. **Opening Rhymes:** What rhyme(s) does each scene-01 OPEN with?
   - Read the first 2-3 paragraphs of each scene-01.md
   - Identify which rhymes are "caught" from a previous thread

3. **Handoff Validation:**
   - Does `rhyme_tracker.py` properly identify these position-aware rhymes?
   - Does it flag when a closing rhyme from one thread appears as an opening rhyme in another?
   - Does it validate the handoff sequence?

**Expected Pattern (you must verify this):**
```
archaeologist scene-01 ENDS with: [rhyme X]
  ↓
algorithm scene-01 OPENS with: [rhyme X variation]
  ↓
algorithm scene-01 ENDS with: [rhyme Y]
  ↓
last-human scene-01 OPENS with: [rhyme Y variation]
  ↓
last-human scene-01 ENDS with: [rhyme Z]
  ↓
(loops back or forward to next cycle)
```

### Voice Contamination Validation:

Movement Two requires INTENTIONAL voice bleeding. For each scene-01:

1. Identify passages of high intensity (recognition moments, bleed experiences)
2. Check if voice contamination occurs during these moments
3. Verify if `voice_validator.py` properly distinguishes between:
   - **Intentional contamination** (feature): During intensity moments, appropriate to cycle
   - **Unintentional bleed** (bug): Voice drift in normal passages

### Genre Bleed Assessment:

For Cycle 1, genre should be DISTINCT with only subtle echoes. Check:

1. Does each thread maintain its primary genre? (Corporate Gothic, Existential Horror, Cosmic Pastoral)
2. Are there moments where genre bleeds during intensity passages?
3. Does `genre_checker.py` properly flag unexpected genre crossover vs. allow intentional echoes?

### Philosophy Validation:

Most critical: The Four Shackles must be avoided. Check:

1. Does any scene-01 make identity claims? ("They are the same person")
2. Are there binary oppositions? (human vs. machine)
3. Are there resemblance comparisons? ("This reminds him of...")
4. Are there analogical structures? ("The Algorithm is like...")

**Pharmakon Check:**
- Do scenes show BOTH poison and cure aspects of the entanglement?
- Example: Algorithm's efficiency loss (poison) + deeper awareness (cure)
- Does `philosophy_checker.py` recognize dual operation or just flag violations?

## PHASE 4: MEASURE EFFECTIVENESS

### For Each Script, Assess:

1. **Accuracy:**
   - Are the detected patterns actually present in the text?
   - Are there false positives (flagging things that are actually correct)?
   - Are there false negatives (missing things that should be flagged)?

2. **Movement Two Awareness:**
   - Do scripts account for intentional contamination in M2?
   - Do they reference `movement_config.json` correctly?
   - Do tolerances match the braiding mechanics described in scaffolding files?

3. **Completeness:**
   - Are there important patterns the scripts don't check?
   - Do scripts validate the handoff mechanics described in `movement-two-braiding.md`?
   - Do they track the escalation structure (Cycle 1 → 2 → 3)?

4. **Usability:**
   - Is the output clear and actionable for a writer?
   - Is the JSON format helpful or should there be a human-readable summary?
   - Are error messages informative?
   - **Truncation issues:** Where does output get cut off and why?

5. **Coverage Gaps:**
   - **Phrase tracking:** Do scripts monitor "I find myself" / "I find myself found" / "The form is what makes self-observation possible"?
   - **Mutual bleed validation:** Do scripts recognize when contamination is MUTUAL (two voices bleeding into each other)?
   - **Intensity moment detection:** Can scripts identify when intensity peaks occur?

## PHASE 5: COMPILE REPORT

### Required Report Sections:

#### 1. Executive Summary
- Overall assessment of script effectiveness
- Most critical issues found
- Priority recommendations

#### 2. Script-by-Script Analysis

For each script (`genre_checker.py`, `philosophy_checker.py`, `rhyme_tracker.py`, `voice_validator.py`):

**Current State:**
- What it checks for
- Configuration dependencies
- Output format

**Test Results:**
- What it correctly identified in scene-01 files
- What it missed (false negatives)
- What it incorrectly flagged (false positives)

**Effectiveness Rating:** (1-10 scale)
- Accuracy: __/10
- Movement Two Awareness: __/10
- Completeness: __/10
- Usability: __/10

**Specific Issues:**
- List concrete problems with examples from test runs
- Note any truncation issues and where they occur

**Recommended Improvements:**
- Prioritized list of enhancements
- Code-level suggestions where appropriate
- Configuration adjustments needed

#### 3. Cross-Validation Findings

**Rhyme Handoffs:**
- Map the actual handoff pattern found in scene-01 files
- Assess whether `rhyme_tracker.py` validates this correctly
- Gaps in handoff detection

**Voice Contamination:**
- Intensity moments where contamination occurs
- Whether contamination is appropriate for Cycle 1
- Script's ability to distinguish intentional vs. unintentional bleed

**Genre Bleed:**
- Where genre crosses boundaries
- Whether bleed is appropriate for Cycle 1
- Script's tolerance settings vs. actual requirements

**Philosophy Validation:**
- Any Shackle violations found
- Pharmakon assessment (dual operation shown?)
- Recommendation quality

#### 4. Missing Validations

What should be checked but isn't currently:

- [ ] Core phrase tracking across threads
- [ ] Intensity moment detection
- [ ] Mutual bleed patterns (bidirectional contamination)
- [ ] Scene position validation (opening/closing rhymes)
- [ ] Cycle progression rules
- [ ] Character-specific phantasm connection
- [ ] Temporal marker consistency
- [ ] (Add others as discovered)

#### 5. Truncation Analysis

**Problem:**
- Users report responses often get truncated
- Where does this occur in script output?
- Is it JSON length? Verbose regex matches? List overflow?

**Root Causes Identified:**
- (Document specific truncation points)

**Solutions:**
- Implement summary modes
- Add pagination for long outputs
- Reduce verbosity in match reporting
- Create human-readable summaries separate from full JSON
- (Other solutions as appropriate)

#### 6. Priority Improvements (Ranked)

**High Priority:**
1. [Most critical improvement with rationale]
2. [Second most critical]
3. ...

**Medium Priority:**
1. [Important but not blocking]
2. ...

**Low Priority:**
1. [Nice to have enhancements]
2. ...

#### 7. Implementation Suggestions

For each high-priority improvement:

**Issue:** [Specific problem]

**Current Code Location:** [File and function/section]

**Proposed Solution:** 
```python
# Pseudocode or actual code suggestion
```

**Testing Approach:** [How to verify the fix works]

---

## DELIVERABLE FORMAT

Create a markdown file named `validation-scripts-review-report.md` in the `scripts/` directory with all sections above completed.

**Report Requirements:**
- Concrete examples from actual test runs
- Specific line numbers and passages when citing issues
- Code-level recommendations where appropriate
- Clear prioritization based on Movement Two needs
- Solutions to truncation problems

**Style:**
- Technical but readable
- Focus on actionable improvements
- Include both "what's wrong" and "how to fix it"
- Cross-reference project documentation files

---

## EXECUTION NOTES

**Approach:**
1. Don't rush through the context reading - understanding the project framework is critical
2. Actually run all the scripts and capture full output
3. Read the scene-01 files carefully to understand what writers are trying to achieve
4. Compare script validation against the documented goals in scaffolding files
5. Be specific about what works and what doesn't

**Common Pitfalls to Avoid:**
- Don't just summarize what scripts do - TEST them
- Don't assume scripts are correct - validate against the actual prose and project goals
- Don't ignore the truncation issue - this is a real problem to solve
- Don't forget Movement Two is about INTENTIONAL contamination - scripts must distinguish this

**Success Criteria:**
- Report enables immediate improvement of validation scripts
- Truncation problems identified and solutions proposed
- Clear understanding of gaps between current validation and Movement Two requirements
- Specific, actionable recommendations with implementation guidance

---

## TECHNICAL TROUBLESHOOTING

**If Python environment needs setup:**
- Configure environment using available tools
- Install dependencies as needed
- Note any missing requirements in report

**If scripts fail to run:**
- Document the error
- Check if issue is in script code or environment
- Suggest fixes

**If output is unclear:**
- Note this as a usability issue
- Suggest output format improvements

**If you need to modify movement_config.json for testing:**
- Document what you changed and why
- Restore original values after testing
- Note if config structure needs improvement

---

## FINAL CHECKLIST

Before submitting report, verify you have:

- [ ] Read all required context files
- [ ] Run all 4 scripts against all 3 scene-01 files (12 total test runs)
- [ ] Analyzed rhyme handoff patterns manually
- [ ] Identified voice contamination moments
- [ ] Checked for Shackle violations
- [ ] Documented truncation issues specifically
- [ ] Provided effectiveness ratings for each script
- [ ] Listed missing validations
- [ ] Prioritized improvements
- [ ] Included implementation suggestions for high-priority items
- [ ] Created report in `scripts/validation-scripts-review-report.md`

**The goal:** Enable the author to make the validation scripts truly effective for Movement Two's braided narrative structure.
