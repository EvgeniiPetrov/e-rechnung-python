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


def test_raises_TypeError_when_none():
    with pytest.raises(TypeError) as exc_info:
        validate_invoice_number(None)  # type: ignore
    assert str(exc_info.value) == "Invoice number must be of type str."


def test_raises_ValueError_when_empty_string():
    with pytest.raises(ValueError) as exc_info:
        validate_invoice_number("")
    assert str(exc_info.value) == "Invoice number must not be empty or contain only whitespace."


def test_raises_ValueError_when_doublespase():
    with pytest.raises(ValueError) as exc_info:
        validate_invoice_number("  ")
    assert str(exc_info.value) == "Invoice number must not be empty or contain only whitespace."


def test_raises_TypeError_when_not_string():
    with pytest.raises(TypeError) as exc_info:
        validate_invoice_number(4)  # type: ignore
    assert str(exc_info.value) == "Invoice number must be of type str."
