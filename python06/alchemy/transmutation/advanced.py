# alchemy/transmutation/advanced.py

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    gold = lead_to_gold()
    heal = healing_potion()
    return (
        "Philosopher's stone created using "
        f"{gold} and {heal}"
    )


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
