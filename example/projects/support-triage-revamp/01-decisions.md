---
type: project
status: done
updated: 2026-09-14
---

# Support Ticket Triage Revamp — Decisions

A running log of decisions made on this project, most recent first. See
[00-overview.md](00-overview.md) for background.

## 2026-09-12 — Check for a single root cause before anything else

Both August spikes turned out to have one shared cause, but the team spent hours treating
each ticket as a separate problem before noticing the pattern. Decided that the first
step of any future triage is a quick sample of 15-20 tickets, specifically looking for a
shared theme, before doing anything else.

## 2026-09-10 — Fold known-cause spikes into existing project scope

When a spike's root cause maps to a project that's already being worked on, treat it as
part of that project instead of opening a separate incident. Opening a new incident for a
problem someone's already fixing just splits the context in two places.

## 2026-09-08 — Set a 25% threshold for notifying the team lead

Below 25% above baseline, let whoever's triaging handle it. Above that, notify the team
lead regardless of whether a root cause has been found yet, since volume that high is
worth a second set of eyes even mid-investigation.
