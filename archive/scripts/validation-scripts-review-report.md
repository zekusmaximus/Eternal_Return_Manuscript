# Validation Scripts Review Report — Movement Two (Cycle 1)

## 1. Executive Summary

Overall, the scripts correctly avoid false **Four Shackles** positives but struggle with Movement Two’s braided requirements: cross-scene handoffs, intentional contamination, and pharmakon detection. The most critical issues are **false negatives in pharmakon detection**, **lack of automatic rhyme handoff validation**, and **over-penalization of intentional contamination in the Algorithm scene**. Usability is decent but outputs can grow large and are at risk of truncation without an explicit summary mode.

**Top critical issues:**
1. Philosophy checker misses explicit poison/cure passages and intensity-recognition language.
2. Rhyme tracker does not validate handoff sequence across scenes by default.
3. Voice validator flags Cycle 1 Algorithm scene as over-contaminated and too short in syntax without intensity-segment awareness.

## 2. Script-by-Script Analysis

### A) Genre Checker (scripts/genre_checker.py)

**Current State**
- Regex-based genre marker scanning per thread, plus cross-thread bleed detection.
- Uses cycle-based bleed tolerance from movement_config.json.
- Output: JSON with marker counts, bleed detection, and an intensity assessment.

**Test Results**
- Archaeologist scene: **Pass**, light bleed within tolerance. Markers found but limited to two categories. Example marker occurrence: cold-hands + server-room atmosphere in [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L7).
- Algorithm scene: **Warn** due to heavy bleed (14 markers) against Cycle 1 tolerance. Example of strong archaeologist bleed: “Cold hands. Server room chill...” in [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L71).
- Last Human scene: **Warn** due to bleed from archaeologist markers; likely false positives driven by broad economic markers and general “decay” language. Example: pharmakon paragraph flagged as economic predation in [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L183).

**Effectiveness Rating**
- Accuracy: 6/10
- Movement Two Awareness: 5/10
- Completeness: 6/10
- Usability: 7/10

**Specific Issues**
- **False positives** on economic markers when “cost/price” is used metaphorically (e.g., “The cost accrues” in [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L121)).
- **Bleed inflation** due to generic words (cold, cost, decay) which overlap genre vocab but are not necessarily cross-genre in context.

**Recommended Improvements**
- Restrict economic markers to monetary context (collocations like “fee/cost/price/payment” within 3–5 words of “integration/contract/client”).
- Add explicit “intensity moment” allowance for Cycle 1 where bleed is expected (rather than strict totals across the whole scene).

---

### B) Philosophy Checker (scripts/philosophy_checker.py)

**Current State**
- Detects Four Shackles violations, forbidden narrative moves, positive philosophical markers, and pharmakon balance.
- Pharmakon detection is rule-based and thread-specific.

**Test Results**
- **Shackles:** no violations detected across all three scenes (correct).
- **False negatives in pharmakon detection:**
  - Archaeologist explicitly states poison and cure but `check_pharmakon` still warns. Example: “The same poison… is curing…” in [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L252).
  - Algorithm explicitly names pharmakon and poison/cure but still warns. Example: “The pharmakon operates…” in [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L293).
- **Intensity-recognition marker miss:** “Recognition as intensity…” not captured by current patterns in [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L13).
- **Forbidden move not flagged:** “sending consciousness backward through time” in [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L153) should be flagged or at least warned as transmission framing.

**Effectiveness Rating**
- Accuracy: 6/10
- Movement Two Awareness: 6/10
- Completeness: 5/10
- Usability: 7/10

**Specific Issues**
- Pharmakon detection relies on a narrow set of named entities (Lena, Marcus, etc.) and misses strong textual signals.
- Positive marker detection for intensity recognition is too literal.
- Forbidden move patterns are too narrow and miss “sending consciousness backward” phrasing.

**Recommended Improvements**
- Add a more flexible poison/cure lexicon and allow local-window co-occurrence (e.g., poison/cure within 1–2 sentences).
- Expand intensity recognition patterns to include “recognition as intensity” style phrasing.
- Add transmission patterns that include “sending consciousness backward through time” and “transmitting awareness across temporal distance.”

---

### C) Rhyme Tracker (scripts/rhyme_tracker.py)

**Current State**
- Regex marker detection across full text, with opening/closing zones defined by word counts.
- Optional handoff validation via `--previous-closing` list.

