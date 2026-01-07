#!/usr/bin/env python3
"""
ft_analytics_dashboard.py

Exercise 6: Data Alchemist
Demonstrate list/dict/set comprehensions on sample gaming data.
Authorized: comprehensions, len(), print(), sum(), max(), min(), sorted()
"""


def format_set(values):
    """Return a stable, pretty set-like string with sorted elements."""
    return "{" + ", ".join([repr(v) for v in sorted(values)]) + "}"


def main():
    players = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "combo_50",
                "speedrunner",
            ],
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": [
                "first_kill",
                "level_10",
                "collector",
            ],
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "strategist",
                "explorer",
                "raider",
                "veteran",
            ],
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "region": "east",
            "achievements": [
                "level_10",
                "boss_slayer",
                "survivor",
                "builder",
            ],
        },
    ]

    # === List Comprehension Examples ===
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    scores_doubled = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"]]

    # === Dict Comprehension Examples ===
    player_scores = {p["name"]: p["score"] for p in players if p["active"]}

    achievement_counts = {
        p["name"]: len(p["achievements"])
        for p in players
        if p["active"]
    }

    score_categories = {
        "high": sum([1 for p in players if p["score"] >= 2100]),
        "medium": sum([1 for p in players if 1800 <= p["score"] < 2100]),
        "low": sum([1 for p in players if p["score"] < 1800]),
    }

    # === Set Comprehension Examples ===
    unique_players = {p["name"] for p in players}
    unique_achievements = {a for p in players for a in p["achievements"]}
    active_regions = {p["region"] for p in players if p["active"]}

    # === Combined Analysis ===
    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum([p["score"] for p in players]) / len(players)

    top_player = max(players, key=lambda p: p["score"])
    top_name = top_player["name"]
    top_score = top_player["score"]
    top_achievements = len(top_player["achievements"])

    # === Output ===
    print("=== Game Analytics Dashboard ===")

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {format_set(unique_players)}")
    print(f"Unique achievements: {format_set(unique_achievements)}")
    print(f"Active regions: {format_set(active_regions)}")

    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_name} "
        f"({top_score} points, {top_achievements} achievements)"
    )


if __name__ == "__main__":
    main()
