from typing import Callable
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        self.a: Decimal = a
        self.b: Decimal = b
        self.operation = operation  # Store the operation function

    def perform(self) -> Decimal:
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)