"""
Calculator functions
"""


def add(x, y):
    """Add x and y and return result."""
    return x + y


def subtract(x, y):
    """Subtract y from x and return result."""
    return x - y


def multiply(x, y):
    """Multiply x and y and return result."""
    return x * y


def divide(x, y):
    """Divide x by y and return result."""
    if y == 0:
        raise ValueError("Denominator cannot be zero.")
    return x / y
