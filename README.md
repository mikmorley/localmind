# LocalMind

Persistent memory for Claude Code, built from plain Markdown files you own.

A boilerplate pattern for using a plain-Markdown note vault as [Claude Code](https://claude.com/claude-code)'s
persistent memory, independent of any specific note app. It works whether the vault is
opened in Obsidian, a plain text editor, or nothing at all. No Dataview, no plugin config,
no app-specific syntax required.

By default, an AI coding or agent tool has no memory of your project, priorities, or past
decisions once a session ends. This pattern gives it one: a small set of Markdown files
and a few rules that let Claude Code orient itself at the start of every session, covering
what's current and where to look next.

## Why this exists

Most AI coding and agent tools store memory inside their own cloud service. This pattern
takes a different starting point:

- **Your data stays yours.** Memory lives in plain-text files on your own machine, in your
  own git repo, not on a vendor's server. It survives closing an account, switching tools,
  or a vendor changing its memory feature entirely.
- **No lock-in.** Plain Markdown works with any AI tool that can read a file, not only
  Claude Code. The vault you build today keeps working if you move to a different
  assistant next year.
- **Every fact is auditable.** The assistant's memory is a set of files you can open, diff,
  and check into git history, not an opaque blob you have to take on faith. If it acted on
  something wrong, you can see exactly what it read and when that file last changed.
- **It grows with you.** A single person starts with a handful of daily notes and one
  project folder. A team adds more folders and more contributors without changing the
  underlying pattern, because the three files describe structure and priorities, not a
  fixed list of content. The same `CLAUDE.md`, `INDEX.md`, and `NOW.md` pattern that works
  for one person's notes on day one still works once there are years of them.
- **It doesn't stop at work.** Nothing about the pattern is job-specific. The same vault
  that tracks a project's decisions can hold your own notes alongside it: health, finances,
  personal projects, a reading list, whatever you'd otherwise scatter across other apps,
  under the same rules and the same off-limits protections as everything else in the vault.

## Why three files, not one

- **[CLAUDE.md](template/CLAUDE.md)** holds *rules*: what's off-limits, how to file new
  notes, editing conventions, a memory policy. It changes rarely, so it stays small enough
  to read in full every session.
- **[INDEX.md](template/INDEX.md)** holds *where things live*: a map of folders by purpose
  and naming pattern, not an exhaustive file listing. It changes occasionally, when the
  shape of the vault changes, not when its contents do.
- **[NOW.md](template/NOW.md)** holds *what matters right now*: current priorities and
  situation, dated, short, and rewritten every session.

These three age at different rates and get read for different reasons. Merge them into
one file and either the rules get buried under a wall of changing status updates, or the
status updates get stale because you don't want to touch the file that also holds the
rules. Keeping them separate means each file stays exactly as long as it needs to be, and
you can trust each one for its own job.

## Quickstart

1. Copy the contents of [`template/`](template/) into a new or existing vault (or clone
   this whole repo and start from there).
2. Fill in the `[PLACEHOLDER]` text in `CLAUDE.md`, `INDEX.md`, and `NOW.md` with your own
   context.
3. Adjust `.claude/settings.json` if you have specific files that should be off-limits to
   Claude Code (see [Privacy and secrets](#privacy-and-secrets) below).
4. Start a Claude Code session in the vault. If it doesn't already read `CLAUDE.md` on its
   own, point it there yourself; from there it should read `INDEX.md`, then `NOW.md`, and
   orient itself.

Folder and file names in `template/` are suggestions. Rename `daily-notes/`, `projects/`,
or anything else to fit how you work. The three files and the separation between them are
what make the pattern work; folder names are yours to choose.

## Philosophy

- **Memory lives in one place.** Split durable facts between the vault and the tool's own
  separate memory feature, and neither one is trustworthy: you end up checking both, or
  trusting neither. The vault stays the single source of truth because it's plain text,
  versioned, and portable across tools.
- **The index describes patterns, not files.** List every file and the index goes stale
  the moment you add one that isn't on it. Describe a folder as "daily notes live here,
  named like this, containing that," and the index stays accurate as the vault grows:
  new files that follow the pattern don't need an entry.
- **NOW.md keeps context current.** Without it, Claude Code infers what's current from
  file timestamps and guesswork, or works from whatever it read last, which might be
  weeks old. Rewriting it every session, with today's date on it, forces a check against
  stale context.

## Worked example

[`example/`](example/) is a small, fully filled-in vault for a fictional team (no
placeholders) that shows the pattern at work: two [daily notes](example/daily-notes/), a
[project](example/projects/example-project/) using the numbered-file convention
(`00-overview.md`, `01-decisions.md`), a [meeting note](example/meetings/), a
[reference runbook](example/reference/), and a [personal note](example/personal/)
sitting right alongside the work notes, in the same vault, under the same rules. Its own
`CLAUDE.md`, `INDEX.md`, and `NOW.md` are filled in end to end. Start there if you want to
see the pattern in practice before adapting `template/` to your own vault.

## Privacy and secrets

This pattern means an AI agent reads your notes. If the vault holds anything that
shouldn't be exposed that way (credentials, private drafts, anything sensitive),
[`.claude/settings.json`](.claude/settings.json) shows how to deny read and edit access
to specific files or folders:

```json
{
  "permissions": {
    "deny": [
      "Read(./SECRETS.md)",
      "Edit(./SECRETS.md)",
      "Read(./private/**)",
      "Edit(./private/**)"
    ]
  }
}
```

This is a backstop enforced by the tool. It doesn't replace keeping live credentials out
of the vault in the first place. A rule in `CLAUDE.md` ("never read this file") is a
convention, and a model can be talked past a convention. A `settings.json` deny rule is
enforced regardless of what the prompt says. Use both, and keep real secrets out of the
vault when you can.

## What this isn't

- Not an Obsidian plugin or theme. It's plain Markdown and YAML frontmatter, nothing more.
- Not a note-taking app.
- Not a fully automated agent system. The three files and the rules around them are the
  whole pattern on their own. [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills)
  can add automation on top once the base pattern works (a skill that re-audits
  `INDEX.md` for drift, for example), but nothing here requires one.

## Author

Created by [Michael Morley](https://www.morley.cloud) ([michael@morley.cloud](mailto:michael@morley.cloud), [LinkedIn](https://www.linkedin.com/in/michaelmorleyau/)).

## License

[MIT](LICENSE)
