import random
from typing import Dict, Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Multiple inheritance:
    - Card: identity + base card behavior
    - Combatable: attack capability
    - Rankable: ranking capability (wins/losses/rating)
    """

    def __init__(
            self, card_id: str, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id

        self._wins = 0
        self._losses = 0
        self._rating = 1200

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_id": self.card_id,
            "played": True,
            "card": self.get_card_info(),
            "tournament": self.get_tournament_stats(),
        }

    def attack(self, target: Any) -> Dict:
        """
        Minimal combat model:
        - Compute "power" from rating + randomness
        - Winner decided by comparing power values
        """
        my_power = self._combat_power()
        target_power = target._combat_power() if hasattr(
            target, "_combat_power") else 0

        winner = self if my_power >= target_power else target
        loser = target if winner is self else self

        return {
            "attacker": self.card_id,
            "defender": getattr(target, "card_id", "unknown"),
            "attacker_power": my_power,
            "defender_power": target_power,
            "winner": getattr(winner, "card_id", "unknown"),
            "loser": getattr(loser, "card_id", "unknown"),
        }

    def defend(self, attacker: Any) -> Dict:
        """
        Combatable requirement: defend against an attacker.
        We return a defense value (simple, deterministic-ish).
        """
        defense = random.randint(0, 10)
        return {
            "defender": self.card_id,
            "attacker": getattr(attacker, "card_id", "unknown"),
            "defense": defense,
        }

    def get_combat_stats(self) -> Dict:
        """
        Combatable requirement: expose combat-related stats.
        """
        return {
            "id": self.card_id,
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses,
        }

    def _combat_power(self) -> int:
        # Rating influences outcome + small randomness for variety
        return int(self._rating + random.randint(-50, 50))

    # -----------------------
    # Rankable behavior
    # -----------------------
    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            return
        self._wins += wins
        self._rating = self._apply_rating(win=True)

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            return
        self._losses += losses
        self._rating = self._apply_rating(win=False)

    def _apply_rating(self, win: bool) -> int:
        """
        Simple Elo-like delta (lightweight, deterministic enough):
        - win: +16
        - loss: -66
        clamp minimum rating at 0
        """
        points = 16 if win else -66
        new_rating = self._rating + points
        return max(0, new_rating)

    def get_rank_info(self) -> Dict:
        return {
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses,
            "record": f"{self._wins}-{self._losses}",
        }

    def get_tournament_stats(self) -> Dict:
        return {
            "id": self.card_id,
            "name": getattr(self, "name", ""),
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses,
        }
