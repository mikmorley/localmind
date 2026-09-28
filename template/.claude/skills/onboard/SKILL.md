---
name: onboard
description: Interview the person using this vault and turn their answers into a filled-in CLAUDE.md, INDEX.md, and NOW.md. Use when setting up a new vault from template/, or when refreshing an existing vault's current-state or structure.
metadata:
  trigger: Setting up a new vault from template/, or refreshing CLAUDE.md, INDEX.md, or NOW.md
---

# Onboard

Interview the person using this vault and write their answers directly into `CLAUDE.md`,
`INDEX.md`, and `NOW.md`. Ask one question at a time. Propose a sensible default where you
can, and let them accept it, edit it, or skip it.

## Before you start

Find `CLAUDE.md`, `INDEX.md`, and `NOW.md` in the current directory. If none exist, stop
and tell the person to copy the contents of `template/` into their vault first.

Check `CLAUDE.md` for `[PLACEHOLDER]` markers.

- Markers present: this is first-time setup. Run the full interview below.
- No markers: this is a refresh. Skip straight to **Refreshing NOW.md**, unless the person
  asked for something more specific (a new folder in INDEX.md, a change to a convention
  in CLAUDE.md, and so on). In that case, ask about that directly instead of running the
  full interview.

## First-time setup

Ask these in order. Skip a question if the person already answered it earlier in the
conversation.

1. **Purpose.** "What's this vault for? Personal notes, a team's shared notes, a specific
   project? Who else, if anyone, will use it?" Fills `## What this vault is` in
   `CLAUDE.md`.
2. **Off-limits files.** "Any files or folders that should never be read or edited?
   Credentials, private drafts, anything like that?" Fills `## Off-limits files` in
   `CLAUDE.md`, and add a matching deny rule for each one to `.claude/settings.json`.
3. **Memory policy.** "Should the tool's own separate memory feature stay unused, or do
   you want it for something narrow, like your own working-style preferences?" Fills
   `## Memory policy` in `CLAUDE.md`.
4. **Conventions.** "How do you want to name files? Any tagging convention? Do old dated
   notes get archived, and if so, how?" Fills `## Vault conventions` in `CLAUDE.md`.
5. **Structure.** "What top-level folders do you want? Daily notes, projects, meetings,
   reference, personal, something else? For each one, what's it for, and how are files
   inside it named?" Fills `INDEX.md`, one section per folder, following the existing
   `Naming pattern` / `Contains` / `Example` pattern.
6. **Current state.** Run through **Refreshing NOW.md** below.

Replace every `[PLACEHOLDER]` block with the person's actual answer. Don't leave
commentary, brackets, or unanswered placeholders behind. Set `updated:` in the `INDEX.md`
and `NOW.md` frontmatter to today's date.

## Refreshing NOW.md

Ask:

- "What's the current situation, in one or two sentences?"
- "What are your top priorities right now, in order?"
- "What's actively in flight?"
- "Anything lower priority or parked, and why?"

Rewrite `NOW.md` from these answers. Don't append to what's already there; NOW.md reflects
the current state, not a running log. Set `updated:` to today's date.

## After

Show the person what changed, or open the files, and remind them these are plain Markdown
files they can hand-edit any time. This skill is a shortcut for getting started or staying
current, not the only way to keep the vault up to date.
