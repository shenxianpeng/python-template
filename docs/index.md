# python-template

`python-template` is a reusable Python project template prepared for PyPI
distribution. It includes a `src/` package layout, setuptools-based packaging,
dynamic versions from Git tags, pytest tests, pre-commit linting, Nox sessions,
and MkDocs documentation.

## Install

```bash
pip install python-template
```

## Quick Start — Bootstrap a New Project

### Using `python-template init`

```bash
pip install python-template
python-template init my-awesome-project
```

This creates a `my-awesome-project/` directory with everything set up.

```bash
python-template init my-awesome-project \
    --author "Your Name" \
    --email "you@example.com" \
    --description "An awesome Python package" \
    --github-user your-gh-username
```

### Using GitHub "Use this template"

<https://github.com/shenxianpeng/python-template>

Click the green **"Use this template"** button → **"Create a new repository"**,
then clone your new repo and start coding.

---

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
