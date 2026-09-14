from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "repo-init.py"
spec = importlib.util.spec_from_file_location("repo_init", MODULE_PATH)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class RepoInitTests(unittest.TestCase):
    def test_all_profiles_are_defined(self) -> None:
        self.assertEqual(set(module.PROFILES), {"library", "application", "service", "cli", "monorepo"})

    def test_safe_name_rejects_empty_and_traversal(self) -> None:
        for value in ("", ".", ".."):
            with self.assertRaises(ValueError):
                module.safe_name(value)

    def test_create_structure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "demo"
            created = module.create_structure(destination, "library", "demo")
            self.assertTrue((destination / "source" / ".gitkeep").exists())
            self.assertTrue((destination / "tests" / ".gitkeep").exists())
            self.assertTrue((destination / "README.md").read_text(encoding="utf-8").startswith("# demo"))
            self.assertTrue((destination / ".ecosystem.json").exists())
            self.assertGreaterEqual(len(created), 5)


if __name__ == "__main__":
    unittest.main()
