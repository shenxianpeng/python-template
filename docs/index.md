# python-template

`python-template` is a reusable Python project template prepared for PyPI
distribution. It includes a `src/` package layout, setuptools-based packaging,
dynamic versions from Git tags, pytest tests, pre-commit linting, Nox sessions,
and MkDocs documentation.

## Install

```bash
pip install python-template
```

## Use

```bash
python-template
python -m python_template
```

```python
from python_template.main import get_message

print(get_message())
```

## Develop

```bash
python -m pip install --upgrade pip nox
nox -s test
nox -s lint
nox -s docs
```

## Package Layout

```text
src/python_template/   Python package
tests/                 pytest test suite
docs/                  MkDocs documentation
```
