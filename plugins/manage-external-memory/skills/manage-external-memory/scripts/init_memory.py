#!/usr/bin/env python3
"""Create a new, tool-neutral external-memory workspace without overwriting files."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "system-template"
ADAPTER_ROOT = SKILL_ROOT / "assets" / "adapters"

CORE_FILES = (
    ".gitignore",
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

EMPTY_DIRS = (
    "Workspaces/Projects",
    "Workspaces/Tasks",
)

ADAPTERS = {
    "codex": ("codex.md", "AGENTS.md"),
    "claude": ("claude.md", "CLAUDE.md"),
    "workbuddy": ("workbuddy.md", "WORKBUDDY.md"),
    "hermes": ("hermes.md", "HERMES.MD"),
}


class InitializationError(RuntimeError):
    """Raised when initialization cannot proceed safely."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a new Markdown external-memory workspace. The target path must "
            "not already exist; this command never merges or overwrites."
        )
    )
    parser.add_argument("--root", required=True, help="New workspace root to create")
    parser.add_argument(
        "--owner",
        default="用户",
        help="Display name used in blank templates; do not provide sensitive data",
    )
    parser.add_argument(
        "--adapters",
        default="codex",
        help="Comma-separated adapters: codex,claude,workbuddy,hermes,all,none",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned files without creating anything",
    )
    return parser.parse_args()


def parse_adapters(raw_value: str) -> list[str]:
    values = [item.strip().lower() for item in raw_value.split(",") if item.strip()]
    if not values:
        values = ["codex"]
    if "all" in values:
        return list(ADAPTERS)
    if "none" in values:
        if len(values) != 1:
            raise InitializationError("'none' cannot be combined with other adapters")
        return []
    unknown = sorted(set(values) - set(ADAPTERS))
    if unknown:
        raise InitializationError(f"Unknown adapter(s): {', '.join(unknown)}")
    return list(dict.fromkeys(values))


def normalize_target(raw_path: str) -> Path:
    if os.name != "nt" and len(raw_path) >= 2 and raw_path[0].isalpha() and raw_path[1] == ":":
        raise InitializationError(
            "Windows-style drive path detected in non-Windows Python. "
            "In WSL, use a path such as /mnt/d/My-AI; otherwise run this command with Windows Python."
        )
    target = Path(raw_path).expanduser()
    if target.exists() and target.is_symlink():
        raise InitializationError("Target path is a symlink; choose a new explicit path")
    target = target.absolute()
    anchor = Path(target.anchor)
    if target == anchor:
        raise InitializationError("Refusing to use a filesystem root as the target")
    if target.exists():
        raise InitializationError(
            "Target already exists. Choose a new path; this initializer never merges or overwrites."
        )
    return target


def normalize_owner(raw_value: str) -> str:
    owner = raw_value.strip() or "用户"
    if "\n" in owner or "\r" in owner:
        raise InitializationError("Owner label must be a single line")
    if "{{" in owner or "}}" in owner:
        raise InitializationError("Owner label cannot contain template markers")
    if len(owner) > 80:
        raise InitializationError("Owner label must be 80 characters or fewer")
    return owner


def render_template(source: Path, replacements: dict[str, str]) -> str:
    content = source.read_text(encoding="utf-8")
    for marker, value in replacements.items():
        content = content.replace(marker, value)
    return content


def planned_files(adapters: list[str]) -> list[str]:
    files = list(CORE_FILES)
    files.extend(ADAPTERS[name][1] for name in adapters)
    return sorted(files)


def validate_assets(adapters: list[str]) -> None:
    missing = [str(TEMPLATE_ROOT / item) for item in CORE_FILES if not (TEMPLATE_ROOT / item).is_file()]
    for name in adapters:
        source_name, _ = ADAPTERS[name]
        source = ADAPTER_ROOT / source_name
        if not source.is_file():
            missing.append(str(source))
    if missing:
        raise InitializationError("Skill assets are incomplete:\n- " + "\n- ".join(missing))


def create_workspace(target: Path, owner: str, adapters: list[str]) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{target.name}-building-", dir=target.parent))
    try:
        memory_path = target / "Memory"
        replacements = {
            "{{OWNER}}": owner.strip() or "用户",
            "{{DATE}}": date.today().isoformat(),
            "{{ROOT_PATH}}": str(target),
            "{{MEMORY_PATH}}": str(memory_path),
        }

        for relative in CORE_FILES:
            source = TEMPLATE_ROOT / relative
            destination = temporary / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(render_template(source, replacements), encoding="utf-8")

        for relative in EMPTY_DIRS:
            (temporary / relative).mkdir(parents=True, exist_ok=True)

        for adapter in adapters:
            source_name, destination_name = ADAPTERS[adapter]
            destination = temporary / destination_name
            destination.write_text(
                render_template(ADAPTER_ROOT / source_name, replacements),
                encoding="utf-8",
            )

        if target.exists():
            raise InitializationError("Target appeared during creation; no files were installed")
        temporary.rename(target)
    except Exception:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise


def main() -> int:
    try:
        args = parse_args()
        adapters = parse_adapters(args.adapters)
        target = normalize_target(args.root)
        owner = normalize_owner(args.owner)
        validate_assets(adapters)
        files = planned_files(adapters)

        print(f"Target: {target}")
        print(f"Owner label: {owner}")
        print(f"Adapters: {', '.join(adapters) if adapters else 'none'}")
        print("Planned files:")
        for relative in files:
            print(f"  - {relative}")

        if args.dry_run:
            print("[OK] Dry run only; no files were created.")
            return 0

        create_workspace(target, owner, adapters)
        print(f"[OK] External-memory workspace created at: {target}")
        return 0
    except (InitializationError, OSError, UnicodeError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
