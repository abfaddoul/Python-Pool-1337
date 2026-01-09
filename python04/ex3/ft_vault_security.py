#!/usr/bin/env python3

def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")

    with open("classified_data.txt", "r") as file:
        print("Vault connection established with failsafe protocols")
        print("SECURE EXTRACTION:")
        print(file.read())

    with open("secure_archive.txt", "w") as file:
        print("SECURE PRESERVATION:")
        file.write("New security protocols archived\n")
        print("{[}CLASSIFIED{]} New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
