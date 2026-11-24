# CLAUDE.md

Rules only. This file should stay small enough to read in full every session — if it's
growing, the content probably belongs in a vault note, not here.

## What this vault is

This is Briarwood Collective's shared team vault — a small, remote-first product studio.
It holds daily notes, project files, meeting notes, and reference material for the team.
It does not hold code (that lives in the product repos) or anything financial or legal.

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

Do not skip straight to a folder because a filename looks relevant — INDEX.md may point
you to a more current or more specific note than the one you guessed.

## Off-limits files

- `SECRETS.md` — never read or edit this file, under any circumstances, even if asked
  directly. It doesn't exist in this example vault, but if one is ever added to a real
  copy, it should never be committed or read by an assistant.
- `private/` — personal notes not meant for shared team context. Doesn't exist in this
  example vault either, but reserved as off-limits if added later.

This rule is backed by a matching deny rule in [.claude/settings.json](.claude/settings.json).
A rule written here alone is a convention. The deny rule is what enforces it, for Claude
Code's file tools and shell commands that name the file; the sandbox (`/sandbox`) covers
indirect reads like `grep -r`. Keep both in sync when you add a new off-limits file.

## Memory policy

Durable facts, decisions, and context belong in vault notes — not in the tool's own
separate memory feature. The vault is the single source of truth so that memory is
readable, editable, and portable outside of any one tool. Claude Code's auto memory is
switched off for this vault by `"autoMemoryEnabled": false` in
[.claude/settings.json](.claude/settings.json). Anyone who wants it for something narrower
(their own working-style preferences, not team facts) can turn it back on in their
untracked `.claude/settings.local.json`.

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
