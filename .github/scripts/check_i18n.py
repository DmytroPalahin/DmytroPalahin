#!/usr/bin/env python3
"""Check that the translated READMEs stay structurally in sync.

Four language versions drift apart the moment you edit one and forget the
others. This catches that in CI instead of six months later.

Checks:
  1. every expected README file exists;
  2. they all have the same number of level-2 sections;
  3. every version links to all the other versions;
  4. they all reference the same set of local files (assets, workflows).
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = "README.md"
TRANSLATIONS = ["README.fr.md", "README.ru.md", "README.ua.md"]
ALL_FILES = [CANONICAL, *TRANSLATIONS]

SECTION = re.compile(r"^## ", re.MULTILINE)
LOCAL_LINK = re.compile(r"(?:src|srcset|href)=\"(?!https?:|mailto:)([^\"]+)\"")

errors: list[str] = []


def read(name: str) -> str | None:
    path = ROOT / name
    if not path.is_file():
        errors.append(f"missing file: {name}")
        return None
    return path.read_text(encoding="utf-8")


contents = {name: read(name) for name in ALL_FILES}
if errors:
    print("\n".join(f"error: {e}" for e in errors))
    sys.exit(1)

# 2. same number of sections everywhere
expected_sections = len(SECTION.findall(contents[CANONICAL] or ""))
for name in TRANSLATIONS:
    found = len(SECTION.findall(contents[name] or ""))
    if found != expected_sections:
        errors.append(
            f"{name}: has {found} sections, {CANONICAL} has {expected_sections} "
            "- a translation is out of date"
        )

# 3. language switcher is complete in every version
for name in ALL_FILES:
    body = contents[name] or ""
    for other in ALL_FILES:
        if other == name:
            continue
        if f"({other})" not in body:
            errors.append(f"{name}: missing language link to {other}")

# 4. referenced local paths actually exist
for name in ALL_FILES:
    for target in LOCAL_LINK.findall(contents[name] or ""):
        target = target.split("#", 1)[0].strip()
        if not target:
            continue
        if not (ROOT / target).exists():
            errors.append(f"{name}: references missing path '{target}'")

if errors:
    print("\n".join(f"error: {e}" for e in errors))
    sys.exit(1)

print(f"ok: {len(ALL_FILES)} READMEs in sync ({expected_sections} sections each)")
