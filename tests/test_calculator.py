"""Test cases for calculator module."""

import sys
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

import pytest
from calculator import add, subtract, multiply, divide, factorial, power, percentage

class TestBasicOperations:
    """Test basic arithmetic operations."""

    def test_add(self):
        """Test addition."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_subtract(self):
        """Test subtraction."""
        assert subtract(5, 3) == 2

    def test_multiply(self):
        """Test multiplication."""
        assert multiply(3, 4) == 12

    def test_divide(self):
        """Test division."""
        assert divide(10, 2) == 5.0

    def test_factorial(self):
        """Test factorial."""
        assert factorial(5) == 120

    def test_power(self):
        """Test power."""
        assert power(2, 3) == 8

    def test_percentage(self):
        """Test percentage."""
        assert percentage(25, 100) == 25.0
        
    def test_add_negative(self):
        """Test addition with negative numbers."""
        assert add(-5, 5) == 0

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(0, 100) == 0

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_factorial_negative(self):
        """Test that factorial of negative raises error."""
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1

    def test_percentage_zero_total(self):
        """Test that percentage with zero total raises error."""
        with pytest.raises(ValueError):
            percentage(25, 0)
