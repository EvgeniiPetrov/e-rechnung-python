from decimal import Decimal

import pytest

from e_rechnung.domain.calculate_tax_amount import calculate_tax_amount


@pytest.mark.parametrize(
    "taxable_amount, vat_percent, expected",
    [
        (Decimal("160"), Decimal("19"), Decimal("30.40")),
        (Decimal("100.03"), Decimal("19"), Decimal("19.01")),
        (Decimal("100"), Decimal("7"), Decimal("7")),
        (Decimal("0"), Decimal("19"), Decimal("0")),
    ],
)
def test_calculate_tax_amount_when_values_is_correct(taxable_amount, vat_percent, expected):
    result = calculate_tax_amount(taxable_amount, vat_percent)
    assert result == expected
