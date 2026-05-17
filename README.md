# pyrepo-init

`pyrepo-init` is a reusable Python repository starter with packaging, tests,
linting, documentation, and PyPI publishing configuration already wired in.

Use it as a starting point for small Python packages that should be installable
with `pip`, testable with `pytest`, and releasable through GitHub Actions.

## Installation

```bash
pip install pyrepo-init
```

## Usage

```python
from pyrepo_init.main import get_message

print(get_message())
```

Or via command line:

```bash
pyrepo-init
python -m pyrepo_init
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

Configure trusted publishing for `shenxianpeng/pyrepo-init` on PyPI and
TestPyPI before releasing.

## License

MIT
