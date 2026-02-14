#!/usr/bin/env python3


def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def add_power(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    storage: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        storage[key] = value

    def recall(key: str) -> str:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(10)
    print("Add 5:", acc(5))
    print("Add 3:", acc(3))
    print("Add 20:", acc(20))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", "Ancient Rune")
    vault["store"]("level", "Master")
    print("Recall secret:", vault["recall"]("secret"))
    print("Recall level:", vault["recall"]("level"))
    print("Recall missing:", vault["recall"]("dragon"))


if __name__ == "__main__":
    main()
