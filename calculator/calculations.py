from typing import Callable, List

from calculator.calculation import Calculation

class CalculationHistory:
    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)
        
    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history
        
    @classmethod
    def clear_history(cls):
        cls.history = []