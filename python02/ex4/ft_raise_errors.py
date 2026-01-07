#!/usr/bin/env python3
"""
Exercise 4: Raising Your Own Errors

Validate plant monitoring inputs and raise clear ValueErrors.
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant inputs and return a success message if valid."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Demonstrate success and different validation failures."""
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as exc:
        print(f"Error: {exc}")

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 5, 8))
    except ValueError as exc:
        print(f"Error: {exc}")

    print("Testing bad water level...")
    try:
        print(check_plant_health("lettuce", 15, 8))
    except ValueError as exc:
        print(f"Error: {exc}")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("carrot", 5, 0))
    except ValueError as exc:
        print(f"Error: {exc}")

    print("All error raising tests completed!")


def main():
    """Program entry point."""
    test_plant_checks()


if __name__ == "__main__":
    main()
