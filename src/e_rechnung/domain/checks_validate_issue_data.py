from datetime import date


def validate_issue_data(value: str) -> date:
    if not isinstance(value, str):
        raise TypeError("Дата должна иметь тип str. Требуемый формат даты: str(YYYY-MM-DD).")
    if len(value) != 10:
        raise ValueError(f"Полученная дата: '{value}'. Требуемый формат даты: YYYY-MM-DD.")
    if "w" in value.lower():
        raise ValueError(f"Полученная дата: '{value}'. Требуемый формат даты: YYYY-MM-DD.")
    try:
        result = date.fromisoformat(value)
    except ValueError as exc_info:
        raise ValueError(f"Полученная дата: '{value}'. Ошибка: {str(exc_info)}") from exc_info
    return result
