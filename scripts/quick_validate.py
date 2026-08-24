#!/usr/bin/env python3
"""Perform a compact structural check on one Codex skill directory."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ALLOWED = {"name", "description", "license", "allowed-tools", "metadata"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate(path: Path) -> tuple[bool, str]:
    skill_md = path / "SKILL.md"
    if not skill_md.is_file():
        return False, "SKILL.md not found"
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        return False, "invalid YAML frontmatter"
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return False, f"invalid YAML: {exc}"
    if not isinstance(data, dict):
        return False, "frontmatter must be a mapping"
    unexpected = sorted(set(data) - ALLOWED)
    if unexpected:
        return False, "unsupported frontmatter keys: " + ", ".join(unexpected)
    name = data.get("name")
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
        return False, "name must be lowercase hyphen-case"
    if name != path.name:
        return False, f"directory/name mismatch: {path.name!r} != {name!r}"
    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        return False, "description is missing"
    if len(description.strip()) > 1024 or "<" in description or ">" in description:
        return False, "description violates length or character constraints"
    if data.get("license") != "AGPL-3.0-or-later":
        return False, "license must be AGPL-3.0-or-later"
    if not isinstance(data.get("metadata"), dict):
        return False, "metadata mapping is required"
    required = [
        path / "agents" / "openai.yaml",
        path / "test-prompts.json",
        path / "test-results.md",
    ]
    missing = [str(item.relative_to(path)) for item in required if not item.is_file()]
    if missing:
        return False, "missing required files: " + ", ".join(missing)
    unfinished = ("TO" + "DO", "FIX" + "ME")
    body = text[match.end():]
    if any(re.search(rf"\b{term}\b", body, re.IGNORECASE) for term in unfinished):
        return False, "unfinished scaffold marker found"
    return True, "Skill is valid!"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/quick_validate.py <skill_directory>", file=sys.stderr)
        return 2
    ok, message = validate(Path(sys.argv[1]).expanduser().resolve())
    print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
