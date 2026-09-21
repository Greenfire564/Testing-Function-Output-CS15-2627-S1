import pytest


# =====================================================================
# Functions to Test
# =====================================================================

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate Body Mass Index (BMI).

    :param weight_kg: Weight in kilograms.
    :param height_m: Height in meters.
    :return: Calculated BMI index.
    """
    return weight_kg / (height_m ** 2)


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    :param celsius: Temperature in degrees Celsius.
    :return: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after applying a percentage discount.

    :param price: Original price.
    :param discount_percent: Discount percentage (0-100).
    :return: Final discounted price.
    """
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


# =====================================================================
# PyTest Cases
# =====================================================================

# --- Function 1 Tests: calculate_bmi ---

def test_calculate_bmi_standard():
    # 70 kg, 1.75 m -> BMI is approx 22.857
    assert pytest.approx(22.857, rel=1e-3) == calculate_bmi(70, 1.75)


def test_calculate_bmi_round_numbers():
    # 80 kg, 2.0 m -> BMI should be exactly 20.0
    assert calculate_bmi(80, 2.0) == 20.0


# --- Function 2 Tests: convert_celsius_to_fahrenheit ---

def test_convert_celsius_freezing():
    # 0°C should be exactly 32°F
    assert convert_celsius_to_fahrenheit(0) == 32.0


def test_convert_celsius_boiling():
    # 100°C should be exactly 212°F
    assert convert_celsius_to_fahrenheit(100) == 212.0


# --- Function 3 Tests: calculate_discount ---

def test_calculate_discount_half_off():
    # 50% off $100 should be $50.00
    assert calculate_discount(100.0, 50.0) == 50.0


def test_calculate_discount_decimal_price():
    # 15% off $19.99 should be approx $16.9915
    assert pytest.approx(16.9915) == calculate_discount(19.99, 15.0)