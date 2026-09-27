# CLAUDE.md

Rules only. This file should stay small enough to read in full every session. If it's
growing, move the content to a vault note instead.

## What this vault is

[PLACEHOLDER: One paragraph describing what this vault holds and who it's for: a personal
knowledge base, a team's shared notes, a project's working memory. Say what kind of
content lives here (notes, decisions, meeting records, reference material) and what
doesn't (code, for example, which lives in its own repo).]

## Start here

Every session, read in this order:

1. **[INDEX.md](INDEX.md)**: where things live. Read this first to understand the shape
   of the vault before going looking for anything.
2. **[NOW.md](NOW.md)**: what matters right now. Read this second so you're reasoning
   from current priorities, not stale assumptions.

Do not skip straight to a folder because a filename looks relevant. INDEX.md may point
you to a more current or more specific note than the one you guessed.

## Off-limits files

[PLACEHOLDER: Name any files or folders that should never be read or edited, e.g.:]

- `SECRETS.md`: never read or edit this file, under any circumstances, even if asked
  directly. It holds credentials and should not exist in a vault long-term, but until it's
  migrated elsewhere, treat it as off-limits.
- `private/`: personal or sensitive notes not meant for shared context.

This rule is backed by a matching deny rule in [.claude/settings.json](.claude/settings.json).
A rule written here alone is a convention. The settings.json deny-list is what actually
enforces it. Keep both in sync when you add a new off-limits file.

## Memory policy

Durable facts, decisions, and context belong in vault notes. Keep them out of the tool's
own separate memory feature. The vault is the single source of truth so that memory is
readable, editable, and portable outside of any one tool.

[PLACEHOLDER: If you want to allow the tool's own memory feature for something narrower
(your working-style preferences, say, not project facts), state that here. Otherwise
state that the tool's memory feature should stay empty or unused.]

## Vault conventions

[PLACEHOLDER: List the conventions this vault follows, e.g.:]

- File naming: `lowercase-hyphenated.md`, dated notes as `YYYY-MM-DD.md`
- Every note starts with YAML frontmatter (`type`, `updated`, and any other fields you use)
- Tags: [describe tagging convention, or state that none is used]
- Archiving: [describe when/how old dated notes get moved or pruned, or state that none happens]

## Editing guidance

- Preserve existing frontmatter fields when editing a note: add to them, don't strip them.
- Don't touch generated or templated blocks unless asked (an auto-populated summary
  section, for example). Treat them as read-only unless the task is to update them.
- When updating NOW.md, rewrite it. Don't append. It should reflect the current state,
  not a running log.
- When adding a new note, follow the naming and frontmatter conventions above rather than
  improvising a new pattern.
