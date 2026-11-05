from datetime import date


def validate_issues_data(value: str) -> date:
    if not isinstance(value, str):
        raise TypeError("Дата должна быть строкой. Требуемый формат даты: str(YYYY-MM-DD).")
    if len(value) != 10:
        raise ValueError(f"Полученная дата: '{value}'. Требуемый формат даты: YYYY-MM-DD.")
    try:
        result = date.fromisoformat(value)
    except ValueError as exc_info:
        raise ValueError(f"Полученная дата: '{value}'. Ошибка: {str(exc_info)}")  # noqa: B904
    return result
