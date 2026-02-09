from typing import Dict, List, Optional

from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None

        self._hand: List[Card] = []
        self._battlefield: List[Card] = []

        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
            self,
            factory: CardFactory, strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy

    def _require_configured(self) -> None:
        if self._factory is None or self._strategy is None:
            raise RuntimeError(
                "Engine not configured: factory and strategy are required"
            )

    def _draw_initial_hand_if_needed(self) -> None:
        if self._factory is None:
            return

        while len(self._hand) < 3:
            choice = (self._cards_created % 3)
            if choice == 0:
                self._hand.append(self._factory.create_creature())
            elif choice == 1:
                self._hand.append(self._factory.create_spell())
            else:
                self._hand.append(self._factory.create_artifact())
            self._cards_created += 1

    def simulate_turn(self) -> Dict:
        self._require_configured()
        self._draw_initial_hand_if_needed()

        hand_before = [f"{c.name} ({c.cost})" for c in self._hand]
        strategy_report = self._strategy.execute_turn(
            self._hand,
            self._battlefield)
        actions = strategy_report.get("actions", {})
        damage = int(actions.get("damage_dealt", 0))

        self._turns_simulated += 1
        self._total_damage += damage

        return {
            "turn": self._turns_simulated,
            "strategy": self._strategy.get_strategy_name(),
            "hand_before": hand_before,
            "hand": [f"{c.name} ({c.cost})" for c in self._hand],
            "battlefield": [c.name for c in self._battlefield],
            "turn_execution": strategy_report,
            "game_report": {
                "turns_simulated": self._turns_simulated,
                "strategy_used": self._strategy.get_strategy_name(),
                "total_damage": self._total_damage,
                "cards_created": self._cards_created,
            },
        }

    def get_engine_status(self) -> Dict:
        self._require_configured()
        return {
            "factory": self._factory.__class__.__name__,
            "strategy": self._strategy.get_strategy_name(),
            "turns_simulated": self._turns_simulated,
            "cards_created": self._cards_created,
            "hand_size": len(self._hand),
            "battlefield_size": len(self._battlefield),
            "total_damage": self._total_damage,
        }
