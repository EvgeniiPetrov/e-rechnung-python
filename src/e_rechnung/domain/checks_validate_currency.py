def validate_currency(value: str) -> str:  # noqa
    currencies: set = {
        "EUR",
    }
    if value is None:
        raise TypeError(
            f"В строке {value} требуется тип входных данных str и буквенное обозначение валюты."
        )
    if not isinstance(value, str):
        raise TypeError(
            f"В строке {value} требуется тип входных данных str и буквенное обозначение валюты."
        )
    value = value.strip().upper()
    if len(value) == 0:
        raise ValueError(
            "Длинна передаваемого параметра равна 0. Требуется обозначение поддерживаемого"
            "типа валюты в str формате."
        )
    if value in currencies:
        return value
    else:
        raise ValueError(f"Обозначение валюты '{value}' не входит в поддерживаемые.")
