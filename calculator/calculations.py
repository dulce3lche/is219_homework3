from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    _calculation_history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.calculation_history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        return cls.calculation_history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.calculation_history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.calculation_history:
            return cls.calculation_history[-1]
        return None

   # @classmethod
    #def find_by_operation(cls, operation_name: str) -> List[Calculation]:
     #   """Find and return a list of calculations by operation name."""
      #  return [calc for calc in cls.calculation_history if calc.operation.__name__ == operation_name]

