"""
Tests for the calculation module.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('5'), divide, Decimal('2')),
])
def test_calculation(a, b, operation, expected):
    """
    Test the Calculation class with different operations.
    Args:
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (function): The operation to perform.
        expected (Decimal): The expected result.
    Returns:
        None
    """
    calculation = Calculation(a, b, operation)
    result = calculation.perform()
    assert result == expected, f"Operation {operation.__name__} operation with {a} and {b}"

def test_calculation_create():
    """
    Test the create method of the Calculation class.

    Returns:
        None
    """
    calculation = Calculation.create(Decimal('10'), Decimal('5'), add)
    result = calculation.perform()
    assert result == Decimal('15'), "Create method failed"


def test_calculation_divide_by_zero():
    """
    Test that the Calculation class raises a ZeroDivisionError when dividing by zero.

    Returns:
        None
    """
    calc = Calculation(Decimal('4'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
        