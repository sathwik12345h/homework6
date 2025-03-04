from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
    
    @staticmethod
    def create(num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Alternative constructor to create a Calculation instance."""
        return Calculation(num1, num2, operation)

    def perform(self) -> Decimal:
        """Perform the stored operation and return the result."""
        return self.operation(self.num1, self.num2)

    def __repr__(self):
        """Return a string representation of the calculation."""
        return f"Calculation({self.num1}, {self.num2}, {self.operation.__name__})"
