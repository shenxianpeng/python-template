"""Tests for python_template.main."""

import tempfile
from pathlib import Path
from pytest import CaptureFixture

from python_template.main import get_message, main


def test_main(capsys: CaptureFixture[str]) -> None:
    main([])
    captured = capsys.readouterr()
    assert get_message() in captured.out


def test_main_init_creates_project() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        target = Path(tmpdir) / "my-test-project"
        main(["init", "my-test-project", "--target", str(target), "--force"])
        assert target.is_dir()
        assert (target / "pyproject.toml").exists()
        assert (target / "src" / "my_test_project" / "__init__.py").exists()
        assert (target / "tests" / "test_main.py").exists()
        assert (target / ".gitignore").exists()
        assert (target / ".github" / "workflows" / "test.yml").exists()

        # Verify placeholder replacement
        content = (target / "pyproject.toml").read_text()
        assert "my-test-project" in content
        assert "{{" not in content

        # Verify the package directory was renamed correctly
        assert not (target / "src" / "{{package_name}}").exists()
        assert (target / "src" / "my_test_project").is_dir()


def test_main_init_with_options() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        target = Path(tmpdir) / "my-test-project"
        main(
            [
                "init",
                "my-test-project",
                "--target",
                str(target),
                "--author",
                "Alice",
                "--email",
                "alice@example.com",
                "--description",
                "A test project",
                "--github-user",
                "alice",
                "--force",
            ]
        )
        content = (target / "pyproject.toml").read_text()
        assert 'name = "my-test-project"' in content
        assert "Alice" in content
        assert "alice@example.com" in content
        assert "A test project" in content
        assert "alice" in content
