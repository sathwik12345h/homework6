from decimal import Decimal
from typing import List, Callable
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Retrieve the most recent calculation."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find calculations by operation type (add, subtract, etc.)."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
