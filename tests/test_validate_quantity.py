from decimal import Decimal

import pytest

from e_rechnung.domain.checks_validate_quantity import validate_quantity


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("1", Decimal("1")),
        ("10.5", Decimal("10.5")),
        ("1000", Decimal("1000")),
        ("0.001", Decimal("0.001")),
    ],
)
def test_validate_quantity_with_valid_input(input_value, expected_output):
    result = validate_quantity(input_value)
    assert isinstance(result, Decimal)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_value",
    ["0", "-1", "abc", "", " ", "NaN", "Infinity"],
)
def test_validate_quantity_value_error_with_invalid_input(input_value):
    with pytest.raises(ValueError):
        validate_quantity(input_value)


@pytest.mark.parametrize(
    "input_value",
    [
        None,
        1,
        2.5,
        -1,
    ],
)
def test_validate_quantity_type_error_with_invalid_input(input_value):
    with pytest.raises(TypeError):
        validate_quantity(input_value)
