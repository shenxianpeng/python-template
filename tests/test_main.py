"""Tests for mypackage.main."""

from mypackage.main import main


def test_main(capsys: object) -> None:
    main()
    captured = capsys.readouterr()  # type: ignore[union-attr]
    assert "Hello from mypackage!" in captured.out
