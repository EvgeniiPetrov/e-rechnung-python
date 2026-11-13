import pytest

from e_rechnung.domain.checks_validate_items_requirement_fields import (
    validate_items_requirement_fields,
)


def report(message):
    print(message)


def test_when_all_fields_are_present():
    value = {
        "description": "description",
        "quantity": "1",
        "unit_code": "HUR",
        "net_unit_price": "1",
        "vat_percent": "19",
    }

    result = validate_items_requirement_fields(value)
    assert result is True


def test_when_all_fields_are_missing() -> None:
    value: dict = {}
    with pytest.raises(ValueError) as exec_info:
        validate_items_requirement_fields(value)
    assert (
        str(exec_info.value)
        == "В переданном dict отсутствуют обязательные поля: ['description', 'net_unit_price', 'quantity', 'unit_code', 'vat_percent']"
    )


@pytest.mark.parametrize(
    "value",
    [
        {"description": "description"},
        {"description": "description", "quantity": "1", "unit_code": "HUR"},
        {
            "description": "description",
            "quantity": "1",
            "unit_code": "HUR",
            "vat_percent": "19",
        },
    ],
)
def test_when_some_fields_are_missing(value) -> None:
    with pytest.raises(ValueError):
        validate_items_requirement_fields(value)


def test_more_when_all_fields_are_present():
    value = {
        "description": "description",
        "quantity": "1",
        "unit_code": "HUR",
        "net_unit_price": "1",
        "vat_percent": "19",
        "discount": "20",
    }

    with pytest.raises(ValueError):
        validate_items_requirement_fields(value)
