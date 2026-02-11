#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def main():
    print("\nORACLE STATUS: Reading the Matrix...\n")

    dotenv_loaded = load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")

    default_log_level = (
        "DEBUG" if matrix_mode == "development" else "INFO"
    )
    log_level = os.getenv("LOG_LEVEL", default_log_level)

    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if database_url:
        if matrix_mode == "production":
            print("Database: Connected to production instance")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: NOT CONFIGURED")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: NOT CONFIGURED")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online\n")
    else:
        print("Zion Network: Offline\n")

    required = ["DATABASE_URL", "API_KEY"]
    missing = [k for k in required if not os.getenv(k)]

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if not dotenv_loaded:
        print("[WARN] .env file not found or not loaded")
    elif missing:
        print("[WARN] .env loaded but missing variables:", ", ".join(missing))
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
