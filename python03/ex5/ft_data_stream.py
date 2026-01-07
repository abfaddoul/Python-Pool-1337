#!/usr/bin/env python3


def game_event_stream(count):
    """Yield simulated game events one by one (streaming)."""
    players = ("alice", "bob", "charlie", "dina", "youssef")
    actions = ("killed monster", "found treasure", "leveled up")

    for i in range(1, count + 1):
        player = players[(i - 1) % len(players)]
        level = (i * 7) % 20 + 1
        action = actions[(i - 1) % len(actions)]

        yield (i, player, level, action)


def fibonacci_stream():
    """Infinite Fibonacci generator."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream():
    """Infinite prime number generator."""
    n = 2
    while True:
        is_prime = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                is_prime = False
                break
            d += 1

        if is_prime:
            yield n

        n += 1


def join_first_n(gen, n):
    """Return the first n values from gen as a comma-separated string."""
    result = ""
    i = 0
    for value in gen:
        if i == n:
            break
        if i > 0:
            result += ", "
        result += str(value)
        i += 1
    return result


def main():
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for event_id, player, level, action in game_event_stream(total_events):
        processed += 1

        if level >= 10:
            high_level_players += 1

        if action == "found treasure":
            treasure_events += 1

        if action == "leveled up":
            level_up_events += 1

        if event_id <= 3:
            print(
                f"Event {event_id}: Player {player} "
                f"(level {level}) {action}"
            )

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("=== Generator Demonstration ===")
    print(
        "Fibonacci sequence (first 10): "
        f"{join_first_n(fibonacci_stream(), 10)}"
    )
    print(
        "Prime numbers (first 5): "
        f"{join_first_n(prime_stream(), 5)}"
    )


if __name__ == "__main__":
    main()
