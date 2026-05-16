"""Tests for {{package_name}}.main."""


from pytest import CaptureFixture

from {{package_name}}.main import get_message, main


def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert get_message() in captured.out
