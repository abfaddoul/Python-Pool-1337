#!/usr/bin/env python3
"""Plant factory output demo.

This module demonstrates:
- Building objects from structured specs (tuples)
- Collecting objects in a list
- Iterating and reporting results
"""


class Plant:
    """Represent a plant with a compact summary for reporting."""

    def __init__(self, name, height_cm, age_days):
        """Initialize a Plant from its core attributes."""
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def summary(self):
        """Return a short summary string for logging/reporting."""
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"


def main():
    """Create multiple plants from specs and print factory output."""
    specs = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []

    for spec in specs:
        plant = Plant(spec[0], spec[1], spec[2])
        plants.append(plant)

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.summary()}")

    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
