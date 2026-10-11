# simple input chesks
# Use:  UBL (Universal Business Language) 2.1
#       EN 16931


def validate_invoice_number(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError
    value = value.strip()
    value_len = len(value)
    if value is None or value_len == 0:
        raise ValueError
    if not isinstance(value, str):
        raise TypeError
    return value
