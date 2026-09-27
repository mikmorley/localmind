---
type: meeting
date: 2026-10-06
attendees: [Priya, Dana, Marcus]
---

# Weekly Sync — 2026-10-06

## Agenda

1. Onboarding redesign — wireframe review
2. Support ticket volume check-in
3. Anything blocking

## Notes

**Onboarding redesign.** Dana walked through the wireframes for combining steps 2 and 3.
Consensus that the combined screen is less confusing and doesn't feel overloaded, as long
as we keep the optional fields collapsed behind a toggle. Marcus flagged that the profile
photo upload will need a separate loading state since it's the slowest part of the
combined screen — noted for the spec.

**Support ticket volume.** Still elevated (roughly 15% above baseline) but flat compared
to last week, not climbing further. Agreed not to treat it as a separate incident — most
tickets trace back to onboarding confusion, so the redesign should absorb it rather than
needing its own fix.

**Blockers.** None currently. Dana needs final copy for the combined screen from Priya by
Thursday to stay on track for Friday's prototype.

## Decisions

- Combine onboarding steps 2 and 3 into one screen, optional fields behind a toggle.
- Profile photo upload gets its own loading state in the combined screen.
- Support ticket spike is treated as downstream of onboarding friction, not tracked
  separately.

## Action items

- [ ] Dana — build clickable prototype of combined screen (due 2026-10-09)
- [ ] Priya — send final copy for combined screen to Dana (due 2026-10-08)
- [ ] Marcus — scope the profile-photo loading state
