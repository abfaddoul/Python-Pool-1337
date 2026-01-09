#!/usr/bin/env python3

import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()

    sys.stdout.write(
        "{[}STANDARD{]} Archive status from "
        + archivist_id + ": " + status + "\n"
    )

    sys.stderr.write(
        "{[}ALERT{]} System diagnostic: Communication channels verified\n"
    )

    sys.stdout.write("{[}STANDARD{]} Data transmission complete\n\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
