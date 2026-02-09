from typing import Dict, List

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return list(available_targets)

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        mana_budget = 6

        playable = [c for c in hand if c.is_playable(mana_budget)]

        def get_card_cost(card):
            return card.cost

        playable.sort(key=get_card_cost)

        cards_played = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = ["Enemy Player"]

        for card in playable:
            if mana_budget < card.cost:
                continue

            mana_budget -= card.cost
            mana_used += card.cost
            cards_played.append(card.name)

            if card in hand:
                hand.remove(card)

            battlefield.append(card)

            info = card.get_card_info()
            card_type = info.get("type", "")

            if card_type == "Creature":
                damage_dealt += int(info.get("attack", 0))
            elif card_type == "Spell":
                damage_dealt += 3

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets_attacked,
                "damage_dealt": damage_dealt
            }
        }
