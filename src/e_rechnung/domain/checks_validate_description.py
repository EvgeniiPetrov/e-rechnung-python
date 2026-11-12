def validate_description(value: str) -> str:
    if value is None:
        raise TypeError(
            "Получено значение None, требуется тип входных данных str и описание позиции счёта товара."
        )
    if not isinstance(value, str):
        raise TypeError(
            f"В строке {value} требуется тип входных данных str и описание позиции счёта товара."
        )
    value = value.strip()
    if len(value) == 0:
        raise ValueError(
            "Длина передаваемого параметра равна 0 или содержит только пробельные символы."
            + " Требуется описание позиции счёта в str формате."
        )
    return value
