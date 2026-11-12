def validate_description(value: str) -> str:
    if value is None:
        raise TypeError(
            f"В строке {value} требуется тип входных данных str и буквенное описание товара."
        )
    if not isinstance(value, str):
        raise TypeError(
            f"В строке {value} требуется тип входных данных str и буквенное описание товара."
        )
    value = value.strip()
    if len(value) == 0:
        raise ValueError(
            "Длина передаваемого параметра равна 0 или содержит только пробельные символы."
            + " Требуется буквенное описание товара в str формате."
        )
    return value
