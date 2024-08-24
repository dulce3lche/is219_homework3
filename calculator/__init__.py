from calculator.calculation import Calculation # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide # Arithmetic operations
from typing import Callable # For type hinting callable objects
from decimal import Decimal # For precise decimal arithmetic

class Calculator:
    @staticmethod
    def perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        return calculation.perform() # Perform the calculation and return the result()

    @staticmethod
    def add(a: Decimal,b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal,b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, subtract)

    @staticmethod
    def multiply (a: Decimal,b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal,b: Decimal) -> Decimal:
        return Calculator.perform_operation(a, b, divide)