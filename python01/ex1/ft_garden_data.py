#!/usr/bin/env python3
"""Plant registry demo (class + instances).

This module demonstrates:
- Defining a class
- Creating multiple objects
- Returning a summary string from a method
"""


class Plant:
    """Represent a plant with a name, height (cm), and age (days)."""

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

    def summary(self):
        """Return a compact, human-readable summary of this plant."""
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


def main():
    """Create sample plants and print their registry summaries."""
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(plant1.summary())
    print(plant2.summary())
    print(plant3.summary())


if __name__ == "__main__":
    main()
