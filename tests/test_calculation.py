"""
This module contains unit tests for the calculator operations and the Calculation class.

The tests verify the correctness of basic arithmetic operations (addition, subtraction,
multiplication, division) and ensure that the Calculation class performs calculations accurately.
"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# Test arithmetic operations using parameterized test cases
@pytest.mark.parametrize("num1, num2, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_calculation_operations(num1, num2, operation, expected):
    """
    Test that the Calculation class correctly performs arithmetic operations.
    """
    calc = Calculation(num1, num2, operation)
    assert calc.perform() == expected, (
        f"Failed {operation.__name__} operation with {num1} and {num2}" )

def test_calculation_repr():
    """
    Test that the __repr__ method provides a correct string representation
    of a Calculation instance.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "Incorrect __repr__ output."

def test_divide_by_zero():
    """
    Test that division by zero raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
    