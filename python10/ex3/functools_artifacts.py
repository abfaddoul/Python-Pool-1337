#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": operator.gt,
        "min": operator.lt,
    }

    if operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)

    if operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)

    if operation not in operations:
        raise ValueError("Unsupported operation")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatch(spell):
        raise TypeError("Unknown spell type")

    @dispatch.register
    def _(spell: int):
        return f"Damage spell cast! {spell} damage dealt."

    @dispatch.register
    def _(spell: str):
        return f"Enchantment spell applied: {spell}"

    @dispatch.register
    def _(spell: list):
        return f"Multi-cast spell with {len(spell)} effects."

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    try:
        print(dispatcher(100))
        print(dispatcher("fire shield"))
        print(dispatcher([10, 20, 30]))
        print(dispatcher(3.14))
    except TypeError as e:
        print(e)

    print("\nTesting spell partial enchanter...")

    def enchant(power, element, target):
        return f"{element.upper()} enchant | power={power} | target={target}"

    spells = partial_enchanter(enchant)
    print(spells["fire_enchant"]("dragon"))
    print(spells["ice_enchant"]("goblin"))
    print(spells["lightning_enchant"]("troll"))
