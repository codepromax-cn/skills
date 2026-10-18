#!/usr/bin/env python3
"""Validate the repository's portable Agent Skills packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_SKILL_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024


def read_frontmatter(skill_file: Path) -> dict[str, object]:
    content = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", content, re.DOTALL)
    if match is None:
        raise ValueError("missing YAML frontmatter delimited by ---")

    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return metadata


def validate_skill(skill_dir: Path, root_license: bytes) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    license_file = skill_dir / "LICENSE"

    if not skill_file.is_file():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]
    if not license_file.is_file():
        errors.append(f"{skill_dir.relative_to(ROOT)}: missing per-skill LICENSE")
    elif license_file.read_bytes() != root_license:
        errors.append(f"{skill_dir.relative_to(ROOT)}: LICENSE differs from the repository license")

    try:
        metadata = read_frontmatter(skill_file)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        errors.append(f"{skill_file.relative_to(ROOT)}: {error}")
        return errors

    name = metadata.get("name")
    description = metadata.get("description")
    folder_name = skill_dir.name

    if not isinstance(name, str) or not name:
        errors.append(f"{skill_file.relative_to(ROOT)}: name must be a non-empty string")
    else:
        if len(name) > MAX_SKILL_NAME_LENGTH:
            errors.append(f"{skill_file.relative_to(ROOT)}: name exceeds {MAX_SKILL_NAME_LENGTH} characters")
        if not SKILL_NAME_PATTERN.fullmatch(name):
            errors.append(f"{skill_file.relative_to(ROOT)}: name must use lowercase letters, digits, and single hyphens")
        if name != folder_name:
            errors.append(f"{skill_file.relative_to(ROOT)}: name '{name}' must match directory '{folder_name}'")

    if not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_file.relative_to(ROOT)}: description must be a non-empty string")
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"{skill_file.relative_to(ROOT)}: description exceeds {MAX_DESCRIPTION_LENGTH} characters")

    license_id = metadata.get("license")
    if license_id != "MIT":
        errors.append(f"{skill_file.relative_to(ROOT)}: frontmatter license must be MIT")

    return errors


def main() -> int:
    root_license_file = ROOT / "LICENSE"
    if not root_license_file.is_file():
        print("ERROR: missing root LICENSE", file=sys.stderr)
        return 1
    if not SKILLS_DIR.is_dir():
        print("ERROR: missing skills/ directory", file=sys.stderr)
        return 1

    root_license = root_license_file.read_bytes()
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("ERROR: no skill directories found under skills/", file=sys.stderr)
        return 1

    errors = [error for skill_dir in skill_dirs for error in validate_skill(skill_dir, root_license)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    for skill_dir in skill_dirs:
        print(f"OK: {skill_dir.relative_to(ROOT)}")
    print(f"Validated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
