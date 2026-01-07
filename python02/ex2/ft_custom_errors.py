#!/usr/bin/env python3
"""
Exercise 2: Making Your Own Error Types

Demonstrates custom exceptions and inheritance.
"""


class GardenError(Exception):
    """Base exception for garden-related problems."""


class PlantError(GardenError):
    """Exception for plant-related issues."""


class WaterError(GardenError):
    """Exception for watering-related issues."""


def test_custom_errors():
    """Test raising and catching custom garden errors."""
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as exc:
        print(f"Caught PlantError: {exc}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as exc:
        print(f"Caught WaterError: {exc}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as exc:
        print(f"Caught a garden error: {exc}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as exc:
        print(f"Caught a garden error: {exc}")

    print("All custom error types work correctly!")


def main():
    """Program entry point."""
    test_custom_errors()


if __name__ == "__main__":
    main()
