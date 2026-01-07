#!/usr/bin/env python3
"""Position Tracker - 3D coordinates using tuples (Z = height)."""

import math


def create_position(x, y, z):
    """Create a 3D position as a tuple (x, y, z) where z is height."""
    return (x, y, z)


def distance_3d(p1, p2):
    """Compute Euclidean distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(text):
    """Parse a 'x,y,z' string into a 3D position tuple of ints."""
    parts = text.split(",")
    if len(parts) != 3:
        raise ValueError("Coordinates must have exactly 3 values: x,y,z")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main():
    """Demonstrate tuple-based 3D coordinate processing."""
    print("=== Game Coordinate System ===")

    origin = create_position(0, 0, 0)
    position = create_position(10, 20, 5)
    dist = distance_3d(origin, position)

    print("Coordinate convention: (x, y, z) with z = height")
    print(f"Position created: {position}")
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    valid_text = "3,4,2"
    print(f'Parsing coordinates: "{valid_text}"')
    try:
        parsed = parse_coordinates(valid_text)
        print(f"Parsed position: {parsed}")
        print(
            f"Distance between {origin} and {parsed}: "
            f"{distance_3d(origin, parsed)}"
        )
    except ValueError as exc:
        print(f"Error parsing coordinates: {exc}")

    invalid_text = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_text}"')
    try:
        parse_coordinates(invalid_text)
    except ValueError as exc:
        print(f"Error parsing coordinates: {exc}")
        print(
            "Error details - Type: "
            f"{type(exc).__name__}, Args: {exc.args}"
        )

    print("Unpacking demonstration:")
    x, y, z = parse_coordinates("3,4,2")
    print(f"Player at x={x}, y={y}, height={z}")
    print(f"Coordinates: X={x}, Y={y}, Z(height)={z}")


if __name__ == "__main__":
    main()
