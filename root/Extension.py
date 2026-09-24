import pytest


def double_integer(a: int) -> int:
    """
    >>> double_integer(2)
    :param a:
    :return:
    """
    double = a * 2
    return double


def add(a: float, b: float) -> float:
    """Add two numbers."""
    total = a + b
    return total

def divide (a: float, b: float) -> float:
    """Divides two numbers together."""
    half = a / 2
    return half

def test_double_interger_one():
    assert double_integer(40) == 80

def test_double_interger_two():
    assert double_integer(10) == 20

def test_add_one():
    assert add(2.4, 0.1) == pytest.approx(2.5)

def test_add_two():
    assert add(3, 10) == 13

def test_divide_one():
    assert divide(4, 2) == 2

def test_divide_two():
    assert divide(100, 2) == 50