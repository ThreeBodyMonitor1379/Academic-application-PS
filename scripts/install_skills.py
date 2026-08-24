#!/usr/bin/env python3
"""Install this repository's Codex skills without overwriting conflicts."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class InstallResult:
    skill: str
    status: str
    source: str
    target: str
    detail: str


class InstallerInputError(ValueError):
    """Raised for an invalid source package or invocation."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_manifest(directory: Path) -> dict[str, str]:
    if not directory.is_dir():
        raise InstallerInputError(f"not a directory: {directory}")
    manifest: dict[str, str] = {}
    for path in sorted(directory.rglob("*")):
        if path.is_symlink():
            raise InstallerInputError(f"symbolic links are not allowed: {path}")
        if path.is_file():
            manifest[path.relative_to(directory).as_posix()] = sha256_file(path)
    return manifest


def frontmatter_name(skill_md: Path) -> str:
    if not skill_md.is_file():
        raise InstallerInputError(f"missing SKILL.md: {skill_md.parent}")
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise InstallerInputError(f"missing YAML frontmatter: {skill_md}")
    end = text.find("\n---", 4)
    if end < 0:
        raise InstallerInputError(f"unterminated YAML frontmatter: {skill_md}")
    match = re.search(r"^name:\s*[\"']?([^\"'\n]+)[\"']?\s*$", text[4:end], re.MULTILINE)
    if not match:
        raise InstallerInputError(f"frontmatter name is missing: {skill_md}")
    return match.group(1).strip()


def validate_source_skill(source: Path) -> str:
    name = source.name
    if not NAME_PATTERN.fullmatch(name):
        raise InstallerInputError(f"invalid skill directory name: {name}")
    declared = frontmatter_name(source / "SKILL.md")
    if declared != name:
        raise InstallerInputError(
            f"directory/name mismatch for {source}: declared {declared!r}"
        )
    required = [
        source / "agents" / "openai.yaml",
        source / "test-prompts.json",
        source / "test-results.md",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise InstallerInputError("missing required skill files: " + ", ".join(missing))
    file_manifest(source)
    return name


def install_one(source: Path, target_root: Path) -> InstallResult:
    name = validate_source_skill(source)
    target = target_root / name
    source_manifest = file_manifest(source)

    if not target.exists():
        target_root.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target, symlinks=False)
        copied_manifest = file_manifest(target)
        if copied_manifest != source_manifest:
            raise InstallerInputError(f"post-copy manifest mismatch: {name}")
        return InstallResult(
            skill=name,
            status="installed",
            source=str(source.resolve()),
            target=str(target.resolve()),
            detail=f"installed {len(source_manifest)} files",
        )

    if not target.is_dir() or target.is_symlink():
        return InstallResult(
            skill=name,
            status="conflict",
            source=str(source.resolve()),
            target=str(target.absolute()),
            detail="target exists but is not a regular directory; left unchanged",
        )

    target_manifest = file_manifest(target)
    if target_manifest == source_manifest:
        return InstallResult(
            skill=name,
            status="identical",
            source=str(source.resolve()),
            target=str(target.resolve()),
            detail=f"identical relative file list and SHA-256 manifest ({len(source_manifest)} files)",
        )

    source_files = set(source_manifest)
    target_files = set(target_manifest)
    changed = sorted(
        path
        for path in source_files & target_files
        if source_manifest[path] != target_manifest[path]
    )
    missing = sorted(source_files - target_files)
    extra = sorted(target_files - source_files)
    summary = {
        "changed": changed,
        "missing_in_target": missing,
        "extra_in_target": extra,
    }
    return InstallResult(
        skill=name,
        status="conflict",
        source=str(source.resolve()),
        target=str(target.resolve()),
        detail="manifest differs; left unchanged: " + json.dumps(summary, ensure_ascii=False),
    )


def discover_target(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return (Path(codex_home).expanduser().resolve() / "skills")
    return (Path.home() / ".codex" / "skills").resolve()


def discover_sources(source_root: Path, requested: list[str] | None) -> list[Path]:
    if not source_root.is_dir():
        raise InstallerInputError(f"skills source directory not found: {source_root}")
    available = {
        path.name: path
        for path in source_root.iterdir()
        if path.is_dir() and not path.is_symlink()
    }
    names = sorted(requested or available)
    unknown = [name for name in names if name not in available]
    if unknown:
        raise InstallerInputError("unknown requested skills: " + ", ".join(unknown))
    return [available[name] for name in names]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install complete skill directories; never overwrite or mix conflicts."
    )
    parser.add_argument(
        "--source-dir",
        default=str(Path(__file__).resolve().parents[1] / "skills"),
        help="repository skills directory",
    )
    parser.add_argument(
        "--target-dir",
        help="Codex skills directory; defaults to CODEX_HOME/skills or ~/.codex/skills",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="skills",
        help="install only this skill; repeat for multiple skills",
    )
    parser.add_argument("--json", action="store_true", help="emit a JSON report")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        source_root = Path(args.source_dir).expanduser().resolve()
        target_root = discover_target(args.target_dir)
        sources = discover_sources(source_root, args.skills)
        results = [install_one(source, target_root) for source in sources]
    except InstallerInputError as exc:
        print(f"installer input error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(
            json.dumps(
                {
                    "target_dir": str(target_root),
                    "results": [asdict(result) for result in results],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"target: {target_root}")
        for result in results:
            print(f"{result.skill}: {result.status} - {result.detail}")

    return 1 if any(result.status == "conflict" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
