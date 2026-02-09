from typing import Dict, List

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense_power: int
    ):
        super().__init__(name, cost, rarity)

        if attack_power <= 0 or defense_power < 0:
            raise ValueError("Attack must be > 0 and defense must be >= 0")

        self.attack_power = attack_power
        self.defense_power = defense_power
        self.total_mana = 0

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed (combat + magic ready)"
        }

    def attack(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(self.defense_power, max(0, incoming_damage))
        taken = max(0, incoming_damage - blocked)

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense_power
        }

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        mana_used = min(4, self.total_mana)
        self.total_mana -= mana_used

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> Dict:
        if amount < 0:
            raise ValueError("Amount must be >= 0")

        self.total_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.total_mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "total_mana": self.total_mana
        }
