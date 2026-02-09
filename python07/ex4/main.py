from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary")
    wizard = TournamentCard("wizard_001", "Ice Wizard", 3, "Rare")

    print("Fire Dragon (ID:", dragon.card_id, ")", sep="")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", dragon.calculate_rating())
    print("- Record:", dragon.get_rank_info().get("record", "0-0"), "\n")

    print("Ice Wizard (ID:", wizard.card_id, ")", sep="")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", wizard.calculate_rating())
    print("- Record:", wizard.get_rank_info().get("record", "0-0"), "\n")

    platform.register_card(dragon)
    platform.register_card(wizard)

    print("Creating tournament match...")
    result = platform.create_match(dragon.card_id, wizard.card_id)
    print("Match result:", result, "\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for row in leaderboard:
        print(
            f"{row['rank']}. {row['name']}"
            f"- Rating: {row['rating']} ({row['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
