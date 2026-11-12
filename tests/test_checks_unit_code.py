import pytest

from e_rechnung.domain.checks_unit_code import validate_unit_code


def test_type_error_when_None_in_unit_code(value=None) -> None:
    with pytest.raises(TypeError) as exec_info:
        validate_unit_code(value)  # type: ignore
    assert (
        str(exec_info.value)
        == "Получено значение None, требуется тип входных данных str и код единицы измерения позиции счёта."
    )


def test_type_error_when_integer_in_unit_code(value=123) -> None:
    with pytest.raises(TypeError) as exec_info:
        validate_unit_code(value)  # type: ignore
    assert (
        str(exec_info.value)
        == f"В строке {value} требуется тип входных данных str и код единицы измерения позиции счёта."
    )


@pytest.mark.parametrize(
    "value",
    [
        "   ",
        "",
    ],
)
def test_value_error_when_whitespace_or_zero_length_in_unit_code(value) -> None:
    with pytest.raises(ValueError) as exec_info:
        validate_unit_code(value)  # type: ignore
    assert (
        str(exec_info.value)
        == "Длина передаваемого параметра равна 0 или содержит только пробельные символы."
        + " Требуется код единицы измерения позиции счёта в str формате."
    )


@pytest.mark.parametrize(
    "value, expected",
    [("HUR", "HUR"), (" HUR ", "HUR"), ("C62", "C62")],
)
def test_correct_value_in_unit_code(value, expected) -> None:
    result = validate_unit_code(value)
    assert result == expected
