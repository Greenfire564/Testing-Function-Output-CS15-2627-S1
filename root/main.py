import pytest


def double_integer(a: int) -> int:
    """Double an integer.

    :param a: The value to double.
    :return: The doubled value.
    """
    double = a * 2
    return double


def add(a: float, b: float) -> float:
    """Adds two numbers together

    :param a: First number to add.
    :param b: Second number to add.
    :return: Sum of two numbers.
    """
    total = a + b
    return total


def test_double_integer():
    assert 4 == double_integer(2)


def test_add():
    assert pytest.approx(0.3) == add(0.1, 0.2)


def test_pass():
    assert 1 == 1


def test_fail():
    assert True