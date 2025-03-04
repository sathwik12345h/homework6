from decimal import Decimal  # Importing Decimal for precise floating-point arithmetic

def add(a: Decimal, b: Decimal) -> Decimal:
    """Returns the sum of two Decimal numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Returns the difference between two Decimal numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Returns the product of two Decimal numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Returns the quotient of two Decimal numbers.
    
    Raises:
        ValueError: If an attempt is made to divide by zero.
    """
    if b == Decimal('0'):  # Ensuring proper comparison with Decimal type
        raise ValueError("Cannot divide by zero")  # Handling divide-by-zero error
    return a / b
