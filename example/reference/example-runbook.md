---
type: reference
updated: 2026-09-15
---

# Runbook: Handling a Support Ticket Spike

Reference procedure for when support ticket volume rises noticeably above baseline.
Unlike daily notes or project files, this doesn't change often — it's updated only when
the process itself changes, not every time it's used.

## When to use this

Ticket volume is more than ~10% above the trailing 4-week baseline for two or more
consecutive days.

## Steps

1. **Check for a single root cause first.** Pull a sample of 15–20 recent tickets and
   look for a shared theme (a specific flow, a recent release, a specific error message).
   Most spikes trace back to one cause rather than many.
2. **Decide: incident or absorb.** If the cause maps to an already-active project (e.g.
   an onboarding redesign already in flight), fold the spike into that project's scope
   instead of opening a separate incident — note the decision in that project's decisions
   file. If there's no existing owner, open a dedicated note under `projects/`.
3. **Notify the team lead** if volume is more than 25% above baseline, regardless of
   whether a root cause has been found yet.
4. **Log the resolution.** Once volume returns to baseline, note what fixed it (a
   redesign, a bug fix, a comms change) in the relevant project's decisions file, so the
   next spike can be checked against this one.

## Notes

This runbook intentionally doesn't name specific tools or dashboards — fill in your own
team's monitoring setup here if you adapt this note for a real vault.
