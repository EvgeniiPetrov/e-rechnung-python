from decimal import ROUND_HALF_UP, Decimal


def calculate_tax_amount(
    taxable_amount: Decimal,
    vat_percent: Decimal,
) -> Decimal:
    result = taxable_amount * vat_percent / Decimal("100")

    return result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
