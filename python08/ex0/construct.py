# ex0/construct.py
import os
import site
import sys
from typing import Optional


def _get_venv_path() -> Optional[str]:
    """
    Return venv root path if running inside a virtual environment, else None.
    Detection strategy:
    - sys.prefix differs from sys.base_prefix inside venv (standard behavior)
    - VIRTUAL_ENV env var often set on Unix shells
    """
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    if sys.prefix != base_prefix:
        return sys.prefix

    venv_env = os.environ.get("VIRTUAL_ENV")
    if venv_env:
        return venv_env

    return None


def _safe_site_packages() -> list[str]:
    """Return discovered site-packages paths, defensively."""
    paths: list[str] = []
    try:
        paths.extend(site.getsitepackages())
    except Exception:
        # Some environments (or permissions) may block getsitepackages()
        pass

    try:
        user_site = site.getusersitepackages()
        if user_site:
            paths.append(user_site)
    except Exception:
        pass

    # Remove duplicates while preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for p in paths:
        if p not in seen:
            unique.append(p)
            seen.add(p)
    return unique


def main() -> None:
    venv_path = _get_venv_path()
    python_path = sys.executable

    if venv_path is None:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows\n")
        print("Then run this program again.\n")

        print("Global/Current package locations (site-packages candidates):")
        for p in _safe_site_packages():
            print(f"- {p}")
        return

    # Inside venv
    venv_name = os.path.basename(os.path.normpath(venv_path))
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    print("Package installation path (site-packages candidates):")
    for p in _safe_site_packages():
        print(f"- {p}")


if __name__ == "__main__":
    main()
