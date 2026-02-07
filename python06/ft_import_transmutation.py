# ft_import_transmutation.py

print("=== Import Transmutation Mastery ===\n")

# Method 1 - Full module import:
import alchemy.elements as elements  # noqa: E402

print("Method 1 - Full module import:")
print("alchemy.elements.create_fire():", elements.create_fire())

# Method 2 - Specific function import:
from alchemy.elements import create_water  # noqa: E402

print("\nMethod 2 - Specific function import:")
print("create_water():", create_water())

# Method 3 - Aliased import:
from alchemy.potions import healing_potion as heal  # noqa: E402

print("\nMethod 3 - Aliased import:")
print("heal():", heal())

# Method 4 - Multiple imports:
from alchemy.elements import create_earth, create_fire  # noqa: E402
from alchemy.potions import strength_potion  # noqa: E402

print("\nMethod 4 - Multiple imports:")
print("create_earth():", create_earth())
print("create_fire():", create_fire())
print("strength_potion():", strength_potion())

print("\nAll import transmutation methods mastered!")
