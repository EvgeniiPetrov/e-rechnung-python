from decimal import Decimal


def calculate_position_sum(
    quantity: Decimal,
    net_unit_price: Decimal,
) -> Decimal:
    return quantity * net_unit_price
