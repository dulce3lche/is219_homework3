"""This module provides classes to manage calculations."""
from typing import List
from calculator.calculation import Calculation

class CalculationHistory:
    """
    A class to manage the history of calculations. This class provides methods to add and retrieve 
    calculations from the history, as well as a method to clear the history. 
    """
    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations. This method removes all calculations from the history."""
        cls.history = []

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation in the history.
        Returns: 
        The latest calculation in the history, or None if the history is empty.
        """
        if cls.history:
            return cls.history[-1]
        return None
