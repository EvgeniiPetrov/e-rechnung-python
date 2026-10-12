# simple input chesks
# Use:  UBL (Universal Business Language) 2.1
#       EN 16931


def validate_invoice_number(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Invoice number must be of type str.")
    value = value.strip()
    value_len = len(value)

    # The "value is None" check is redundant because the type has already been checked
    if value is None or value_len == 0:
        raise ValueError("Invoice number must not be empty or contain only whitespace.")
    return value
