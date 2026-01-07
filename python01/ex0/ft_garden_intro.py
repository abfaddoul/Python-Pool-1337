#!/usr/bin/env python3
"""Simple entry-point script that prints a static plant snapshot.

This module demonstrates:
- Basic variables
- Formatted output with f-strings
- A conventional main() entry point
"""


def main():
    """Run a minimal program that prints a plant summary."""
    name = "Rose"
    height_cm = 25
    age_days = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height_cm}cm")
    print(f"Age: {age_days} days")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
