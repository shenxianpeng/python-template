# Memory

## Me
Xianpeng Shen (shenxianpeng), DevOps engineer.

## About This Repo
This is a **Python project template** published as `python-template`.
The import package is `python_template`, following the normal PyPI convention
where distribution names may contain hyphens and Python import names use
underscores.

## Tech Stack
- Python 3.9+ | src layout | setuptools-scm (versioning)
- Linting: ruff, mypy, pre-commit
- Testing: pytest
- Docs: MkDocs + mkdocs-material
- Task runner: Nox

## Key Commands
- `nox -s lint` — run linters
- `nox -s test` — run tests
- `nox -s docs` — build docs
- `pre-commit run --all-files` — before committing

## Structure
```
src/python_template/
tests/
docs/
```

## Preferences
- Branch for PRs: `main`
- Always run `nox -s lint` before committing
- **Language**: Always reply in the same language the user writes in. If the user writes in Chinese, respond in Chinese.
