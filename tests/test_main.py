"""Tests for mypackage.main."""

from __future__ import annotations

from typing import TYPE_CHECKING

from mypackage.main import main

if TYPE_CHECKING:
    from pytest import CaptureFixture


def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from mypackage!" in captured.out
