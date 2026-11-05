import datetime

import pytest

from e_rechnung.domain.checks_validate_issue_data import validate_issue_data


@pytest.mark.parametrize("value", [("2026-2-8"), ("20261008"), (" 2026-10-08 "), ""])
def test_raices_ValueErorr_when_data_Incorrect(value: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        validate_issue_data(value)
    assert str(exc_info.value) == f"Полученная дата: '{value}'. Требуемый формат даты: YYYY-MM-DD."


@pytest.mark.parametrize(
    "value",
    [
        ("2026-02-29"),
        ("2026-02-30"),
    ],
)
def test_raices_ValueErorr_when_data_Out_Of_Range(value: str) -> None:
    # exc_info = None
    with pytest.raises(ValueError) as exc_info_too:
        validate_issue_data(value)
    assert (
        str(exc_info_too.value)
        == f"Полученная дата: '{value}'. Ошибка: day is out of range for month"
    )


def test_raices_TypeErorr_when_data_Not_String() -> None:
    with pytest.raises(TypeError) as exc_info:
        validate_issue_data(123)  # type: ignore
    assert str(exc_info.value) == (
        "Дата должна быть строкой. Требуемый формат даты: str(YYYY-MM-DD)."
    )


def test_raices_TypeErorr_when_data_is_None() -> None:
    with pytest.raises(TypeError) as exc_info:
        validate_issue_data(None)  # type: ignore
    assert str(exc_info.value) == (
        "Дата должна быть строкой. Требуемый формат даты: str(YYYY-MM-DD)."
    )


@pytest.mark.parametrize(
    "value, expected",
    [("2026-10-08", datetime.date(2026, 10, 8)), ("2024-02-29", datetime.date(2024, 2, 29))],
)
def test_corret_data(value, expected) -> None:
    result = validate_issue_data(value)
    assert result == expected
