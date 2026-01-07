#!/usr/bin/env python3
"""Secure plant demo with guarded setters.

This module demonstrates:
- Using underscore-prefixed attributes as an encapsulation convention
- Validating updates through setter methods
- Producing security-style logs for rejected operations
"""


class SecurePlant:
    """A plant model that prevents invalid (negative) height/age updates."""

    def __init__(self, name):
        """
        Initialize a secure plant with a default safe state
        (0 height, 0 age).
        """
        self.name = name
        self._height_cm = 0
        self._age_days = 0

    def set_height(self, height_cm):
        """Set plant height after validation.

        Args:
            height_cm (int): New height in centimeters.

        Notes:
            Negative values are rejected to protect state integrity.
        """
        if height_cm < 0:
            print(
                f"Invalid operation attempted: height {height_cm}cm "
                f"[REJECTED]"
            )
            print("Security: Negative height rejected")
            return
        self._height_cm = height_cm
        print(f"Height updated: {self._height_cm}cm [OK]")

    def set_age(self, age_days):
        """Set plant age after validation.

        Args:
            age_days (int): New age in days.

        Notes:
            Negative values are rejected to protect state integrity.
        """
        if age_days < 0:
            print(
                f"Invalid operation attempted: age {age_days} days "
                f"[REJECTED]"
            )
            print("Security: Negative age rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days [OK]")

    def get_height(self):
        """Return current height in centimeters."""
        return self._height_cm

    def get_age(self):
        """Return current age in days."""
        return self._age_days

    def info(self):
        """Return a human-readable info string."""
        return f"{self.name} ({self._height_cm}cm, {self._age_days} days)"


def main():
    """Run a small scenario to show valid and invalid updates."""
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)

    print(f"Current plant: {plant.info()}")


if __name__ == "__main__":
    main()
