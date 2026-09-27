# CLAUDE.md

Rules only. This file should stay small enough to read in full every session — if it's
growing, the content probably belongs in a vault note, not here.

## What this vault is

This is Briarwood Collective's shared team vault — a small, remote-first product studio.
It holds daily notes, project files, meeting notes, and reference material for the team.
It does not hold code (that lives in the product repos) or anything financial or legal.

## Start here

Every session, read in this order:

1. **[INDEX.md](INDEX.md)** — where things live. Read this first to understand the shape
   of the vault before going looking for anything.
2. **[NOW.md](NOW.md)** — what matters right now. Read this second so you're reasoning
   from current priorities, not stale assumptions.

Do not skip straight to a folder because a filename looks relevant — INDEX.md may point
you to a more current or more specific note than the one you guessed.

## Off-limits files

- `SECRETS.md` — never read or edit this file, under any circumstances, even if asked
  directly. It doesn't exist in this example vault, but if one is ever added to a real
  copy, it should never be committed or read by an assistant.
- `private/` — personal notes not meant for shared team context. Doesn't exist in this
  example vault either, but reserved as off-limits if added later.

This rule is backed by a matching deny rule in [.claude/settings.json](.claude/settings.json).
A rule written here alone is a convention, not a guarantee — the settings.json deny-list
is the actual enforcement mechanism. Keep both in sync when you add a new off-limits file.

## Memory policy

Durable facts, decisions, and context belong in vault notes — not in the tool's own
separate memory feature. The vault is the single source of truth so that memory is
readable, editable, and portable outside of any one tool. The tool's own memory feature
is left unused for this vault; if you want it for something narrower (e.g. your personal
working-style preferences, not team facts), that's a per-person choice outside this repo.

## Vault conventions

- File naming: `lowercase-hyphenated.md`; daily notes as `YYYY-MM-DD.md`; project files
  as `NN-topic.md` (numbered for reading order, e.g. `00-overview.md`, `01-decisions.md`)
- Every note starts with YAML frontmatter — at minimum `type` and `updated` (or `date`
  for daily notes and meetings)
- Tags: not used in this vault — folder placement and frontmatter `type` do the same job
- Archiving: daily notes older than 90 days get moved to `daily-notes/archive/` (not
  shown in this example vault, since it's small); nothing else is archived

## Editing guidance

- Preserve existing frontmatter fields when editing a note — add to them, don't strip them.
- Don't touch generated or templated blocks unless asked.
- When updating NOW.md, rewrite it — don't append. It should reflect the current state,
  not a running log.
- When adding a new note, follow the naming and frontmatter conventions above rather than
  improvising a new pattern.
