from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("\n=== DataDeck Deck Builder ===\n")

    deck = Deck()

    creature = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    spell = SpellCard(
        name="Lightning Bolt",
        cost=4,
        rarity="Common",
        effect_type="damage"
    )

    artifact = ArtifactCard(
        name="Mana Crystal",
        cost=3,
        rarity="Rare",
        durability=3,
        effect="Permanent: +1 mana per turn"
    )

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    print("Deck stats:", deck.get_deck_stats())
    print("\nDrawing and playing cards:\n")

    deck.shuffle()

    while True:
        try:
            card = deck.draw_card()
            print(f"Drew: {card.name} ({card.get_card_info()['type']})")
            print("Play result:", card.play({}))
        except ValueError:
            break

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
