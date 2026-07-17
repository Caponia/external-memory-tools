#!/usr/bin/env python3
"""Validate structure and filename-level safety of an external-memory workspace."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "START-HERE.md",
    "Memory/README.md",
    "Memory/RULES.md",
    "Memory/PROFILE.md",
    "Memory/PROJECTS.md",
    "Memory/CHANGELOG.md",
    "Memory/INBOX/README.md",
    "Memory/WORKFLOWS/README.md",
    "Workspaces/README.md",
    "Exports/README.md",
    "Archive/README.md",
)

OPTIONAL_ADAPTERS = ("AGENTS.md", "CLAUDE.md", "WORKBUDDY.md", "HERMES.MD")
SENSITIVE_SUFFIXES = {".key", ".pem", ".pfx", ".p12"}
PLACEHOLDER_PREFIX = "{{"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate required files, unresolved template markers, and sensitive-looking "
            "filenames. File contents are not scanned for credentials."
        )
    )
    parser.add_argument("--root", required=True, help="External-memory workspace root")
    return parser.parse_args()


def looks_sensitive(path: Path) -> bool:
    name = path.name.lower()
    if name == ".env.example":
        return False
    return (
        name == ".env"
        or name.startswith(".env.")
        or name == ".dev.vars"
        or name.startswith("credentials")
        or name.startswith("secrets")
        or path.suffix.lower() in SENSITIVE_SUFFIXES
    )


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().absolute()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print(f"[ERROR] Workspace root does not exist or is not a directory: {root}", file=sys.stderr)
        return 1

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing required file: {relative}")

    managed_files = [root / relative for relative in REQUIRED_FILES]
    managed_files.extend(root / name for name in OPTIONAL_ADAPTERS if (root / name).is_file())
    for path in managed_files:
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {path.relative_to(root)} as UTF-8: {exc}")
            continue
        if PLACEHOLDER_PREFIX in content and "}}" in content:
            errors.append(f"Unresolved template marker in: {path.relative_to(root)}")

    readme = root / "Memory" / "README.md"
    if readme.is_file():
        content = readme.read_text(encoding="utf-8")
        for marker in ("RULES.md", "PROFILE.md", "PROJECTS.md", "INBOX", "CHANGELOG.md"):
            if marker not in content:
                errors.append(f"Memory/README.md does not route to {marker}")

    rules = root / "Memory" / "RULES.md"
    if rules.is_file():
        content = rules.read_text(encoding="utf-8")
        for marker in ("默认只读", "INBOX", "敏感"):
            if marker not in content:
                errors.append(f"Memory/RULES.md is missing governance marker: {marker}")

    for path in root.rglob("*"):
        if path.is_file() and looks_sensitive(path):
            errors.append(f"Sensitive-looking filename found: {path.relative_to(root)}")

    present_adapters = [name for name in OPTIONAL_ADAPTERS if (root / name).is_file()]
    if not present_adapters:
        warnings.append("No tool adapter was found; tools must be configured manually")

    for message in warnings:
        print(f"[WARN] {message}")
    if errors:
        for message in errors:
            print(f"[ERROR] {message}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"[OK] Structure is valid: {root}")
    print(f"[OK] Tool adapters: {', '.join(present_adapters) if present_adapters else 'none'}")
    print("[OK] No sensitive-looking filenames were found.")
    print("[INFO] File contents were not scanned for credentials; review private content manually.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
