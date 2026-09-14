from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "validate-foundation.py"

spec = importlib.util.spec_from_file_location("validate_foundation", MODULE_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def contract() -> dict:
    return json.loads((ROOT / "specifications" / "foundation-contract.instance.json").read_text(encoding="utf-8"))


def test_minimal_repository_passes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "README.md").write_text("# test\n", encoding="utf-8")
        assert validator.check(root, contract()) == []


def test_overlapping_aliases_fail() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "README.md").write_text("# test\n", encoding="utf-8")
        (root / "docs").mkdir()
        (root / "documentation").mkdir()
        errors = validator.check(root, contract())
        assert any("overlapping directories for documentation" in error for error in errors)


def test_generated_output_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "README.md").write_text("# test\n", encoding="utf-8")
        (root / "target").mkdir()
        errors = validator.check(root, contract())
        assert any("generated output" in error for error in errors)
