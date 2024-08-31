""" Test operations module. """
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

def test_calculation_add():
    """Test addition operation for various scenarios."""
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    result = calculation.perform()
    assert result == Decimal('15'), "Add operation failed"

def test_calculation_subtract():
    """Test subtraction operation for various scenarios. 
    This test ensures that the subtraction operation correctly subtracts
    the second operand from the first operand and returns the expected result.
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    result = calculation.perform()
    assert result == Decimal('5'), "Subtract operation failed"

def test_calculation_multiply():
    """Test multiplication operation for various scenarios.
    This test ensures that the multiplication operation correctly multiplies
    the first operand by the second operand and returns the expected result.
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    result = calculation.perform()
    assert result == Decimal('50'), "Multiply operation failed"

def test_calculation_divide():
    """Test division operation for various scenarios.
    This test ensures that the division operation correctly divides
    the first operand by the second operand and returns the expected result.
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    result = calculation.perform()
    assert result == Decimal('2'), "Divide operation failed"
    