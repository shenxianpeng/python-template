# python-template

`python-template` is a reusable Python project template with packaging, tests,
linting, documentation, and PyPI publishing configuration already wired in.

Use it as a starting point for small Python packages that should be installable
with `pip`, testable with `pytest`, and releasable through GitHub Actions.

## Installation

```bash
pip install python-template
```

## Usage

```python
from python_template.main import get_message

print(get_message())
```

Or via command line:

```bash
python-template
python -m python_template
```

## Development

```bash
python -m pip install --upgrade pip nox
nox -s test
nox -s lint
nox -s docs
```

## Release to PyPI

Before publishing, verify that the package builds cleanly:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

This repository includes `.github/workflows/publish-pypi.yml`:

- Manual `workflow_dispatch` publishes to TestPyPI.
- Publishing a GitHub release publishes to PyPI.

Configure trusted publishing for this project on PyPI/TestPyPI, or add the
repository secrets expected by your publishing workflow before releasing.

## License

MIT
