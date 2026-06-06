"""
Calculator Module - Performs basic mathematical operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def factorial(n):
    """Calculate factorial of n (n!)."""
    if n < 0:
        raise ValueError("Factorial of negative number is undefined!")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent

def percentage(value, total):
    """Calculate percentage of value relative to total."""
    if total == 0:
        raise ValueError("Total cannot be zero!")
    return (value / total) * 100
