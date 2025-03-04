"""Tests for the main module and calculator operations."""

from decimal import InvalidOperation
import pytest
from main import calculate_and_print, main
from calculator import Calculator

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    # Valid operations:
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    # Division by zero:
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    # Unknown operation:
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    # Invalid number inputs (failing digit check):
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """Test calculate_and_print for valid operations, errors, and unknown commands."""
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

def test_invalid_operation_exception(monkeypatch, capsys):
    """
    Test that if Calculator.add raises an InvalidOperation exception,
    calculate_and_print catches it and prints the appropriate error message.
    """
    def fake_add(num1, num2):
        raise InvalidOperation("Simulated error")
    monkeypatch.setattr(Calculator, 'add', fake_add)
    calculate_and_print("5", "3", "add")
    captured = capsys.readouterr()
    expected = "Invalid number input: 5 or 3 is not a valid number."
    assert captured.out.strip() == expected

def test_main(monkeypatch, capsys):
    """
    Test the main() function by monkeypatching App so that start() prints a message.
    This covers the main() function in the module.
    """
    class DummyApp:
        """A dummy App class for testing main()."""
        def start(self):
            """Simulate the app start method."""
            print("app started")
    # Monkeypatch the App class in the main module.
    monkeypatch.setattr("main.App", DummyApp)
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "app started"
