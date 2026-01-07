#!/usr/bin/env python3
"""Plant types demo using inheritance.

This module demonstrates:
- Base class + derived classes
- Specialized behavior (bloom, shade calculation)
- Reusing core attributes via super()
"""


class Plant:
    """Base class representing common attributes for plants."""

    def __init__(self, name, height_cm, age_days):
        """Initialize shared plant attributes."""
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def info(self):
        """Return a generic info string for the plant."""
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days"


class Flower(Plant):
    """A plant type that can bloom and has a flower color."""

    def __init__(self, name, height_cm, age_days, color):
        """Initialize a flower with its color."""
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self):
        """Print a blooming message (demo behavior)."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """A plant type that can provide shade and has a trunk diameter."""

    def __init__(self, name, height_cm, age_days, trunk_diameter):
        """Initialize a tree with trunk diameter (cm)."""
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Compute and print an estimated shade area (demo metric)."""
        shade = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """A plant type representing a vegetable
    with harvest and nutrition metadata."""

    def __init__(
        self,
        name,
        height_cm,
        age_days,
        harvest_season,
        nutritional_value,
    ):
        """Initialize a vegetable with harvest season and nutritional value."""
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main():
    """Instantiate multiple plant types and print their details."""
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 60, "spring", "vitamin A")

    print(rose.info(), "-", rose.color)
    rose.bloom()

    print(tulip.info(), "-", tulip.color)
    tulip.bloom()

    print(oak.info(), "-", oak.trunk_diameter, "cm trunk")
    oak.produce_shade()

    print(pine.info(), "-", pine.trunk_diameter, "cm trunk")
    pine.produce_shade()

    print(tomato.info(), "-", tomato.harvest_season, "harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")

    print(carrot.info(), "-", carrot.harvest_season, "harvest")
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")


if __name__ == "__main__":
    main()
