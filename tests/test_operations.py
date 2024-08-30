from decimal import Decimal
from operations import add, subtract, multiply, divide
from calculator.operations import Calculation

def test_calculation_add():
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    result = calculation.perform()
    assert result == Decimal('15'), "Add operation failed"

def test_calculation_subtract():
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    result = calculation.perform()
    assert result == Decimal('5'), "Subtract operation failed"

def test_calculation_multiply():
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    result = calculation.perform()
    assert result == Decimal('50'), "Multiply operation failed"

def test_calculation_divide():
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    result = calculation.perform()
    assert result == Decimal('2'), "Divide operation failed"