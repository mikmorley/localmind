---
name: onboard
description: Interview the person using this vault and turn their answers into a filled-in CLAUDE.md, INDEX.md, and NOW.md, creating the folders INDEX.md describes. Use when setting up a new vault from template/, finishing a setup that stopped partway, or refreshing an existing vault's current-state or structure.
metadata:
  trigger: Setting up a new vault from template/, resuming a partial setup, or refreshing CLAUDE.md, INDEX.md, or NOW.md
---

# Onboard

Interview the person using this vault and write their answers directly into `CLAUDE.md`,
`INDEX.md`, and `NOW.md`. Ask one question at a time. Propose a sensible default where you
can, and let them accept it, edit it, or skip it.

## Before you start

Find `CLAUDE.md`, `INDEX.md`, and `NOW.md` in the current directory. If none exist, stop
and tell the person to copy the contents of `template/` into their vault first, with
`cp -r template/. /path/to/vault/` so the hidden `.claude/` folder comes too. If only some
exist, stop and name the missing ones so the person can copy them from `template/` first.

Check all three files for `[PLACEHOLDER]` markers, and the `INDEX.md` and `NOW.md`
frontmatter for `updated: [DATE]`.

- **Markers in any file:** setup isn't finished. This is either a first run or an earlier
  run that stopped partway. Tell the person which files and sections still have
  placeholders, then run **First-time setup** below for those sections only.
- **No markers anywhere:** this is a refresh. Skip straight to **Refreshing NOW.md**,
  unless the person asked for something more specific (a new folder in INDEX.md, a change
  to a convention in CLAUDE.md, and so on). In that case, ask about that directly instead
  of running the full interview. When you add a folder to INDEX.md, create it as in step 5.

## First-time setup

Ask these in order. Skip a question when its section no longer has a `[PLACEHOLDER]`
marker (on a resumed setup, that means it's already filled in), or when the person already
answered it earlier in the conversation.

1. **Purpose.** "What's this vault for? Personal notes, a team's shared notes, a specific
   project? Who else, if anyone, will use it?" Fills `## What this vault is` in
   `CLAUDE.md`.
2. **Off-limits files.** "Any files or folders that should never be read or edited?
   Credentials, private drafts, anything like that?" Fills `## Off-limits files` in
   `CLAUDE.md`, and add a matching deny rule for each one to `.claude/settings.json`.
3. **Memory policy.** "Should the tool's own separate memory feature stay unused, or do
   you want it for something narrow, like your own working-style preferences?" Fills
   `## Memory policy` in `CLAUDE.md`. If they want it, set `"autoMemoryEnabled"` to `true`
   in `.claude/settings.json`; otherwise leave it `false`.
4. **Conventions.** "How do you want to name files? Any tagging convention? Do old dated
   notes get archived, and if so, how?" Fills `## Vault conventions` in `CLAUDE.md`.
5. **Structure.** "What top-level folders do you want? Daily notes, projects, meetings,
   reference, personal, something else? For each one, what's it for, and how are files
   inside it named?" Fills `INDEX.md`, one section per folder, following the existing
   `Naming pattern` / `Contains` / `Example` pattern.

   Then list the folders that don't exist yet and, once the person confirms, create them
   as empty folders, with no placeholder notes inside. Leave existing folders alone: don't
   rename, move, or delete anything. If a folder already in the vault isn't on their list,
   ask whether to add it to INDEX.md. If the vault is a git repository, mention that git
   doesn't track empty folders, so a new folder shows up in git once it holds a note.
6. **Current state.** Run through **Refreshing NOW.md** below.

Replace every `[PLACEHOLDER]` block with the person's actual answer. Don't leave
commentary, brackets, or unanswered placeholders behind. Set `updated:` in the `INDEX.md`
and `NOW.md` frontmatter to today's date.

Before finishing, check all three files for `[PLACEHOLDER]` and `[DATE]` again. If any
are left (because the person skipped a question, say), tell them which sections, and that
running `/onboard` again picks up from there.

## Refreshing NOW.md

Ask:

- "What's the current situation, in one or two sentences?"
- "What are your top priorities right now, in order?"
- "What's actively in flight?"
- "Anything lower priority or parked, and why?"

Rewrite `NOW.md` from these answers. Don't append to what's already there; NOW.md reflects
the current state, not a running log. Set `updated:` to today's date.

## After

Show the person what changed, including any folders you created, or open the files, and
remind them these are plain Markdown files they can hand-edit any time. This skill is a
shortcut for getting started or staying current, not the only way to keep the vault up to
date.
