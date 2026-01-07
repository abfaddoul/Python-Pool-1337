#!/usr/bin/env python3
"""Weekly growth simulation demo.

This module demonstrates:
- Mutating object state via methods
- Tracking deltas (growth over time)
- A simple loop-based simulation
"""


class Plant:
    """Represent a plant that can grow and age over time."""

    def __init__(self, name, height_cm, age_days):
        """Initialize a Plant.

        Args:
            name (str): Plant name.
            height_cm (int): Height in centimeters.
            age_days (int): Age in days.
        """
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm=1):
        """Increase plant height.

        Args:
            cm (int): Centimeters to add (default: 1).
        """
        self.height_cm += cm

    def age(self, days=1):
        """Increase plant age.

        Args:
            days (int): Days to add (default: 1).
        """
        self.age_days += days

    def get_info(self):
        """Return a human-readable info string for this plant."""
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


def main():
    """Simulate one week of plant growth and print a report."""
    plant = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(plant.get_info())

    start_height = plant.height_cm

    for _ in range(6):
        plant.grow(1)
        plant.age(1)

    print("=== Day 7 ===")
    print(plant.get_info())
    print(f"Growth this week: +{plant.height_cm - start_height}cm")


if __name__ == "__main__":
    main()
