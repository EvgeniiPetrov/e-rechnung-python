import pytest

from e_rechnung.domain.checks import validate_invoice_number


@pytest.mark.parametrize(
    "test_value, expected",
    [
        (" 1", "1"),
        ("1 ", "1"),
        (" 1 ", "1"),
        ("test", "test"),
        (" test", "test"),
        ("test ", "test"),
        (" test ", "test"),
        ("  test  ", "test"),
    ],
)
def test_correct_validate_invoice_number(test_value, expected):
    result = validate_invoice_number(test_value)

    assert result == expected


def test_raises_ValueError_when_none():
    with pytest.raises(TypeError):
        validate_invoice_number(None)  # type: ignore


def test_raises_ValueError_when_empty_string():
    with pytest.raises(ValueError):
        validate_invoice_number("")


def test_raises_ValueError_when_doublespase():
    with pytest.raises(ValueError):
        validate_invoice_number("  ")


def test_raises_TypeError_when_not_string():
    with pytest.raises(TypeError):
        validate_invoice_number(4)  # type: ignore
