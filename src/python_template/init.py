"""Project initialization from the python-template."""

import shutil
import sys
from datetime import datetime
from importlib.resources import files
from pathlib import Path
from importlib.resources.abc import Traversable

# File extensions that should be processed for placeholder replacement
_TEXT_EXTENSIONS = frozenset(
    {".py", ".toml", ".yml", ".yaml", ".md", ".txt", ".cfg", ".ini", ".json", ".j2"}
)
# Files without extensions that should still be processed
_TEXT_NAMES = frozenset({".gitignore", ".codespellrc", "LICENSE", "Makefile"})

# Placeholder prefix used in the template directory name
_PKG_PLACEHOLDER = "{{package_name}}"

# Set of all known placeholder keys
_PLACEHOLDER_KEYS = frozenset(
    {
        "{{project_name}}",
        "{{package_name}}",
        "{{author_name}}",
        "{{author_email}}",
        "{{description}}",
        "{{github_user}}",
        "{{year}}",
    }
)


def _to_package_name(project_name: str) -> str:
    """Convert a project name to a valid Python package name."""
    return project_name.replace("-", "_").replace(".", "_")


def _should_process(name: str, suffix: str) -> bool:
    """Check if a file should be processed for placeholder replacement."""
    return suffix.lower() in _TEXT_EXTENSIONS or name in _TEXT_NAMES


def _apply_replacements(content: str, replacements: dict[str, str]) -> str:
    """Apply placeholder replacements to a string."""
    for old, new in replacements.items():
        content = content.replace(old, new)
    return content


def _copy_tree(
    src: Traversable,
    dst: Path,
    replacements: dict[str, str],
    *,
    rename_pkg: str,
) -> None:
    """Recursively copy template tree, processing files along the way.

    Parameters
    ----------
    src : Traversable
        Source template directory.
    dst : Path
        Destination directory on disk.
    replacements : dict
        Placeholder → value mapping.
    rename_pkg : str
        Actual package name to use when renaming the
        ``{{package_name}}`` directory under ``src/``.
    """
    for item in src.iterdir():
        # Compute destination name, applying renames
        dest_name = item.name
        if item.is_dir() and item.name == _PKG_PLACEHOLDER:
            dest_name = rename_pkg

        dest_path = dst / dest_name

        if item.is_dir():
            dest_path.mkdir(parents=True, exist_ok=True)
            _copy_tree(item, dest_path, replacements, rename_pkg=rename_pkg)
        else:
            # Strip .j2 suffix from template files (used to hide from linters)
            if dest_name.endswith(".j2"):
                dest_name = dest_name[:-3]
                dest_path = dst / dest_name
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            if _should_process(
                item.name, item.suffix if hasattr(item, "suffix") else ""
            ):
                content = item.read_text(encoding="utf-8")
                content = _apply_replacements(content, replacements)
                dest_path.write_text(content, encoding="utf-8")
            else:
                dest_path.write_bytes(item.read_bytes())


def init_project(
    project_name: str,
    *,
    target_dir: str | None = None,
    author: str | None = None,
    email: str | None = None,
    description: str | None = None,
    github_user: str | None = None,
    force: bool = False,
) -> Path:
    """Initialize a new Python project from the template.

    Parameters
    ----------
    project_name : str
        The name of the project (hyphenated, e.g. ``my-project``).
    target_dir : str or None
        Directory to create. Defaults to ``project_name``.
    author : str or None
        Author name for pyproject.toml.
    email : str or None
        Author email.
    description : str or None
        Short project description.
    github_user : str or None
        GitHub username for URLs in config files.
    force : bool
        Overwrite target directory if it already exists.

    Returns
    -------
    Path
        Path to the created project directory.
    """
    package_name = _to_package_name(project_name)

    if target_dir is None:
        target_dir = project_name

    target = Path(target_dir).resolve()

    if target.exists():
        if not force:
            print(
                f"Error: directory '{target}' already exists. "
                "Use --force to overwrite.",
                file=sys.stderr,
            )
            sys.exit(1)
        shutil.rmtree(target)

    # Build replacements
    replacements: dict[str, str] = {
        "{{project_name}}": project_name,
        "{{package_name}}": package_name,
        "{{author_name}}": author or "",
        "{{author_email}}": email or "",
        "{{description}}": description or "",
        "{{github_user}}": github_user or "",
        "{{year}}": str(datetime.now().year),
    }

    # Copy template from package data
    template_root = files("python_template") / "template"
    target.mkdir(parents=True)
    _copy_tree(template_root, target, replacements, rename_pkg=package_name)
    # Print success message
    print(f"✨ Project '{project_name}' created at {target}")
    print()
    print("Next steps:")
    print(f"  cd {target_dir}")
    print("  git init")
    print("  python -m pip install --upgrade pip nox")
    print("  nox -s lint test")

    return target
