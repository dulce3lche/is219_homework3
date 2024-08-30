import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('5'), divide, Decimal('2')),
])
def test_calculation(a, b, operation, expected):
    calculation = Calculation(a, b, operation)
    result = calculation.perform()
    assert result == expected, f"Operation {operation.__name__} failed"

def test_calculation_create():
    calculation = Calculation.create(Decimal('10'), Decimal('5'), add)
    result = calculation.perform()
    assert result == Decimal('15'), "Create method failed"

def test_calculation_divide_by_zero():
    operation = divide
    calc = Calculation(Decimal('4'), Decimal('0'), operation)
    with pytest.raises(ZeroDivisionError):
        calc.perform()