#!/usr/bin/env python3
"""Validate the public Agent Skills package without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
SKILLS_ROOT = ROOT / ".agents" / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")
PERSONAL_EMAIL_RE = re.compile(
    r"(?i)\b[a-z0-9._%+-]+@(?:gmail|outlook|hotmail|yahoo)\.[a-z]{2,}\b"
)
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
)
# Split literals keep the denylist from matching its own source file while still
# detecting the assembled private markers in every other public text file.
PRIVATE_MARKERS = (
    "liech" + "-brand-direction",
    "viskie" + "-brand-direction",
    "fabiula" + "-brand-direction",
    "liech" + "-hub-eter",
    "liech" + "parfums.com.br",
    "liech" + "parfums",
    "rm-" + "pneus",
)
SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    ".next",
    "dist",
    "build",
    "coverage",
    "htmlcov",
    "artifacts",
    "tmp",
    ".cache",
}


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


def iter_public_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts[:-1]):
            continue
        try:
            path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        files.append(path)
    return files


def check_local_links(path: Path, text: str) -> int:
    failures = 0
    for match in LINK_RE.finditer(text):
        rel = unquote(match.group(1).split("#", 1)[0])
        if not rel:
            continue
        target = (path.parent / rel).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            fail(f"{path.relative_to(ROOT)}: local link escapes repository: {rel!r}")
            failures += 1
            continue
        if not target.exists():
            fail(f"{path.relative_to(ROOT)}: broken local link {rel!r}")
            failures += 1
    return failures


def validate_package(skill_names: list[str]) -> int:
    failures = 0
    manifest_path = ROOT / "skills-package.json"
    version_path = ROOT / "SKILLS_PACKAGE_VERSION"

    if not manifest_path.is_file():
        fail("missing skills-package.json")
        return 1
    if not version_path.is_file():
        fail("missing SKILLS_PACKAGE_VERSION")
        return 1

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        fail(f"skills-package.json: {exc}")
        return 1

    if manifest.get("canonicalRoot") != ".agents/skills":
        fail("skills-package.json: canonicalRoot must be '.agents/skills'")
        failures += 1

    active = manifest.get("activeSkills")
    if not isinstance(active, list) or any(not isinstance(item, str) for item in active):
        fail("skills-package.json: activeSkills must be a string list")
        failures += 1
    else:
        if len(active) != len(set(active)):
            fail("skills-package.json: activeSkills contains duplicates")
            failures += 1
        if set(active) != set(skill_names):
            fail(
                "skills-package.json: activeSkills does not match skill directories "
                f"(manifest={sorted(active)!r}, dirs={sorted(skill_names)!r})"
            )
            failures += 1

    profiles = manifest.get("profiles")
    if not isinstance(profiles, dict):
        fail("skills-package.json: profiles must be an object")
        failures += 1
    else:
        known = set(skill_names)
        for profile_name, members in profiles.items():
            if not isinstance(members, list) or any(not isinstance(item, str) for item in members):
                fail(f"skills-package.json: profile {profile_name!r} must be a string list")
                failures += 1
                continue
            unknown = sorted(set(members) - known)
            if unknown:
                fail(
                    f"skills-package.json: profile {profile_name!r} references unknown skills {unknown!r}"
                )
                failures += 1

    manifest_version = manifest.get("version")
    version_file = version_path.read_text(encoding="utf-8").strip()
    if manifest_version != version_file:
        fail(
            "package version mismatch: "
            f"skills-package.json={manifest_version!r}, SKILLS_PACKAGE_VERSION={version_file!r}"
        )
        failures += 1

    return failures


def main() -> int:
    failures = 0
    if not SKILLS_ROOT.is_dir():
        fail(f"skills root not found: {SKILLS_ROOT}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("no skills found")
        return 1

    skill_names = [path.name for path in skill_dirs]

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
        lowered_description = description.lower()
        if name != skill_dir.name:
            fail(f"{skill_dir.name}: frontmatter name is {name!r}")
            failures += 1
        if not NAME_RE.fullmatch(name):
            fail(f"{skill_dir.name}: invalid kebab-case name")
            failures += 1
        if not description:
            fail(f"{skill_dir.name}: missing description")
            failures += 1
        if "use when" not in lowered_description and "use for" not in lowered_description:
            fail(
                f"{skill_dir.name}: description should contain a trigger boundary "
                "('Use when' or 'Use for')"
            )
            failures += 1
        if not any(
            marker in lowered_description
            for marker in ("do not use", "do not ", "exclude", "never ")
        ):
            fail(
                f"{skill_dir.name}: description should contain an explicit exclusion/negative boundary"
            )
            failures += 1

    failures += validate_package(skill_names)

    for path in iter_public_text_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()

        if path.suffix.lower() == ".md":
            failures += check_local_links(path, text)

        for marker in PRIVATE_MARKERS:
            if marker.lower() in lowered:
                fail(f"{rel}: private marker {marker!r}")
                failures += 1

        if PERSONAL_EMAIL_RE.search(text):
            fail(f"{rel}: personal email address found")
            failures += 1

        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"{rel}: possible secret/private-key pattern found")
                failures += 1

    if failures:
        print(f"\n{failures} validation failure(s).")
        return 1

    print(f"PASS: {len(skill_dirs)} public skills validated; repository-wide public checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
