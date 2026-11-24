#!/usr/bin/env bash
# LocalMind: warn at the start of a Claude Code session when NOW.md looks stale.
#
# Usage: now-staleness.sh [max_age_days]    (default: 7)
#
# Reads the `updated:` date from NOW.md's YAML frontmatter. When NOW.md is missing, has no
# valid date, or is older than max_age_days, it prints a SessionStart hook JSON response:
# a short warning for you, and a note in Claude's context asking it to flag the staleness.
# When NOW.md is current it prints nothing. It always exits 0, so it never blocks a session.
#
# LOCALMIND_TODAY=YYYY-MM-DD overrides today's date, for testing.

set -u

max_age="${1:-7}"
case "$max_age" in
  '' | *[!0-9]*) max_age=7 ;;
esac

now_file="${CLAUDE_PROJECT_DIR:-$PWD}/NOW.md"
today="${LOCALMIND_TODAY:-$(date +%Y-%m-%d)}"

# Days since 1970-01-01 for a YYYY-MM-DD date, using Howard Hinnant's days_from_civil
# algorithm, so the script needs no GNU- or BSD-specific `date` flags.
days() {
  local y=$((10#${1:0:4})) m=$((10#${1:5:2})) d=$((10#${1:8:2}))
  if ((m <= 2)); then y=$((y - 1)); fi
  local era=$(((y >= 0 ? y : y - 399) / 400))
  local yoe=$((y - era * 400))
  local doy=$(((153 * ((m + 9) % 12) + 2) / 5 + d - 1))
  local doe=$((yoe * 365 + yoe / 4 - yoe / 100 + doy))
  echo $((era * 146097 + doe - 719468))
}

is_date() {
  [[ "$1" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]
}

# $1 is shown to you, $2 goes into Claude's context. Both are built only from fixed text,
# dates and numbers, so they need no JSON escaping.
warn() {
  printf '{"systemMessage":"%s","hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' \
    "$1" "$2"
  exit 0
}

if [[ ! -f "$now_file" ]]; then
  warn "LocalMind: no NOW.md found in this vault." \
    "This vault has no NOW.md, so there is no record of current priorities. Mention this to the user before relying on any assumptions about what matters right now."
fi

# The `updated:` value from the frontmatter block at the top of the file, with quotes and
# spaces stripped. Carriage returns are dropped first so Windows line endings work.
updated="$(awk '
  { sub(/\r$/, "") }
  NR == 1 && $0 != "---" { exit }
  NR > 1 && $0 == "---" { exit }
  NR > 1 && /^updated:/ { sub(/^updated:[ \t]*/, ""); gsub(/["\047 \t\r]/, ""); print; exit }
' "$now_file")"

if ! is_date "$updated"; then
  warn "LocalMind: NOW.md has no valid updated: date." \
    "NOW.md has no valid updated: date in its frontmatter, so its priorities may be stale. Mention this to the user and offer to refresh NOW.md before relying on it."
fi

if ! is_date "$today"; then
  exit 0
fi

age=$(($(days "$today") - $(days "$updated")))

if ((age > max_age)); then
  unit="days"
  if ((age == 1)); then unit="day"; fi
  warn "LocalMind: NOW.md was last updated $updated ($age $unit ago)." \
    "NOW.md was last updated $updated, $age $unit ago, so its priorities may be stale. Mention this to the user and offer to refresh NOW.md before relying on it."
fi

exit 0
