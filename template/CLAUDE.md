# CLAUDE.md

Rules only. This file should stay small enough to read in full every session. If it's
growing, move the content to a vault note instead.

## What this vault is

[PLACEHOLDER: One paragraph describing what this vault holds and who it's for: a personal
knowledge base, a team's shared notes, a project's working memory. Say what kind of
content lives here (notes, decisions, meeting records, reference material) and what
doesn't (code, for example, which lives in its own repo).]

## Start here

Claude Code loads this file at the start of every session, and these two imports load
the other two files with it:

@INDEX.md
@NOW.md

- **[INDEX.md](INDEX.md)**: where things live. Use it to understand the shape of the
  vault before going looking for anything.
- **[NOW.md](NOW.md)**: what matters right now. Check its `updated:` date, and say so if
  it looks stale rather than reasoning from old priorities.

A tool that doesn't support `@` imports should read INDEX.md, then NOW.md, before
anything else.

Do not skip straight to a folder because a filename looks relevant. INDEX.md may point
you to a more current or more specific note than the one you guessed.

## Off-limits files

[PLACEHOLDER: Name any files or folders that should never be read or edited, e.g.:]

- `SECRETS.md`: never read or edit this file, under any circumstances, even if asked
  directly. It holds credentials and should not exist in a vault long-term, but until it's
  migrated elsewhere, treat it as off-limits.
- `private/`: personal or sensitive notes not meant for shared context.

This rule is backed by a matching deny rule in [.claude/settings.json](.claude/settings.json).
A rule written here alone is a convention. The deny rule is what enforces it, for Claude
Code's file tools and shell commands that name the file; the sandbox (`/sandbox`) covers
indirect reads like `grep -r`. Keep both in sync when you add a new off-limits file.

## Memory policy

Durable facts, decisions, and context belong in vault notes. Keep them out of the tool's
own separate memory feature. The vault is the single source of truth so that memory is
readable, editable, and portable outside of any one tool.

Claude Code's own auto memory is switched off for this vault by `"autoMemoryEnabled": false`
in [.claude/settings.json](.claude/settings.json).

[PLACEHOLDER: If you want auto memory for something narrower (your working-style
preferences, say, not project facts), set that key to `true` and state what it's for here.
Otherwise delete this placeholder.]

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
