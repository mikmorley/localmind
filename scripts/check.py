#!/usr/bin/env python3
"""Consistency checks for the LocalMind repo.

Run from anywhere: python3 scripts/check.py
Uses the standard library only, so it runs the same locally and in CI.

Checks:
  1. Every .claude/settings.json is valid JSON, and all copies are identical.
  2. Each core file in template/ still has [PLACEHOLDER] markers.
  3. Nothing in example/ has a leftover [PLACEHOLDER] or [DATE] marker.
  4. Relative Markdown links and images point at files that exist, and #anchors
     match a heading in the target file.
  5. @ imports in CLAUDE.md files point at files that exist.
  6. The opt-in NOW.md staleness hook in extras/ gives the right result for fresh,
     stale, undated and missing NOW.md files (skipped if bash isn't installed).
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE_FILES = ("CLAUDE.md", "INDEX.md", "NOW.md")
EXAMPLE_MARKERS = ("[PLACEHOLDER", "[DATE]")
HOOK = ROOT / "extras" / "hooks" / "now-staleness" / "now-staleness.sh"

# (NOW.md content or None for no file, today, hook args, expected warning text or None
# for silence)
HOOK_CASES = [
    ("---\nupdated: 2026-10-06\n---\n", "2026-10-08", [], None),
    ("---\nupdated: 2026-10-06\n---\n", "2026-10-13", [], None),
    ("---\nupdated: 2026-10-06\n---\n", "2026-10-14", [], "8 days ago"),
    ("---\nupdated: 2026-10-06\n---\n", "2026-11-24", ["7"], "49 days ago"),
    ("---\nupdated: 2026-10-06\n---\n", "2026-11-24", ["60"], None),
    ("---\nupdated: 2026-10-06\n---\n", "2026-10-07", ["0"], "1 day ago"),
    ("---\nupdated: 2024-02-28\n---\n", "2024-03-01", ["1"], "2 days ago"),
    ("---\nupdated: 2026-12-31\n---\n", "2027-01-02", ["0"], "2 days ago"),
    ('---\ntype: now\nupdated: "2026-10-06"\n---\n', "2026-10-14", [], "8 days ago"),
    ("---\r\nupdated: 2026-10-06\r\n---\r\n", "2026-10-14", [], "8 days ago"),
    ("---\nupdated: 2026-10-06\n---\n", "2026-10-14", ["abc"], "8 days ago"),
    ("---\nupdated: [DATE]\n---\n", "2026-10-07", [], "no valid updated"),
    ("# Now\n\nupdated: 2026-10-06\n", "2026-10-07", [], "no valid updated"),
    ("---\ntitle: now\n---\nupdated: 2026-10-06\n", "2026-10-07", [], "no valid updated"),
    (None, "2026-10-07", [], "no NOW.md"),
]

FENCE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
IMPORT = re.compile(r"^@(\S+)\s*$", re.MULTILINE)

errors = []


def rel(path):
    return path.relative_to(ROOT).as_posix()


def markdown_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def slug(heading):
    """GitHub-style heading anchor."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        text = FENCE.sub("", path.read_text(encoding="utf-8"))
        seen, found = {}, set()
        for match in HEADING.finditer(text):
            base = slug(match.group(1))
            n = seen.get(base, 0)
            found.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
        cache[path] = found
    return cache[path]


def check_settings():
    files = sorted(p for p in ROOT.rglob("settings.json")
                   if p.parent.name == ".claude" and ".git" not in p.parts)
    if not files:
        errors.append("no .claude/settings.json files found")
        return
    parsed = {}
    for path in files:
        try:
            parsed[path] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel(path)}: invalid JSON ({exc})")
            continue
        deny = parsed[path].get("permissions", {}).get("deny")
        if not isinstance(deny, list) or not deny:
            errors.append(f"{rel(path)}: missing a non-empty permissions.deny list")
    if len(parsed) > 1:
        first_path, first = next(iter(parsed.items()))
        for path, data in parsed.items():
            if data != first:
                errors.append(f"{rel(path)}: differs from {rel(first_path)}; "
                              "keep all settings.json copies identical")


def check_placeholders():
    for name in CORE_FILES:
        path = ROOT / "template" / name
        if not path.exists():
            errors.append(f"template/{name}: missing")
        elif "[PLACEHOLDER" not in path.read_text(encoding="utf-8"):
            errors.append(f"template/{name}: no [PLACEHOLDER] markers left; "
                          "template files should stay unfilled")
    for path in sorted((ROOT / "example").rglob("*")):
        if not path.is_file() or path.suffix not in (".md", ".json"):
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for marker in EXAMPLE_MARKERS:
                if marker in line:
                    errors.append(f"{rel(path)}:{lineno}: leftover {marker} marker; "
                                  "the example vault should be fully filled in")


def check_target(source, target, lineno):
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
        return  # http:, https:, mailto: and other external schemes
    path_part, _, fragment = target.partition("#")
    dest = (source.parent / path_part).resolve() if path_part else source
    where = f"{rel(source)}:{lineno}"
    if not dest.exists():
        errors.append(f"{where}: link target not found: {target}")
        return
    if fragment and dest.suffix == ".md" and fragment.lower() not in anchors(dest):
        errors.append(f"{where}: no heading for anchor #{fragment} in {rel(dest)}")


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def check_links():
    for path in markdown_files():
        raw = path.read_text(encoding="utf-8")
        # Blank out code instead of deleting it so line numbers stay accurate.
        text = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), raw)
        text = HTML_COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)
        text = INLINE_CODE.sub(lambda m: " " * len(m.group(0)), text)
        for match in LINK.finditer(text):
            check_target(path, match.group(1), line_of(text, match.start()))
        if path.name == "CLAUDE.md":
            for match in IMPORT.finditer(text):
                target = match.group(1)
                if not (path.parent / target).exists():
                    errors.append(f"{rel(path)}:{line_of(text, match.start())}: "
                                  f"@ import not found: {target}")


def check_hook():
    if not HOOK.exists():
        return
    if not os.access(HOOK, os.X_OK):
        errors.append(f"{rel(HOOK)}: not executable; run chmod +x on it")
    if shutil.which("bash") is None:
        print(f"Skipping {rel(HOOK)} tests: bash not found.")
        return
    for content, today, args, expected in HOOK_CASES:
        with tempfile.TemporaryDirectory() as vault:
            if content is not None:
                Path(vault, "NOW.md").write_bytes(content.encode())
            env = {**os.environ, "CLAUDE_PROJECT_DIR": vault, "LOCALMIND_TODAY": today}
            result = subprocess.run(["bash", str(HOOK), *args], env=env,
                                    capture_output=True, text=True, timeout=10)
        case = f"{rel(HOOK)} (NOW.md {content!r}, today {today}, args {args})"
        out = result.stdout.strip()
        if result.returncode != 0:
            errors.append(f"{case}: exited {result.returncode}, expected 0")
        if expected is None:
            if out:
                errors.append(f"{case}: expected no output, got {out}")
            continue
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            errors.append(f"{case}: output is not valid JSON: {out!r}")
            continue
        specific = data.get("hookSpecificOutput", {})
        if specific.get("hookEventName") != "SessionStart":
            errors.append(f"{case}: hookSpecificOutput.hookEventName is not SessionStart")
        message = data.get("systemMessage", "")
        if expected not in message or not specific.get("additionalContext"):
            errors.append(f"{case}: expected a warning containing {expected!r}, got {out}")


def main():
    check_settings()
    check_placeholders()
    check_links()
    check_hook()
    if errors:
        print(f"{len(errors)} problem(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
