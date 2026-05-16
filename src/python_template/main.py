"""Command-line entry point for python-template."""

import argparse
import sys


def get_message() -> str:
    """Return the default command-line message."""
    return "python-template is installed and ready to use."


def main(argv: list[str] | None = None) -> None:
    """Run the command-line program."""
    parser = argparse.ArgumentParser(
        prog="python-template",
        description="Python project template – bootstrap new projects.",
    )
    subparsers = parser.add_subparsers(dest="command")

    # --- init subcommand ---
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize a new Python project from the template",
    )
    init_parser.add_argument(
        "project_name",
        nargs="?",
        help="Name of the project to create (e.g. my-awesome-package)",
    )
    init_parser.add_argument(
        "-t",
        "--target",
        dest="target_dir",
        default=None,
        help="Target directory (defaults to the project name)",
    )
    init_parser.add_argument(
        "-a",
        "--author",
        default=None,
        help="Author name for pyproject.toml",
    )
    init_parser.add_argument(
        "-e",
        "--email",
        default=None,
        help="Author email for pyproject.toml",
    )
    init_parser.add_argument(
        "-d",
        "--description",
        default=None,
        help="Short project description",
    )
    init_parser.add_argument(
        "-u",
        "--github-user",
        dest="github_user",
        default=None,
        help="GitHub username for URLs in config files",
    )
    init_parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        default=False,
        help="Overwrite target directory if it exists",
    )

    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    if args.command == "init":
        from python_template.init import init_project

        if args.project_name is None:
            init_parser.print_help()
            sys.exit(1)

        init_project(
            project_name=args.project_name,
            target_dir=args.target_dir,
            author=args.author,
            email=args.email,
            description=args.description,
            github_user=args.github_user,
            force=args.force,
        )
    else:
        print(get_message())
