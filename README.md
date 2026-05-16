# python-template

`python-template` is a reusable Python project template with packaging, tests,
linting, documentation, and PyPI publishing configuration already wired in.

Use it as a starting point for small Python packages that should be installable
with `pip`, testable with `pytest`, and releasable through GitHub Actions.

## Quick Start — Bootstrap a New Project

You can create a new project from this template in two ways:

### Option 1: `python-template init` (command line)

```bash
pip install python-template
python-template init my-awesome-project
```

This creates a `my-awesome-project/` directory with everything set up. You can
customise it with additional options:

```bash
python-template init my-awesome-project \
    --author "Your Name" \
    --email "you@example.com" \
    --description "An awesome Python package" \
    --github-user your-gh-username
```

### Option 2: GitHub "Use this template"

<https://github.com/shenxianpeng/python-template>

Click the green **"Use this template"** button → **"Create a new repository"**,
then clone your new repo and start coding.

---

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
