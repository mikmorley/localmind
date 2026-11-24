# NOW.md staleness hook

An opt-in Claude Code hook that checks NOW.md's `updated:` date when a session starts. If
the date is older than a threshold (7 days by default), it shows you a one-line warning
and asks Claude to flag that NOW.md may be stale before relying on it. If NOW.md is
current, it stays silent.

The pattern works without it: `CLAUDE.md` already tells Claude to check the date. The
hook makes that check automatic instead of relying on the model to notice.

## What it reports

- **NOW.md older than the threshold:** `LocalMind: NOW.md was last updated 2026-10-06 (49 days ago).`
- **No valid `updated:` date** (including an unfilled `[DATE]` placeholder): a warning
  saying so.
- **No NOW.md at all:** a warning saying so.

It never blocks a session. Whatever happens, it exits successfully.

## Install

1. Copy the script into your vault and make it executable:

   ```bash
   mkdir -p /path/to/your/vault/.claude/hooks
   cp extras/hooks/now-staleness/now-staleness.sh /path/to/your/vault/.claude/hooks/
   chmod +x /path/to/your/vault/.claude/hooks/now-staleness.sh
   ```

2. Add a `hooks` block to your vault's `.claude/settings.json`, next to the existing
   `permissions` block. The number at the end is the threshold in days.

   ```json
   "hooks": {
     "SessionStart": [
       {
         "matcher": "startup",
         "hooks": [
           {
             "type": "command",
             "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/now-staleness.sh 7"
           }
         ]
       }
     ]
   }
   ```

   The `startup` matcher runs it only when a new session starts, not after `/clear` or
   when Claude Code compacts the conversation.

3. Start a new Claude Code session in the vault. If NOW.md is stale you'll see the
   warning; if it's current, nothing appears.

## Try it without installing

Run it against the example vault with a fixed date:

```bash
CLAUDE_PROJECT_DIR=example LOCALMIND_TODAY=2026-11-24 extras/hooks/now-staleness/now-staleness.sh 7
```

## Requirements

`bash` and `awk`, which macOS and Linux have by default. On Windows, Claude Code needs Git
Bash or WSL to run it. Date maths is done in the script itself, so it doesn't depend on
GNU or BSD `date` flags.
