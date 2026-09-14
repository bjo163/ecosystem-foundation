#!/usr/bin/env python3
"""Scaffold a repository from the Ecosystem Foundation profiles.

Usage:
    python tools/repo-init.py library my-library
    python tools/repo-init.py application my-app --path ./my-app
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

PROFILES: dict[str, tuple[str, ...]] = {
    "library": ("source", "tests", "examples", "documentation"),
    "application": ("source", "tests", "configuration", "documentation", "deployment"),
    "service": (
        "source",
        "tests",
        "configuration",
        "specifications",
        "infrastructure",
        "deployment",
        "documentation",
    ),
    "cli": ("source", "tests", "examples", "documentation"),
    "monorepo": (
        "source",
        "tests",
        "examples",
        "tools",
        "scripts",
        "configuration",
        "documentation",
        "specifications",
        "infrastructure",
        "deployment",
    ),
}

ROOT_FILES = {
    "README.md": "# {name}\n\nCreated from Ecosystem Foundation profile `{profile}`.\n",
    ".gitignore": "# Generated/build output\n.env\n.env.*\n*.log\ncoverage/\ndist/\nbuild/\ntarget/\n",
}


def safe_name(value: str) -> str:
    cleaned = value.strip().replace("\\", "-").replace("/", "-")
    if not cleaned or cleaned in {".", ".."}:
        raise ValueError("repository name must not be empty or a path traversal value")
    if any(ord(ch) < 32 for ch in cleaned):
        raise ValueError("repository name contains a control character")
    return cleaned


def create_structure(destination: Path, profile: str, name: str) -> list[Path]:
    created: list[Path] = []
    destination.mkdir(parents=True, exist_ok=False)
    for directory in PROFILES[profile]:
        path = destination / directory
        path.mkdir(parents=True, exist_ok=False)
        (path / ".gitkeep").write_text("", encoding="utf-8")
        created.append(path)

    for filename, template in ROOT_FILES.items():
        path = destination / filename
        path.write_text(template.format(name=name, profile=profile), encoding="utf-8")
        created.append(path)

    metadata = {
        "foundation": "ecosystem-foundation",
        "foundation_contract": "0.2",
        "profile": profile,
        "name": name,
    }
    metadata_path = destination / ".ecosystem.json"
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    created.append(metadata_path)
    return created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a repository from an Ecosystem Foundation profile.")
    parser.add_argument("profile", choices=sorted(PROFILES))
    parser.add_argument("name")
    parser.add_argument("--path", type=Path, help="Destination directory; defaults to ./<name>")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    name = safe_name(args.name)
    destination = (args.path or Path.cwd() / name).resolve()
    if destination.exists():
        raise SystemExit(f"error: destination already exists: {destination}")
    created = create_structure(destination, args.profile, name)
    print(f"created {destination}")
    for path in created:
        print(f"  {path.relative_to(destination)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
