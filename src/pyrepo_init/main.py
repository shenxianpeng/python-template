"""Command-line entry point for pyrepo-init."""

from __future__ import annotations


def get_message() -> str:
    """Return the default command-line message."""
    return "pyrepo-init is installed and ready to use."


def main() -> None:
    """Run the command-line program."""
    print(get_message())
