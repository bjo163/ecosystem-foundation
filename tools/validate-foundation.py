#!/usr/bin/env python3
"""Validate a repository against the ecosystem-foundation contract.

Stdlib-only so it can run anywhere a supported Python interpreter exists.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ALIAS_GROUPS = {
    "documentation": {"documentation", "docs"},
    "configuration": {"configuration", "config"},
    "deployment": {"deployment", "deploy"},
    "infrastructure": {"infrastructure", "infra"},
    "assets": {"assets", "static"},
    "scripts": {"scripts", "script"},
    "tools": {"tools", "tooling"},
    "tests": {"tests", "test"},
    "examples": {"examples", "example"},
    "fixtures": {"fixtures", "fixture"},
    "source": {"source", "src"},
}

ROOT_FILES = {"README.md", "LICENSE", ".gitignore"}
MANIFEST_NAMES = {
    "package.json", "pnpm-workspace.yaml", "yarn.lock", "package-lock.json",
    "Cargo.toml", "Cargo.lock", "go.mod", "go.sum", "pyproject.toml",
    "requirements.txt", "poetry.lock", "pom.xml", "build.gradle", "build.gradle.kts",
    "settings.gradle", "settings.gradle.kts", "Gemfile", "mix.exs", "composer.json",
}
GENERATED_NAMES = {"target", "dist", "build", "coverage", ".cache", ".next", ".turbo"}


def load_contract(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def check(root: Path, contract: dict) -> list[str]:
    errors: list[str] = []
    canonical = set(contract["canonicalVocabulary"])

    for required in ("contractVersion", "hierarchy", "canonicalVocabulary", "profiles"):
        if required not in contract:
            errors.append(f"contract missing field: {required}")

    for name in contract.get("canonicalVocabulary", []):
        if not name or name != name.strip() or "/" in name or "\\" in name:
            errors.append(f"invalid canonical vocabulary entry: {name!r}")

    if not (root / "README.md").exists():
        errors.append("missing repository root README.md")

    for alias_name, aliases in ALIAS_GROUPS.items():
        present = [name for name in aliases if (root / name).exists()]
        if len(present) > 1:
            errors.append(f"overlapping directories for {alias_name}: {', '.join(sorted(present))}")

    manifest_files = [p.name for p in root.iterdir() if p.is_file() and p.name in MANIFEST_NAMES]
    nested_manifest_count = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.parent == root:
            continue
        if path.name in MANIFEST_NAMES:
            nested_manifest_count += 1
    if manifest_files or nested_manifest_count:
        # Nested manifests are allowed for monorepos; root manifests are the default rule.
        pass

    for name in GENERATED_NAMES:
        if (root / name).exists():
            errors.append(f"generated output should not be committed by default: {name}")

    for child in root.iterdir():
        if child.is_dir() and child.name in canonical:
            continue
        if child.is_file() and child.name in ROOT_FILES:
            continue
        if child.is_file() and child.name in MANIFEST_NAMES:
            continue
        if child.name.startswith("."):
            continue
        # Non-canonical root entries are informational, not errors.

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument(
        "--contract",
        default="specifications/foundation-contract.instance.json",
        help="path to the normative contract instance",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    contract_path = (root / args.contract).resolve()
    if not contract_path.exists():
        print(f"ERROR: contract not found: {contract_path}")
        return 2

    try:
        contract = load_contract(contract_path)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read contract: {exc}")
        return 2

    errors = check(root, contract)
    if errors:
        print("Foundation validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Foundation validation: PASS (contract {contract['contractVersion']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
