# {{project_name}}

`{{project_name}}` — {{description}}

## Installation

```bash
pip install {{project_name}}
```

## Usage

```python
from {{package_name}}.main import get_message

print(get_message())
```

Or via command line:

```bash
{{project_name}}
python -m {{package_name}}
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
