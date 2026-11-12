import pytest

from e_rechnung.domain.checks_validate_description import validate_description

# pytest.mark.parametrize("value", [None, 123])


def test_type_error_when_None_in_description(value=None) -> None:
    with pytest.raises(TypeError) as exec_info:
        validate_description(value)  # type: ignore
    assert (
        str(exec_info.value)
        == f"В строке {value} требуется тип входных данных str и буквенное описание товара."
    )


def test_type_error_when_integer_in_description(value=123) -> None:
    with pytest.raises(TypeError) as exec_info:
        validate_description(value)  # type: ignore
    assert (
        str(exec_info.value)
        == f"В строке {value} требуется тип входных данных str и буквенное описание товара."
    )


def test_type_error_when_whitespace_in_description(value="   ") -> None:
    with pytest.raises(ValueError) as exec_info:
        validate_description(value)  # type: ignore
    assert (
        str(exec_info.value)
        == "Длина передаваемого параметра равна 0 или содержит только пробельные символы."
        + " Требуется буквенное описание товара в str формате."
    )
