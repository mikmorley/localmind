# Contributing

This is a template/boilerplate repo, not an active application. There's no build to break
and no users running this code in production. Contributions are welcome; keep them scoped
to what's below.

## What's in scope

- Improvements to the pattern itself (the three-file structure, the conventions in
  `template/CLAUDE.md`, the deny-list approach, the `onboard` skill)
- Clarity improvements to the README or the docs inside `template/`
- Additions to `example/` that better demonstrate an existing convention

## What's out of scope

- Personal content. Keep `example/` fictional and generic: no real names, companies, or
  identifying details. It should read as a reference anyone can adapt, not someone's
  private notes.
- Tool-specific syntax (Obsidian Dataview blocks, plugin config, wikilink requirements).
  The pattern is plain Markdown and YAML frontmatter on purpose, so it works whether the
  vault is opened in Obsidian, a plain text editor, or nothing at all.
- New scope beyond the pattern itself. This isn't the place for a notes app, a sync
  service, or an automated agent system. Optional skills, hooks or scripts go in
  `extras/`, each with its own README, and nothing in `template/` should require one
  to work.

## Making a change

1. Open an issue or PR describing what you're changing and why.
2. If you're changing `template/`, check whether `example/` needs a matching update so
   the two stay consistent. The example vault exists to demonstrate the template in use.
3. Keep `template/CLAUDE.md` small. If your change makes it noticeably longer, consider
   whether the content belongs there or in a vault note instead.
4. Run the consistency checks before opening a PR. CI runs the same script on every PR.

   ```bash
   python3 scripts/check.py
   ```

   It checks that every `.claude/settings.json` copy is valid and identical, that the
   `AGENTS.md` and `.gitignore` copies are identical, that `template/` still has its
   `[PLACEHOLDER]` markers and `example/` has none, that `template/` and `example/` have
   no em dashes, and that relative links, `#anchors`, and `@` imports all resolve. It
   needs only the Python standard library.
5. House style for `template/` and `example/`: no em dashes. Use a comma, colon, period,
   or parentheses, whichever reads most naturally. The check enforces this, so the
   files stay consistent however many people edit them.
