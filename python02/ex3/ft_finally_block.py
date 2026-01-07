#!/usr/bin/env python3
"""
Exercise 3: Finally Block - Always Clean Up

Demonstrates using finally to ensure cleanup always happens.
"""


def water_plants(plant_list):
    """Water each plant and always close the watering system."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as exc:
        print(f"Error: {exc}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Demonstrate normal watering and watering with an error."""
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])

    print("Cleanup always happens, even with errors!")


def main():
    """Program entry point."""
    test_watering_system()


if __name__ == "__main__":
    main()
