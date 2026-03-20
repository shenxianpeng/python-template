# Memory

## Me
Xianpeng Shen (shenxianpeng), DevOps engineer.

## About This Repo
This is a **Python project template**. When starting a new Python project, fork/copy this repo and rename `mypackage` to your project name.

## Tech Stack
- Python 3.9+ | src layout | setuptools-scm (versioning)
- Linting: ruff, mypy, pre-commit
- Testing: pytest
- Docs: Sphinx + sphinx-rtd-theme
- Task runner: Nox

## Key Commands
- `nox -s lint` — run linters
- `nox -s test` — run tests
- `nox -s docs` — build docs
- `pre-commit run --all-files` — before committing

## Structure
```
src/mypackage/   ← rename to your package name
tests/
docs/source/
```

## Preferences
- Branch for PRs: `main`
- Always run `nox -s lint` before committing
- **Language**: Always reply in the same language the user writes in. If the user writes in Chinese, respond in Chinese.
