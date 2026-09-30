#!/usr/bin/env python3
"""Validate the public Agent Skills package without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
SKILLS_ROOT = ROOT / ".agents" / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")
PRIVATE_MARKERS = (
    "liech-brand-direction",
    "viskie-brand-direction",
    "fabiula-brand-direction",
    "liech-hub-eter",
    "liechparfums.com.br",
    "rm-pneus",
)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opener")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing YAML frontmatter closer")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def fail(message: str) -> None:
    print(f"FAIL: {message}")


def main() -> int:
    failures = 0
    if not SKILLS_ROOT.is_dir():
        fail(f"skills root not found: {SKILLS_ROOT}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("no skills found")
        return 1

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(f"{skill_dir.name}: missing SKILL.md")
            failures += 1
            continue

        text = skill_file.read_text(encoding="utf-8")
        try:
            frontmatter = parse_frontmatter(text)
        except ValueError as exc:
            fail(f"{skill_dir.name}: {exc}")
            failures += 1
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if name != skill_dir.name:
            fail(f"{skill_dir.name}: frontmatter name is {name!r}")
            failures += 1
        if not NAME_RE.fullmatch(name):
            fail(f"{skill_dir.name}: invalid kebab-case name")
            failures += 1
        if not description:
            fail(f"{skill_dir.name}: missing description")
            failures += 1
        if "use when" not in description.lower():
            fail(f"{skill_dir.name}: description should contain a trigger boundary ('Use when')")
            failures += 1
        if "do not use" not in description.lower() and "exclude" not in description.lower():
            fail(f"{skill_dir.name}: description should contain an exclusion boundary")
            failures += 1

        for match in LINK_RE.finditer(text):
            rel = match.group(1).split("#", 1)[0]
            target = (skill_dir / rel).resolve()
            if not target.exists():
                fail(f"{skill_dir.name}: broken local link {rel!r}")
                failures += 1

        for path in skill_dir.rglob("*"):
            if not path.is_file():
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            lowered = content.lower()
            for marker in PRIVATE_MARKERS:
                if marker.lower() in lowered:
                    fail(f"{path.relative_to(ROOT)}: private marker {marker!r}")
                    failures += 1

    if failures:
        print(f"\n{failures} validation failure(s).")
        return 1

    print(f"PASS: {len(skill_dirs)} public skills validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
