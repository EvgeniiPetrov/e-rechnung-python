import pytest

from e_rechnung.domain.checks_validate_currency import validate_currency


@pytest.mark.parametrize(
    "value, expected",
    [("eur", "EUR"), ("Eur", "EUR"), (" eur ", "EUR"), ("EUR", "EUR"), ("  EUR  ", "EUR")],
)
def test_when_value_is_correct(value, expected):
    result = validate_currency(value)
    assert result == expected


@pytest.mark.parametrize("value", ["USD", "RUB", "EU R"])
def test_raises_value_error(value):
    with pytest.raises(ValueError) as exc_info:
        validate_currency(value)
    assert str(exc_info.value) == (f"Обозначение валюты '{value}' не входит в поддерживаемые.")


@pytest.mark.parametrize("value", [None, 123])
def test_raises_type_error(value):
    with pytest.raises(TypeError) as exc_info:
        validate_currency(value)
    assert (
        str(exc_info.value)
        == f"В строке {value} требуется тип входных данных str и буквенное обозначение валюты."
    )


def test_raises_value_error_when_empty_string(value=""):
    with pytest.raises(ValueError) as exc_info:
        validate_currency(value)
    assert str(exc_info.value) == (
        "Длина передаваемого параметра равна 0. Требуется обозначение поддерживаемого "
        "типа валюты в str формате."
    )


def test_raises_value_error_when_only_whitespace(value="   "):
    with pytest.raises(ValueError) as exc_info:
        validate_currency(value)
    assert str(exc_info.value) == (
        "Длинна передаваемого параметра равна 0. Требуется обозначение поддерживаемого"
        "типа валюты в str формате."
    )
