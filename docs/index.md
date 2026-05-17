# pyrepo-init

`pyrepo-init` is a reusable Python repository starter prepared for PyPI
distribution. It includes a `src/` package layout, setuptools-based packaging,
dynamic versions from Git tags, pytest tests, pre-commit linting, Nox sessions,
and MkDocs documentation.

## Install

```bash
pip install pyrepo-init
```

## Use

```bash
pyrepo-init
python -m pyrepo_init
```

```python
from pyrepo_init.main import get_message

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
src/pyrepo_init/       Python package
tests/                 pytest test suite
docs/                  MkDocs documentation
```
