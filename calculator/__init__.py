from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def _perform_operation(num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Helper method to create a Calculation object and execute it."""
        calculation = Calculation.create(num1, num2, operation)  # Create a calculation object
        Calculations.add_calculation(calculation)  # Store in history
        return calculation.perform()  # Execute the operation and return result

    @staticmethod
    def add(num1: Decimal, num2: Decimal) -> Decimal:
        """Performs addition of two Decimal numbers and stores the result in history."""
        return Calculator._perform_operation(num1, num2, add)

    @staticmethod
    def subtract(num1: Decimal, num2: Decimal) -> Decimal:
        """Performs subtraction of two Decimal numbers and stores the result in history."""
        return Calculator._perform_operation(num1, num2, subtract)

    @staticmethod
    def multiply(num1: Decimal, num2: Decimal) -> Decimal:
        """Performs multiplication of two Decimal numbers and stores the result in history."""
        return Calculator._perform_operation(num1, num2, multiply)

    @staticmethod
    def divide(num1: Decimal, num2: Decimal) -> Decimal:
        """Performs division of two Decimal numbers and stores the result in history."""
        return Calculator._perform_operation(num1, num2, divide)
