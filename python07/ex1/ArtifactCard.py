# ex1/ArtifactCard.py
from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
            self, name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
            ):
        super().__init__(name, cost, rarity)

        if durability <= 0:
            raise ValueError("Durability must be a positive integer")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> Dict:
        self.durability -= 1
        return {
            "artifact": self.name,
            "durability_left": self.durability,
            "ability_activated": True
        }
