#!/usr/bin/env python3

def crisis_handler(filename):
    try:
        with open(filename, "r"):
            pass
        is_routine = True
    except (FileNotFoundError, PermissionError):
        is_routine = False
    except Exception:
        is_routine = False

    if is_routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        with open(filename, "r") as file:
            data = file.read()
        print(f"SUCCESS: Archive recovered - ``{data}''")
        print("STATUS: Normal operations resumed")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        try:
            with open(filename, "r") as file:
                _ = file.read()
            print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except Exception:
            print("RESPONSE: Unexpected system anomaly detected")
            print("STATUS: Crisis handled, system stable")

    print()


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
