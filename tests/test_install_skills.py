from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "install_skills.py"
SPEC = importlib.util.spec_from_file_location("install_skills", MODULE_PATH)
assert SPEC and SPEC.loader
install_skills = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = install_skills
SPEC.loader.exec_module(install_skills)


class SafeInstallerTests(unittest.TestCase):
    def make_source(self, root: Path, name: str = "example-skill") -> Path:
        source = root / "source" / name
        (source / "agents").mkdir(parents=True)
        (source / "references").mkdir()
        (source / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Test skill.\n---\n\n# Test\n",
            encoding="utf-8",
        )
        (source / "agents" / "openai.yaml").write_text(
            "interface:\n  display_name: \"Test\"\n",
            encoding="utf-8",
        )
        (source / "test-prompts.json").write_text("{}\n", encoding="utf-8")
        (source / "test-results.md").write_text("# Results\n", encoding="utf-8")
        (source / "references" / "guide.md").write_text("guide\n", encoding="utf-8")
        return source

    def test_absent_target_is_installed_with_identical_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = self.make_source(root)
            target_root = root / "target"
            result = install_skills.install_one(source, target_root)
            self.assertEqual(result.status, "installed")
            self.assertEqual(
                install_skills.file_manifest(source),
                install_skills.file_manifest(target_root / source.name),
            )

    def test_identical_target_is_not_rewritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = self.make_source(root)
            target_root = root / "target"
            first = install_skills.install_one(source, target_root)
            before = install_skills.file_manifest(target_root / source.name)
            second = install_skills.install_one(source, target_root)
            after = install_skills.file_manifest(target_root / source.name)
            self.assertEqual(first.status, "installed")
            self.assertEqual(second.status, "identical")
            self.assertEqual(before, after)

    def test_conflicting_target_is_left_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = self.make_source(root)
            target_root = root / "target"
            install_skills.install_one(source, target_root)
            target_skill = target_root / source.name
            (target_skill / "references" / "guide.md").write_text(
                "local change\n", encoding="utf-8"
            )
            before = install_skills.file_manifest(target_skill)
            result = install_skills.install_one(source, target_root)
            after = install_skills.file_manifest(target_skill)
            self.assertEqual(result.status, "conflict")
            self.assertEqual(before, after)

    def test_file_at_target_is_a_non_destructive_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = self.make_source(root)
            target_root = root / "target"
            target_root.mkdir()
            target = target_root / source.name
            target.write_text("do not replace\n", encoding="utf-8")
            result = install_skills.install_one(source, target_root)
            self.assertEqual(result.status, "conflict")
            self.assertEqual(target.read_text(encoding="utf-8"), "do not replace\n")


if __name__ == "__main__":
    unittest.main()