**Test Results**
- Archaeologist scene: **Pass** (4 rhymes; opening `cold-hands` at line 7, closing `bone-frequency` at line 260). See [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L7) and [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L260).
- Algorithm scene: **Pass** (4 rhymes; opens with `bone-frequency` line 5, closes with `cold-hands` line 281). See [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L5) and [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L281).
- Last Human scene: **Warn** (5 rhymes; exceeds Cycle 1 max of 4). See [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L3).
- Handoff validation **skipped** because no previous closing rhymes were provided.

**Effectiveness Rating**
- Accuracy: 7/10
- Movement Two Awareness: 5/10
- Completeness: 5/10
- Usability: 6/10

**Specific Issues**
- No automated chaining across the three scene files, so handoff validation is not performed unless user supplies `--previous-closing` manually.
- Opening/closing zones are fixed at 500 words, while the spec expects “first/last 2–3 paragraphs.”

**Recommended Improvements**
- Add a mode to read multiple scenes and validate handoffs automatically (manifest-driven or folder-driven).
- Allow configurable opening/closing zones in paragraphs or percent-of-scene length.

---

### D) Voice Validator (scripts/voice_validator.py)

**Current State**
- Voice signature checks + contamination markers + syntax metrics.
- Contamination limits defined by cycle.

**Test Results**
- Archaeologist scene: **Pass**; contamination within budget (3). Algorithm bleed is detected in bleed segments (e.g., log-style inserts around lines 185–189 in [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L185)).
- Algorithm scene: **Warn**; contamination 17 (over Cycle 1 max) and average sentence length below expected (9.9 vs ≥15). The scene has heavy, intentional bleed and shorter sentences that may be intensity-driven but penalized globally.
- Last Human scene: **Pass**; contamination 1, within budget.

**Effectiveness Rating**
- Accuracy: 6/10
- Movement Two Awareness: 6/10
- Completeness: 6/10
- Usability: 7/10

**Specific Issues**
- Scene-level contamination scoring penalizes **intensity passages** that are supposed to bleed in Cycle 1, especially in the Algorithm thread.
- Syntax scoring doesn’t distinguish between baseline vs. bleed segments.

**Recommended Improvements**
- Add intensity-segment detection (based on bleed markers like “bleed,” “frequency,” “panic,” etc.) and score contamination per segment.
- Normalize contamination to words per 1,000 and allow short-sentence bursts during flagged intensity segments.

---

## 3. Cross-Validation Findings

### Rhyme Handoffs (Manual)
- Archaeologist closes with `bone-frequency` (line 260) → Algorithm opens with `bone-frequency` (line 5). Handoff succeeds. See [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L260) and [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L5).
- Algorithm closes with `cold-hands` (line 281) → Last Human opens with `cold-hands` (line 3). Handoff succeeds. See [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L281) and [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L3).
- Last Human closes with `tracing-the-form` (line 237), which matches the expected handoff to Arch Cycle 2 per braiding spec. See [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L237).

### Voice Contamination
- Archaeologist bleed is algorithmic and localized (log inserts), appropriate for Cycle 1. Example bleed at [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L185).
- Algorithm has extensive Archaeologist sensory bleed, likely beyond Cycle 1 expectations. Example: [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L71).
- Last Human shows light Algorithm contamination at an intensity moment (line 61), which fits Cycle 1. See [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L61).

### Genre Bleed
- Algorithm scene contains strong corporate-gothic bleed (“server room chill,” etc.) beyond Cycle 1 tolerance. See [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L71).
- Last Human scene contains bleed flagged by economic markers; likely a false positive due to general “pharmakon” language. See [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L183).

