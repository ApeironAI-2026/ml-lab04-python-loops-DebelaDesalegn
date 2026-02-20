import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import calculate_factorial


def test_factorial_positive():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(3) == 6

def test_factorial_zero():
    assert calculate_factorial(0) == 1

def test_factorial_negative():
    assert calculate_factorial(-1) is None