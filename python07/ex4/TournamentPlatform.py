from typing import Dict, List

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: Dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self._cards[card.card_id] = card
        return f"Registered: {card.card_id}"

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        if card1_id not in self._cards or card2_id not in self._cards:
            return {"error": "One or both card IDs not found"}

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        combat = card1.attack(card2)
        winner_id = combat.get("winner")
        loser_id = combat.get("loser")

        if winner_id not in self._cards or loser_id not in self._cards:
            return {"error": "Invalid match resolution"}

        winner = self._cards[winner_id]
        loser = self._cards[loser_id]

        # Update ranks
        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> List:
        cards = list(self._cards.values())

        def get_rating(card):
            return card.calculate_rating()

        cards.sort(key=get_rating, reverse=True)

        leaderboard = []
        for idx, c in enumerate(cards, start=1):
            info = c.get_rank_info()
            leaderboard.append({
                "rank": idx,
                "name": getattr(c, "name", ""),
                "id": c.card_id,
                "rating": info.get("rating", 0),
                "record": info.get("record", "0-0"),
            })
        return leaderboard

    def generate_tournament_report(self) -> Dict:
        total = len(self._cards)
        ratings = [c.calculate_rating() for c in self._cards.values()]
        avg_rating = int(sum(ratings) / total) if total > 0 else 0

        return {
            "total_cards": total,
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
