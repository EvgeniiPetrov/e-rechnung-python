import pytest

from e_rechnung.cli import main


def test_help_output(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0
    result = capsys.readouterr()
    assert "e-rechnung" in result.out


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])
    assert exc_info.value.code == 0
    assert "0.1.0" in capsys.readouterr().out
