from decimal import Decimal

import pytest

from e_rechnung.domain.checks_validate_net_unit_price import net_unit_price


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("1", Decimal("1")),
        ("10.5", Decimal("10.5")),
        ("1000", Decimal("1000")),
        ("0.001", Decimal("0.001")),
        ("0", Decimal("0")),
    ],
)
def test_validate_net_unit_price_with_valid_input(input_value, expected_output):
    result = net_unit_price(input_value)
    assert isinstance(result, Decimal)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_value",
    ["-1", "abc", "", " ", "NaN", "Infinity"],
)
def test_validate_net_unit_price_value_error_with_invalid_input(input_value):
    with pytest.raises(ValueError):
        net_unit_price(input_value)


@pytest.mark.parametrize(
    "input_value",
    [
        None,
        1,
        2.5,
        -1,
    ],
)
def test_validate_net_unit_price_type_error_with_invalid_input(input_value):
    with pytest.raises(TypeError):
        net_unit_price(input_value)
