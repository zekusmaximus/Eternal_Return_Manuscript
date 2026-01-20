# Manual Sync Protocol

Quick 2-minute routine to maintain consistency between manifest and working files.

## End-of-Session Checklist

Run this after any drafting or revision session:

### 1. Update manifest.json
- [ ] Set scene `status` to current state (draft, voice_pass, etc.)
- [ ] Record approximate `actual_words` for scenes touched
- [ ] Update `voice_check` and `philosophy_check` states if checks were run
- [ ] Update movement-level `actual_words` totals

### 2. Update rhyming moments registry
- [ ] If you identified or wrote a rhyming moment, add its occurrence to the `rhyming_moments` section
- [ ] Verify the `rhyming_moments` array in the scene entry lists the correct IDs

### 3. Optional: Update progress.md
- [ ] One-line session log entry
- [ ] Update scene status table if major milestones reached

## Notes

- This protocol takes ~2 minutes per session
- Manifest is canonical; progress.md is optional/informational
- Scene file frontmatter does not need to match manifest (manifest is truth)
