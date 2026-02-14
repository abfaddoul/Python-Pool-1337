#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(artifacts, key=lambda a: a["power"], reverse=True)
    except (TypeError, KeyError):
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(filter(lambda m: m["power"] >= min_power, mages))
    except (TypeError, KeyError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda s: f"* {s} *", spells))
    except TypeError:
        return []


def mage_stats(mages: list[dict]) -> dict:
    try:
        if not mages:
            return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

        max_mage = max(mages, key=lambda m: m["power"])
        min_mage = min(mages, key=lambda m: m["power"])
        total = sum(map(lambda m: m["power"], mages))
        avg = round(total / len(mages), 2)

        return {
            "max_power": int(max_mage["power"]),
            "min_power": int(min_mage["power"]),
            "avg_power": float(avg),
        }
    except (TypeError, KeyError, ZeroDivisionError):
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}


def _demo() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "relic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Shadow Dagger", "power": 70, "type": "weapon"},
    ]

    mages = [
        {"name": "Alex", "power": 12, "element": "fire"},
        {"name": "Jordan", "power": 8, "element": "ice"},
        {"name": "Riley", "power": 20, "element": "lightning"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        a1, a2 = sorted_artifacts[0], sorted_artifacts[1]
        print(
            f"{a1['name']} ({a1['power']} power) comes before"
            f"{a2['name']} ({a2['power']} power)"
        )

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting power filter (min_power=10)...")
    filtered = power_filter(mages, 10)
    print([m["name"] for m in filtered])

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    _demo()
