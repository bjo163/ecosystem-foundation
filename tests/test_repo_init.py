from __future__ import annotations

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "repo-init.py"
spec = importlib.util.spec_from_file_location("repo_init", MODULE_PATH)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_all_profiles_have_unique_names() -> None:
    assert set(module.PROFILES) == {"library", "application", "service", "cli", "monorepo"}


def test_safe_name_rejects_empty_and_traversal() -> None:
    for value in ("", ".", ".."):
        try:
            module.safe_name(value)
        except ValueError:
            pass
        else:
            raise AssertionError(f"accepted invalid name: {value!r}")


def test_create_structure(tmp_path: Path) -> None:
    destination = tmp_path / "demo"
    created = module.create_structure(destination, "library", "demo")
    assert (destination / "source" / ".gitkeep").exists()
    assert (destination / "tests" / ".gitkeep").exists()
    assert (destination / "README.md").read_text(encoding="utf-8").startswith("# demo")
    assert (destination / ".ecosystem.json").exists()
    assert len(created) >= 5
