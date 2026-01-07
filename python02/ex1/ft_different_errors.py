#!/usr/bin/env python3
"""
Exercise 1: Different Types of Problems

Demonstrates handling multiple built-in exception types
without crashing the program.
"""


def garden_operations():
    """Trigger and catch different common Python errors."""

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as exc:
        print(f"Caught ValueError: {exc}")

    print("Testing ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as exc:
        print(f"Caught ZeroDivisionError: {exc}")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as exc:
        print(f"Caught FileNotFoundError: {exc}")

    print("Testing KeyError...")
    plants = {"tomato": 5, "lettuce": 7}
    try:
        _ = plants["missing_plant"]
    except KeyError as exc:
        print(f"Caught KeyError: {exc}")


def test_error_types():
    """Run all error tests and show grouped exception handling."""
    print("=== Garden Error Types Demo ===")

    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


def main():
    """Program entry point."""
    test_error_types()


if __name__ == "__main__":
    main()
