#!/usr/bin/env python3
"""Achievement Hunter - Track and analyze unique achievements with sets."""


def count_occurrences(achievement, player_sets):
    """Count how many player sets contain a given achievement."""
    count = 0
    for achievements in player_sets:
        if achievement in achievements:
            count += 1
    return count


def main():
    """Demonstrate set-based achievement tracking and analytics."""
    print("=== Achievement Tracker System ===")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    player_sets = [alice, bob, charlie]
    rare_achievements = set()
    for achievement in all_achievements:
        if count_occurrences(achievement, player_sets) == 1:
            rare_achievements.add(achievement)
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
