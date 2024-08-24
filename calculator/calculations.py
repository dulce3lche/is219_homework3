from typing import List

class CalculationHistory:
    def __init__(self):
        self.history = []

    def add_calculation(self, calculation: str, result: str):
        self.history.append((calculation, result))

    def get_history(self) -> List[str]:
        return [f"{calculation} = {result}" for calculation, result in self.history]

    def clear_history(self):
        self.history = []