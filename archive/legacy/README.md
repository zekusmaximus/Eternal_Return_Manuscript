# .archive Directory

This directory contains archived files that have been superseded by newer implementations.

## Contents

### claude-legacy/

**Archived**: 2026-01-20
**Reason**: Superseded by agent-agnostic `protocols/` directory

The `.claude/` directory contained Claude-specific configuration files:

- `CLAUDE.md` - Project instructions (now superseded by `protocols/drafting-workflow.md`)
- `commands.md` - Slash commands (now superseded by validation scripts in `scripts/`)
- `revision-workflow.md` - Revision system (now superseded by `protocols/drafting-workflow.md`)
- `project-rules.md` - Constraints (now in `protocols/philosophy-constraints.md`)
- `templates/` - File templates

These files may still be useful as reference material but are no longer the primary workflow documents.
