import sys


def check_package(name: str, required: bool, role: str) -> bool:
    """
    Check if a package is installed, print its status + version.
    Returns True if installed, False otherwise.
    """
    try:
        module = __import__(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {role}")
        return True
    except ImportError:
        if required:
            print(f"[MISSING] {name} - {role}")
        else:
            print(f"[INFO] {name} - optional (not installed)")
        return False


def print_install_instructions() -> None:
    print("\nERROR: Missing required dependencies.")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def run_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.DataFrame({
        "x": np.arange(10),
        "y": np.arange(10)
    })

    plt.plot(df["x"], df["y"])

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    ok = True
    ok = check_package("pandas", True, "Data manipulation") and ok
    ok = check_package("numpy", True, "Numerical computations") and ok
    ok = check_package("matplotlib", True, "Visualization") and ok
    check_package("requests", False, "Network access")

    if not ok:
        print_install_instructions()
        sys.exit(1)

    try:
        run_analysis()
    except Exception as e:
        print("\nERROR: Analysis failed unexpectedly.")
        print(f"Details: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
