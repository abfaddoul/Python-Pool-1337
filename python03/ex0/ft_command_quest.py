#!/usr/bin/env python3
"""Command Quest - Discover command-line arguments."""

import sys


def main():
    """Display program name and command-line arguments."""
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {len(sys.argv)}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(arguments)}")

    index = 1
    for arg in arguments:
        print(f"Argument {index}: {arg}")
        index += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
