# ex0/main.py
from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")

    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", dragon.is_playable(6))
    print("Play result:", dragon.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print(dragon.attack_target("Goblin Warrior"))

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", dragon.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
