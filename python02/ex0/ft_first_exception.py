#!/usr/bin/env python3
"""
Exercise 0: Agricultural Data Validation Pipeline

This module validates temperature data coming as strings
and demonstrates basic exception handling.
"""


def check_temperature(temp_str):
    """
    Check if a temperature string is valid for plants (0 to 40).

    Args:
        temp_str (str): Temperature value as a string.

    Returns:
        int or None: Valid temperature or None if invalid.
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None

    return temp


def test_temperature_input():
    """
    Test the temperature checker with valid and invalid inputs.
    """
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        print(f"Testing temperature: {value}")
        result = check_temperature(value)
        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")

    print("All tests completed - program didn't crash!")


def main():
    """Program entry point."""
    test_temperature_input()


if __name__ == "__main__":
    main()
