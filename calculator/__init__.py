from calculator.calculation import Calculation # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide # Arithmetic operations
from typing import Callable # For type hinting callable objects
from decimal import Decimal # For precise decimal arithmetic

class Calculator:
    @staticmethod
    def add(a: Decimal,b: Decimal) -> Decimal:
        calculation = Calculation(a, b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(a: Decimal,b: Decimal) -> Decimal:
        calculation = Calculation(a, b, subtract)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply (a: Decimal,b: Decimal) -> Decimal:
        calculation = Calculation(a, b, multiply)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(a: Decimal,b: Decimal) -> Decimal:
        calculation = Calculation(a, b, divide)  # Pass the add function from calculator.operations
        return calculation.get_result()