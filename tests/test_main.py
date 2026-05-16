"""Tests for python_template.main."""

from __future__ import annotations

from typing import TYPE_CHECKING

from python_template.main import get_message, main

if TYPE_CHECKING:
    from pytest import CaptureFixture


def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert get_message() in captured.out
