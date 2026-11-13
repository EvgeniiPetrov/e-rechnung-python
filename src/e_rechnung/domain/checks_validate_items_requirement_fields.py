def validate_items_requirement_fields(value: dict) -> bool:
    requirement_fields: set = {
        "description",
        "quantity",
        "unit_code",
        "net_unit_price",
        "vat_percent",
    }

    missing_fields: str = ""
    unexpected_fields: str = ""
    correct_fields: set = set()
    uncorrect_fields: set = set()

    if value is None:
        raise TypeError(f"В строке {value} требуется тип входных данных dict.")

    if not isinstance(value, dict):
        raise TypeError(f"В строке {value} требуется тип входных данных dict.")

    if not value:
        sorted_fields = sorted(requirement_fields)
        raise ValueError(f"В переданном dict отсутствуют обязательные поля: {sorted_fields}")

    missing_fields = ", ".join(requirement_fields - value.keys())
    if missing_fields:
        raise ValueError(
            f"В переданном dict {value} отсутствуют обязательные поля: {missing_fields}"
        )

    uncorrect_fields = requirement_fields.symmetric_difference(value.keys())
    if len(uncorrect_fields) > 0:
        unexpected_fields = ", ".join(uncorrect_fields)
        raise ValueError(
            f"В переданном dict {value} присутствуют неожиданные поля: {unexpected_fields}"
        )

    if value is not None:
        correct_fields = requirement_fields.intersection(value.keys())
    else:
        raise TypeError(f"В строке {value} требуется тип входных данных dict.")
    if len(correct_fields) == 5:
        return True
    return False


# if __name__ == "__main__":
#     value = {
#         "description": "description",
#         "quantity": "1",
#         "unit_code": "HUR",
#         "net_unit_price": "1",
#         "vat_percent": "19",
#     }
#     validate_items_requirement_fields(value)
