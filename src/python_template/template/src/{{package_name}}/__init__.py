"""Utilities for the {{project_name}} project."""


from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{project_name}}")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["__version__"]
