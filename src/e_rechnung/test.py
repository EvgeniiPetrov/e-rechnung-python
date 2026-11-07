from decimal import Decimal, InvalidOperation

a = Decimal("0.1")
b = Decimal("0.2")
try:
    result = Decimal("qqq")
    print(result)
except InvalidOperation as e:
    print(f"******Error: {str(e)}")  # Output: Error: [<class 'decimal.ConversionSyntax'>]
except Exception as e:
    print(f"####Error: {str(e)}")  # Output: Error: [<class 'decimal.ConversionSyntax'>]

print(a + b)  # Output: 0.3
print(type(a + b))  # Output: <class 'decimal.Decimal'>
print(a.is_infinite())  # Output: False
