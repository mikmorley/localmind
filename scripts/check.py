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
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE_FILES = ("CLAUDE.md", "INDEX.md", "NOW.md")
EXAMPLE_MARKERS = ("[PLACEHOLDER", "[DATE]")

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


def main():
    check_settings()
    check_placeholders()
    check_links()
    if errors:
        print(f"{len(errors)} problem(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
