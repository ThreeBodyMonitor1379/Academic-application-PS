#!/usr/bin/env python3
"""Validate the curated Academic-application-PS release package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml


EXPECTED_SKILLS = {
    "evidence-first-graduate-personal-statement",
    "graduate-ps-prompt-calibration",
    "graduate-ps-trajectory-bridge",
}
ROOT_REQUIRED = {
    ".gitignore",
    "CHANGELOG.md",
    "LICENSE",
    "README.md",
    "THIRD_PARTY_NOTICES.md",
    "requirements-dev.txt",
    "docs/GLOSSARY.md",
    "docs/TESTING.md",
    "scripts/install_skills.py",
    "scripts/quick_validate.py",
    "scripts/validate_release.py",
    "tests/test_install_skills.py",
}
SKILL_REQUIRED = {
    "SKILL.md",
    "agents/openai.yaml",
    "test-prompts.json",
    "test-results.md",
}
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
REQUIRED_METADATA = {
    "version",
    "provenance",
    "source_title",
    "source_author",
    "source_date",
    "source_pages",
    "source_url",
    "tags",
    "related_skills",
}
PROVENANCE_VALUES = {"source-verified", "product-composite"}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class CheckResult:
    scope: str
    check: str
    passed: bool
    detail: str


def result(scope: str, check: str, passed: bool, detail: str) -> CheckResult:
    return CheckResult(scope=scope, check=check, passed=passed, detail=detail)


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


def relative_markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    links: list[str] = []
    for raw in LINK_PATTERN.findall(text):
        target = raw.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        links.append(target.split("#", 1)[0])
    return links


def check_links(root: Path, paths: list[Path]) -> list[CheckResult]:
    checks: list[CheckResult] = []
    for path in paths:
        for link in relative_markdown_links(path):
            resolved = (path.parent / link).resolve()
            try:
                resolved.relative_to(root.resolve())
                within_root = True
            except ValueError:
                within_root = False
            checks.append(
                result(
                    str(path.relative_to(root)),
                    "relative-link",
                    within_root and resolved.exists(),
                    f"{link} -> {resolved}",
                )
            )
    return checks


def validate_test_prompts(skill_name: str, path: Path) -> list[CheckResult]:
    scope = str(path.parent.name)
    checks: list[CheckResult] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [result(scope, "test-prompts-json", False, str(exc))]

    checks.append(result(scope, "test-skill-name", data.get("skill") == skill_name, str(data.get("skill"))))
    checks.append(result(scope, "test-version", data.get("version") == "0.1.0", str(data.get("version"))))
    checks.append(result(scope, "darwin-compatible", data.get("darwin_compatible") is True, str(data.get("darwin_compatible"))))
    cases = data.get("test_cases")
    if not isinstance(cases, list):
        return checks + [result(scope, "test-cases", False, "test_cases is not a list")]

    counts = {kind: 0 for kind in ("should_trigger", "should_not_trigger", "edge_case")}
    ids: list[str] = []
    complete = True
    for case in cases:
        if not isinstance(case, dict):
            complete = False
            continue
        kind = case.get("type")
        if kind in counts:
            counts[kind] += 1
        ids.append(str(case.get("id", "")))
        complete = complete and all(
            isinstance(case.get(key), str) and bool(case[key].strip())
            for key in ("id", "type", "prompt", "expected_behavior", "notes")
        )
    checks.append(result(scope, "test-count", len(cases) == 8, f"found {len(cases)}"))
    checks.append(result(scope, "test-type-counts", counts == {"should_trigger": 3, "should_not_trigger": 3, "edge_case": 2}, json.dumps(counts, sort_keys=True)))
    checks.append(result(scope, "test-case-fields", complete, "all five fields are non-empty strings" if complete else "missing or invalid field"))
    checks.append(result(scope, "test-id-uniqueness", len(ids) == len(set(ids)) and all(ids), f"{len(set(ids))}/{len(ids)} unique"))
    bait_cases = [case for case in cases if isinstance(case, dict) and case.get("type") == "should_not_trigger"]
    sibling_bait = any(
        "\u8de8 skill" in str(case.get("notes", "")).lower()
        or "sibling" in str(case.get("notes", "")).lower()
        or any(other in str(case.get("expected_behavior", "")) for other in EXPECTED_SKILLS - {skill_name})
        for case in bait_cases
    )
    checks.append(result(scope, "cross-skill-bait", sibling_bait, "at least one sibling bait" if sibling_bait else "missing sibling bait"))
    checks.append(result(scope, "minimum-pass-rate", data.get("minimum_pass_rate") == 1.0, str(data.get("minimum_pass_rate"))))
    return checks


def validate_skill(root: Path, skill_dir: Path) -> list[CheckResult]:
    name = skill_dir.name
    scope = f"skills/{name}"
    checks: list[CheckResult] = []
    for relative in sorted(SKILL_REQUIRED):
        path = skill_dir / relative
        checks.append(result(scope, f"required:{relative}", path.is_file(), "present" if path.is_file() else "missing"))
    if not (skill_dir / "SKILL.md").is_file():
        return checks

    try:
        frontmatter = parse_frontmatter(skill_dir / "SKILL.md")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return checks + [result(scope, "frontmatter", False, str(exc))]

    unexpected = sorted(set(frontmatter) - ALLOWED_FRONTMATTER)
    checks.append(result(scope, "frontmatter-keys", not unexpected, "allowed only" if not unexpected else ", ".join(unexpected)))
    declared_name = frontmatter.get("name")
    checks.append(result(scope, "name-match", declared_name == name and bool(NAME_PATTERN.fullmatch(name)), f"declared={declared_name!r}"))
    description = frontmatter.get("description")
    valid_description = isinstance(description, str) and 20 <= len(description.strip()) <= 1024 and "<" not in description and ">" not in description
    checks.append(result(scope, "description", valid_description, f"length={len(description.strip()) if isinstance(description, str) else 'invalid'}"))
    checks.append(result(scope, "license", frontmatter.get("license") == "AGPL-3.0-or-later", str(frontmatter.get("license"))))

    metadata = frontmatter.get("metadata")
    metadata_ok = isinstance(metadata, dict)
    missing_metadata = sorted(REQUIRED_METADATA - set(metadata or {})) if metadata_ok else sorted(REQUIRED_METADATA)
    checks.append(result(scope, "metadata-fields", metadata_ok and not missing_metadata, "complete" if metadata_ok and not missing_metadata else ", ".join(missing_metadata)))
    if metadata_ok:
        checks.append(result(scope, "metadata-version", metadata.get("version") == "0.1.0", str(metadata.get("version"))))
        checks.append(result(scope, "metadata-provenance", metadata.get("provenance") in PROVENANCE_VALUES, str(metadata.get("provenance"))))
        checks.append(result(scope, "metadata-tags", isinstance(metadata.get("tags"), list) and bool(metadata.get("tags")), str(metadata.get("tags"))))
        checks.append(result(scope, "metadata-related", isinstance(metadata.get("related_skills"), list), str(metadata.get("related_skills"))))

    openai_path = skill_dir / "agents" / "openai.yaml"
    if openai_path.is_file():
        try:
            openai = yaml.safe_load(openai_path.read_text(encoding="utf-8"))
            interface = openai.get("interface") if isinstance(openai, dict) else None
            policy = openai.get("policy") if isinstance(openai, dict) else None
            interface_ok = isinstance(interface, dict) and all(
                isinstance(interface.get(key), str) and bool(interface[key].strip())
                for key in ("display_name", "short_description", "default_prompt")
            )
            checks.append(result(scope, "openai-interface", interface_ok, "complete" if interface_ok else "missing interface string"))
            default_prompt = interface.get("default_prompt", "") if isinstance(interface, dict) else ""
            checks.append(result(scope, "openai-default-prompt", f"${name}" in default_prompt, default_prompt))
            checks.append(result(scope, "implicit-invocation", isinstance(policy, dict) and policy.get("allow_implicit_invocation") is True, str(policy)))
        except (OSError, yaml.YAMLError) as exc:
            checks.append(result(scope, "openai-yaml", False, str(exc)))

    test_path = skill_dir / "test-prompts.json"
    if test_path.is_file():
        checks.extend(validate_test_prompts(name, test_path))

    results_path = skill_dir / "test-results.md"
    if results_path.is_file():
        text = results_path.read_text(encoding="utf-8")
        checks.append(result(scope, "test-results-complete", "8/8" in text and "100%" in text, "contains final 8/8 and 100%" if "8/8" in text and "100%" in text else "final routing result absent"))

    for path in skill_dir.rglob("*"):
        checks.append(result(scope, "no-symlink", not path.is_symlink(), str(path.relative_to(root))))

    markdown_paths = sorted(path for path in skill_dir.rglob("*.md") if path.is_file())
    checks.extend(check_links(root, markdown_paths))
    return checks


def validate_release(root: Path) -> list[CheckResult]:
    root = root.resolve()
    checks: list[CheckResult] = []
    for relative in sorted(ROOT_REQUIRED):
        path = root / relative
        checks.append(result("root", f"required:{relative}", path.is_file(), "present" if path.is_file() else "missing"))

    skills_root = root / "skills"
    actual_skills = {
        path.name for path in skills_root.iterdir() if path.is_dir()
    } if skills_root.is_dir() else set()
    checks.append(result("root", "skill-set", actual_skills == EXPECTED_SKILLS, f"actual={sorted(actual_skills)}"))
    for name in sorted(EXPECTED_SKILLS & actual_skills):
        checks.extend(validate_skill(root, skills_root / name))

    requirements = root / "requirements-dev.txt"
    if requirements.is_file():
        lines = [line.strip() for line in requirements.read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
        checks.append(result("root", "dependencies-pinned", bool(lines) and all("==" in line for line in lines), str(lines)))

    license_path = root / "LICENSE"
    if license_path.is_file():
        licence = license_path.read_text(encoding="utf-8", errors="replace")
        checks.append(result("root", "agpl-license", "GNU AFFERO GENERAL PUBLIC LICENSE" in licence and "Version 3" in licence, "AGPL-3.0 text present"))

    notices_path = root / "THIRD_PARTY_NOTICES.md"
    if notices_path.is_file():
        notices = notices_path.read_text(encoding="utf-8")
        required_notices = ("Carnegie Mellon University", "Max Forsey", "MIT License", "Cangjie Skill")
        checks.append(result("root", "third-party-notices", all(item in notices for item in required_notices), ", ".join(required_notices)))

    published_paths = [
        path for path in root.rglob("*")
        if path.is_file() and ".git" not in path.parts and "books" not in path.parts
    ]
    pdfs = [str(path.relative_to(root)) for path in published_paths if path.suffix.lower() == ".pdf"]
    checks.append(result("root", "no-published-pdf", not pdfs, str(pdfs)))
    symlinks = [str(path.relative_to(root)) for path in root.rglob("*") if path.is_symlink() and ".git" not in path.parts]
    checks.append(result("root", "no-symlinks", not symlinks, str(symlinks)))

    unfinished_terms = ("TO" + "DO", "FIX" + "ME")
    unfinished_hits: list[str] = []
    for path in published_paths:
        if path.name == "LICENSE" or path.suffix.lower() in {".pyc", ".png", ".jpg", ".jpeg", ".gif"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(re.search(rf"\b{term}\b", text, re.IGNORECASE) for term in unfinished_terms):
            unfinished_hits.append(str(path.relative_to(root)))
    checks.append(result("root", "no-unfinished-markers", not unfinished_hits, str(unfinished_hits)))

    markdown_paths = [
        path for path in published_paths
        if path.suffix.lower() == ".md" and "skills" not in path.parts
    ]
    checks.extend(check_links(root, sorted(markdown_paths)))

    for path in published_paths:
        relative = str(path.relative_to(root))
        if path.suffix.lower() == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
                checks.append(result(relative, "json-parse", True, "valid"))
            except (OSError, json.JSONDecodeError) as exc:
                checks.append(result(relative, "json-parse", False, str(exc)))
        elif path.suffix.lower() in {".yaml", ".yml"}:
            try:
                yaml.safe_load(path.read_text(encoding="utf-8"))
                checks.append(result(relative, "yaml-parse", True, "valid"))
            except (OSError, yaml.YAMLError) as exc:
                checks.append(result(relative, "yaml-parse", False, str(exc)))
    return checks


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--json", action="store_true", help="emit machine-readable results")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).expanduser().resolve()
    try:
        checks = validate_release(root)
    except Exception as exc:
        print(f"validator execution error: {exc}", file=sys.stderr)
        return 2
    failures = [check for check in checks if not check.passed]
    if args.json:
        print(json.dumps({"root": str(root), "passed": not failures, "checks": [asdict(check) for check in checks]}, ensure_ascii=False, indent=2))
    else:
        for check in checks:
            marker = "PASS" if check.passed else "FAIL"
            print(f"[{marker}] {check.scope} :: {check.check} :: {check.detail}")
        print(f"summary: {len(checks) - len(failures)}/{len(checks)} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
