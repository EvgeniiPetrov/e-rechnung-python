def validate_unit_code(value: str) -> str:
    if value is None:
        raise TypeError(
            "Получено значение None, требуется тип входных данных str и код единицы измерения товара."
        )
    if not isinstance(value, str):
        raise TypeError(
            f"В строке {value} требуется тип входных данных str и код единицы измерения товара."
        )
    value = value.strip()
    if len(value) == 0:
        raise ValueError(
            "Длина передаваемого параметра равна 0 или содержит только пробельные символы."
            + " Требуется код единицы измерения товара в str формате."
        )
    return value
