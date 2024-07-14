from decimal import Decimal
# Define the functions with type hints
def add(a: Decimal, b: Decimal) -> Decimal:
    """Addition operation"""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtraction operation"""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiplication operation"""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Division operation"""
    if b == 0: #if data is equal to zero it will throw an error
        raise ValueError("Cannot divide by zero")
    return a / b
