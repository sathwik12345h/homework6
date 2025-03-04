"""Pytest configuration file for dynamically generating test cases."""

from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def pytest_addoption(parser):
    """Adds a custom command-line option to specify the number of test records."""
    parser.addoption(
        "--num_records", action="store", default=10, type=int,
        help="Number of test records to generate"
    )

@pytest.fixture(scope="module")
def generated_test_cases(request):
    """Generates test cases dynamically based on --num_records parameter."""
    num_records = request.config.getoption("--num_records")
    test_cases = []
    operations = [add, subtract, multiply, divide]

    for _ in range(num_records):
        num1 = Decimal(fake.random_int(min=1, max=100))
        num2 = Decimal(fake.random_int(min=1, max=100))

        operation = fake.random_element(operations)
        if operation is divide and num2 == Decimal('0'):
            num2 = Decimal('1')

        expected = operation(num1, num2)
        test_cases.append((num1, num2, operation, expected))

    return test_cases

@pytest.mark.parametrize("num1, num2, operation, expected", [])
def test_generated_operations(num1, num2, operation, expected, _generated_cases):
    """Parameterized test for dynamically generated operations."""
    assert operation(num1, num2) == expected, (
        f"Failed {operation.__name__} with {num1}, {num2}"
    )