### Philosophy Validation
- No shackle violations detected.
- Pharmakon is explicitly present in all scenes but is **not recognized** by `check_pharmakon` (false negatives). Examples: [drafts/movement-two/archaeologist/scenes/scene-01.md](drafts/movement-two/archaeologist/scenes/scene-01.md#L252), [drafts/movement-two/algorithm/scenes/scene-01.md](drafts/movement-two/algorithm/scenes/scene-01.md#L293), [drafts/movement-two/last-human/scenes/scene-01.md](drafts/movement-two/last-human/scenes/scene-01.md#L183).

## 4. Missing Validations

- [ ] Cross-scene phrase bleeding validation (phrase_tracker exists but is not integrated into the main test workflow)
- [ ] Intensity moment detection (so contamination is assessed in correct context)
- [ ] Mutual bleed patterns (bidirectional contamination per cycle)
- [ ] Scene position validation based on paragraph zones (not just word counts)
- [ ] Automated cycle progression rules across scenes
- [ ] Phantasm connection checks (geometric form presence by cycle)
- [ ] Temporal marker consistency (AM/PM vs. cycle timestamp coherence)

## 5. Truncation Analysis

**Problem**: Outputs can become long (multiple occurrences, long JSON). Running in a standard terminal with `--pretty` risks truncation when scenes scale up.

**Root Causes Identified**
- Each script outputs full `occurrences` arrays with text previews.
- No built-in pagination or summary mode.

**Solutions**
- Add `--summary` mode (counts only, no occurrences)
- Add `--max-occurrences N` (cap per category)
- Add `--output-file` to reduce terminal load
- Provide a compact human-readable summary block above JSON

## 6. Priority Improvements (Ranked)

**High Priority**
1. Fix pharmakon detection false negatives in `check_pharmakon`.
2. Add automatic cross-scene handoff validation in rhyme tracker.
3. Make voice contamination scoring intensity-aware (segment-based).

**Medium Priority**
1. Reduce genre bleed false positives by tightening economic/decay markers.
2. Integrate phrase tracking into the default Movement Two validation workflow.
3. Expand intensity-recognition pattern detection.

**Low Priority**
1. Add summary-only output mode and configurable verbosity.
2. Make opening/closing zones configurable by paragraphs or percentage.
3. Add per-script `--config` override for experiments without editing movement_config.json.

## 7. Implementation Suggestions

### 7.1 Fix Pharmakon Detection
**Issue**: `check_pharmakon` misses explicit poison/cure language even when present.

**Current Code Location**: `check_pharmakon` in [scripts/philosophy_checker.py](scripts/philosophy_checker.py#L291).

**Proposed Solution**:
- Add a general poison/cure lexicon and detect co-occurrence within a window of 1–2 sentences.
- Allow a “pharmakon” keyword to trigger balanced status if both loss and gain verbs appear in nearby context.

**Testing Approach**:
- Re-run on the three scene files; verify poison/cure balance is detected in the lines cited above.

---

### 7.2 Add Cross-Scene Handoff Validation
**Issue**: `rhyme_tracker.py` only validates handoff if `--previous-closing` is manually supplied.

**Current Code Location**: `validate_rhymes` in [scripts/rhyme_tracker.py](scripts/rhyme_tracker.py#L386).

**Proposed Solution**:
- Add a `--sequence` mode that accepts a list of files (or reads drafts/manifest.json) and auto-passes each scene’s closing rhymes into the next scene’s opening check.
- Add per-thread order rules based on Movement Two braiding spec.

**Testing Approach**:
- Run against the three scene-01 files and verify handoffs are auto-validated.

---

### 7.3 Make Voice Contamination Intensity-Aware
**Issue**: Algorithm scene flagged as over-contaminated because contamination is counted across the entire scene.

**Current Code Location**: `detect_contamination` and `assess_contamination` in [scripts/voice_validator.py](scripts/voice_validator.py#L164).

**Proposed Solution**:
- Add an intensity detector (regex for “bleed,” “panic,” “frequency,” “resonance,” “dream”) to identify segments.
- Score contamination separately inside intensity segments (Cycle 1 allowed) vs. outside (Cycle 1 strict).

**Testing Approach**:
- Re-run on the Algorithm scene and verify contamination warnings are limited to non-intensity sections.

---

### 7.4 Tighten Genre Marker Context
**Issue**: Genre bleed is inflated by generic words like “cost,” “poor,” and “decay.”

**Current Code Location**: `GENRE_MARKERS` in [scripts/genre_checker.py](scripts/genre_checker.py#L37).

**Proposed Solution**:
- Constrain economic markers to monetary context (e.g., `cost` near `fee/price/contract/integration`).
- Add a “semantic whitelist” that exempts uses of `cost` in abstract or thermodynamic contexts.

**Testing Approach**:
- Re-run Algorithm and Last Human scenes; confirm bleed count drops while true genre markers remain.

---

## Appendix: Test Artifacts

Outputs were captured in scripts/validation-outputs/*.json for all 12 script runs.
