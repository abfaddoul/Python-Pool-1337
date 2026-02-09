from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Epic",
        attack_power=5,
        defense_power=3
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    print("Play result:", elite.play({}))

    print("\nCombat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(5))
    print("Combat stats:", elite.get_combat_stats())

    print("\nMagic phase:")
    print("Magic stats (before):", elite.get_magic_stats())
    print("Mana channel:", elite.channel_mana(7))
    print("Magic stats (after channel):", elite.get_magic_stats())
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Magic stats (after spell):", elite.get_magic_stats())

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
