#!/usr/bin/env python3
"""Garden management system demo.

This module demonstrates:
- Inheritance hierarchy (Plant -> FloweringPlant -> PrizeFlower)
- A manager class with:
  - class variable (total_gardens)
  - nested class (GardenStats)
  - instance state (plants, owner)
  - staticmethod and classmethod utilities
- Lightweight reporting / analytics
"""


class Plant:
    """Base plant with a grow operation."""

    def __init__(self, name, height_cm):
        """Initialize a plant with a name and current height."""
        self.name = name
        self.height_cm = height_cm

    def grow(self, cm=1):
        """Increase plant height and log the operation.

        Args:
            cm (int): Growth increment in centimeters (default: 1).
        """
        self.height_cm += cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    """Plant that can bloom and has a flower color."""

    def __init__(self, name, height_cm, color):
        """Initialize a flowering plant with bloom state."""
        super().__init__(name, height_cm)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        """Mark the plant as blooming."""
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    """A flowering plant with prize points (e.g., competition scoring)."""

    def __init__(self, name, height_cm, color, prize_points):
        """Initialize prize flower with additional scoring metadata."""
        super().__init__(name, height_cm, color)
        self.prize_points = prize_points


class GardenManager:
    """Manage a collection of plants for a given owner and produce reports."""

    total_gardens = 0

    class GardenStats:
        """Encapsulate simple garden analytics operations."""

        def count_plants(self, plants):
            """Return the number of plants tracked."""
            return len(plants)

        def total_growth(self, start_heights, plants):
            """Compute total growth across all plants.

            Args:
                start_heights (dict): Mapping of plant object
                    to its starting height.
                plants (list): Plants to measure.

            Returns:
                int: Total growth in centimeters.
            """
            total = 0
            for p in plants:
                total += p.height_cm - start_heights[p]
            return total

        def count_types(self, plants):
            """Count plant types by runtime class.

            Returns:
                tuple: (regular_count, flowering_count, prize_count)
            """
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def __init__(self, owner):
        """Initialize a manager for a specific garden owner.

        Args:
            owner (str): Owner name used in reporting/logging.
        """
        self.owner = owner
        self.plants = []
        self._stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """Add a plant to the garden portfolio.

        Args:
            plant (Plant): A plant instance to track.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self, cm=1):
        """Apply growth across all plants and trigger bloom where applicable.

        Args:
            cm (int): Growth increment for each plant (default: 1).

        Returns:
            dict: start_heights mapping plant -> height before growth.
        """
        start_heights = {}
        for p in self.plants:
            start_heights[p] = p.height_cm

        print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow(cm)
            if isinstance(p, FloweringPlant):
                p.bloom()

        return start_heights

    def report(self, start_heights):
        """Print a structured report for the garden.

        Args:
            start_heights (dict): Plant -> height snapshot before growth.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        for p in self.plants:
            if isinstance(p, PrizeFlower):
                bloom_state = "blooming" if p.is_blooming else "not blooming"
                print(
                    f"- {p.name}: {p.height_cm}cm, {p.color} flowers "
                    f"({bloom_state}), Prize points: {p.prize_points}"
                )
            elif isinstance(p, FloweringPlant):
                bloom_state = "blooming" if p.is_blooming else "not blooming"
                print(
                    f"- {p.name}: {p.height_cm}cm, {p.color} flowers "
                    f"({bloom_state})"
                )
            else:
                print(f"- {p.name}: {p.height_cm}cm")

        plants_added = self._stats.count_plants(self.plants)
        total_growth = self._stats.total_growth(start_heights, self.plants)
        regular, flowering, prize = self._stats.count_types(self.plants)

        print(f"Plants added: {plants_added}, Total growth: {total_growth}cm")
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers"
        )

    @staticmethod
    def is_valid_height(height_cm):
        """Validate height as a non-negative value."""
        return height_cm >= 0

    @classmethod
    def create_garden_network(cls, *owners):
        """Create multiple GardenManager instances from a list of owners."""
        return [cls(owner) for owner in owners]


def main():
    """Run a small demo scenario for the garden management system."""
    print("=== Garden Management System Demo ===")

    managers = GardenManager.create_garden_network("Alice", "Bob")
    alice = managers[0]

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    start = alice.help_all_grow(1)
    alice.report(start)

    print(f"Height validation test: {GardenManager.is_valid_height(10)}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
