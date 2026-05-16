# {{project_name}}

`{{project_name}}` is {{description}}.

## Install

```bash
pip install {{project_name}}
```

## Use

```bash
{{project_name}}
python -m {{package_name}}
```

```python
from {{package_name}}.main import get_message

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
src/{{package_name}}/   Python package
tests/                  pytest test suite
docs/                   MkDocs documentation
```
