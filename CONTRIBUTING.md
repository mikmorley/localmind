# Contributing

This is a template/boilerplate repo, not an active application. There's no build to break
and no users running this code in production. Contributions are welcome; keep them scoped
to what's below.

## What's in scope

- Improvements to the pattern itself (the three-file structure, the conventions in
  `template/CLAUDE.md`, the deny-list approach)
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
  service, or an automated agent system. Skills or scripts can be mentioned as optional
  extensions, but nothing here should require one to work.

## Making a change

1. Open an issue or PR describing what you're changing and why.
2. If you're changing `template/`, check whether `example/` needs a matching update so
   the two stay consistent. The example vault exists to demonstrate the template in use.
3. Keep `template/CLAUDE.md` small. If your change makes it noticeably longer, consider
   whether the content belongs there or in a vault note instead.
