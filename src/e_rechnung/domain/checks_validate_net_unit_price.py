from decimal import Decimal, InvalidOperation


def validate_net_unit_price(value: str) -> Decimal:
    if value is None:
        raise TypeError(f"В строке {value} требуется тип входных данных str и числовое значение.")
    if not isinstance(value, str):
        raise TypeError(f"В строке {value} требуется тип входных данных str и числовое значение.")
    value = value.strip()
    if len(value) == 0:
        raise ValueError(
            "Длина передаваемого параметра равна 0. Требуется числовое значение в str формате."
        )
    try:
        decimal_value = Decimal(value)
        if decimal_value.is_infinite() or decimal_value.is_nan():
            raise ValueError(f"Числовое значение '{value}' должно быть конечным и не NaN.")
        if decimal_value < 0:
            raise ValueError(f"Числовое значение '{value}' не должно быть отрицательным.")
    except InvalidOperation as exc_info:
        raise ValueError(
            f"Ошибка при преобразовании строки '{value}' в Decimal: {str(exc_info)}"
        ) from exc_info
    return decimal_value
