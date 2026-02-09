# ex1/Deck.py
from typing import List, Dict
import random

from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if not self._cards:
            raise ValueError("Cannot draw from an empty deck")
        return self._cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total = len(self._cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self._cards:
            info = card.get_card_info()
            total_cost += card.cost

            card_type = info.get("type", "")
            if card_type == "Creature":
                creatures += 1
            elif card_type == "Spell":
                spells += 1
            elif card_type == "Artifact":
                artifacts += 1

        avg_cost = (total_cost / total) if total else 0.0

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
