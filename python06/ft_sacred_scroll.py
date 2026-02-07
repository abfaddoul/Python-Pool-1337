#!/usr/bin/env python3
# ft_sacred_scroll.py

import alchemy
import alchemy.elements as elements


def safe_call_attr(label, module, attr):
    try:
        func = getattr(module, attr)
        print(f"{label}: {func()}")
    except AttributeError:
        print(f"{label}: AttributeError - not exposed")


print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
print("alchemy.elements.create_fire():", elements.create_fire())
print("alchemy.elements.create_water():", elements.create_water())
print("alchemy.elements.create_earth():", elements.create_earth())
print("alchemy.elements.create_air():", elements.create_air())
print()

print("Testing package-level access (controlled by __init__.py):")
safe_call_attr("alchemy.create_fire()", alchemy, "create_fire")
safe_call_attr("alchemy.create_water()", alchemy, "create_water")
safe_call_attr("alchemy.create_earth()", alchemy, "create_earth")
safe_call_attr("alchemy.create_air()", alchemy, "create_air")
print()

print("Package metadata:")
print("Version:", alchemy.__version__)
print("Author:", alchemy.__author__)
