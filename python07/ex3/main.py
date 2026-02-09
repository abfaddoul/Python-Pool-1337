from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main():
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()

    print("Hand:", result["hand"], "\n")
    actions = result["turn_execution"].get("actions", {})
    print("Turn execution:")
    print("Strategy:", result["turn_execution"].get("strategy"))
    print("Actions:", actions)

    print("\nGame Report:")
    print(result["game_report"])

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
        )


if __name__ == "__main__":
    main()
