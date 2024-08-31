"""Calculator class for performing arithmetic operations."""
from typing import Callable
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """Calculator class for performing arithmetic operations."""
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Initialize the object with a, b, and operation."""
        self.a: Decimal = a
        self.b: Decimal = b
        self.operation = operation  # Store the operation function

    def perform(self) -> Decimal:
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Create a Calculation object with a, b, and operation."""
        return Calculation(a, b, operation)
    