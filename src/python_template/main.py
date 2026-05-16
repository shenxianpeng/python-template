"""Command-line entry point for python-template."""

from __future__ import annotations


def get_message() -> str:
    """Return the default command-line message."""
    return "python-template is installed and ready to use."


def main() -> None:
    """Run the command-line program."""
    print(get_message())
