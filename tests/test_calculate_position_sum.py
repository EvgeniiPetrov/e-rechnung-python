from decimal import Decimal

import pytest

from e_rechnung.domain.calculation_position_sum import calculate_position_sum


@pytest.mark.parametrize(
    "quantity, net_unit_price, expected",
    [
        (Decimal(2), Decimal(50), Decimal(100)),
        (Decimal(1), Decimal(25), Decimal(25)),
        (Decimal(1.5), Decimal(0), Decimal(0)),
    ],
)
def test_when_input_values_is_correct(quantity, net_unit_price, expected):
    result: Decimal = calculate_position_sum(quantity, net_unit_price)

    assert isinstance(result, Decimal)
    assert result == expected
