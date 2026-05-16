"""Command-line entry point for {{project_name}}."""


def get_message() -> str:
    """Return the default command-line message."""
    return "{{project_name}} is installed and ready to use."


def main() -> None:
    """Run the command-line program."""
    print(get_message())
