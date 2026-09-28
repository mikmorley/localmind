---
type: index
updated: 2026-10-06
---

# Index

This file maps *where things live*, by folder purpose and naming pattern — not an
exhaustive file listing. It should go stale slower than a full file list would, because
it describes the shape of the vault rather than its current contents.

For *what matters right now*, see [NOW.md](NOW.md) instead.

## daily-notes/

One file per day: tasks, running notes, and any decisions made that day. This is where
most day-to-day capture happens — if something important comes up mid-day, it lands here
first, and gets promoted to a project file or reference note later if it turns out to be
durable.

- **Naming pattern:** `YYYY-MM-DD.md`, one file per day
- **Contains:** a `## Tasks` checklist, a `## Notes` section, and a `## Decisions` section
  (only present on days a real decision was made)
- **Example:** `2026-10-06.md`

## projects/

One subfolder per project, active or finished. Each project folder uses numbered files so reading
order is obvious: `00-overview.md` first (what it is, why it exists, current status),
then `01-decisions.md` (a running decisions log, most recent first), then further numbered
files as needed (`02-spec.md`, `03-retro.md`, etc.) for projects that grow.

- **Naming pattern:** `projects/<project-name>/NN-topic.md`
- **Contains:** overview, decisions log, and any project-specific supporting files
- **Example:** `projects/example-project/00-overview.md`

## meetings/

One file per meeting. Not folded into daily notes because meetings often need to be
found by topic or attendee rather than by date, and because a meeting's agenda/notes/
action-items structure is different enough from a daily note to warrant its own shape.

- **Naming pattern:** `<meeting-name>-YYYY-MM-DD.md`
- **Contains:** agenda, notes, decisions, and action items
- **Example:** `weekly-sync-2026-10-06.md`

## reference/

Durable material that doesn't change often: runbooks, standing procedures, glossaries.
Unlike daily notes or project files, reference notes are updated only when the underlying
process or fact changes — not on a regular cadence.

- **Naming pattern:** `lowercase-hyphenated-topic.md`
- **Contains:** one note per procedure or topic, no dating convention needed since these
  aren't time-bound
- **Example:** `example-runbook.md`

## personal/

Notes that aren't work at all, kept in the same vault because there's no reason to run a
separate app for them. Not off-limits, not treated differently from anything else here,
just filed under its own folder.

- **Naming pattern:** `lowercase-hyphenated-topic.md`
- **Contains:** whatever's personal, a reading list, a project of your own, anything you'd
  otherwise scatter across other apps
- **Example:** `reading-list.md`

## How to keep this current

Re-audit this file periodically — when a folder's purpose changes, when you add a new
top-level folder, or when the naming pattern for a folder drifts from what's written here.
This is a manual habit by default; if the vault grows large enough to justify it, this
re-audit can later be automated with a script or a Claude Code skill that scans folder
structure and flags drift. That automation is optional and not required to use this
pattern.
