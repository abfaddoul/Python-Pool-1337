#!/usr/bin/env python3
"""
Exercise 5: Garden Management System

Demonstrates a complete error-handling workflow using
custom exceptions, try/except/finally, and raise.
"""


class GardenError(Exception):
    """Base class for all garden-related errors."""


class PlantError(GardenError):
    """Raised when there is a plant-related problem."""


class WaterError(GardenError):
    """Raised when there is a watering-related problem."""


class GardenManager:
    """Manage plants, watering, and health checks."""

    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        """Add a plant to the garden."""
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        """Water all plants with cleanup guaranteed."""
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")

            for plant in self.plants:
                print(f"Watering {plant} - success")

        except WaterError as exc:
            print(f"Caught GardenError: {exc}")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        """Check plant health and raise errors for invalid conditions."""
        if water_level < 1 or water_level > 10:
            raise ValueError(
                f"Water level {water_level} is invalid (1–10)"
            )

        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is invalid (2–12)"
            )

        print(
            f"{plant_name}: healthy "
            f"(water: {water_level}, sun: {sunlight_hours})"
        )


def main():
    """Demonstrate the garden management system."""
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as exc:
        print(f"Error adding plant: {exc}")

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 8)
    except ValueError as exc:
        print(f"Error checking lettuce: {exc}")

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as exc:
        print(f"Caught GardenError: {exc}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
