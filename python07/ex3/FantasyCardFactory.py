import random
from typing import Dict

from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power=None):
        creatures = [
            ("Goblin Warrior", 2, "Common", 2, 2),
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Elf Archer", 3, "Rare", 3, 2),
        ]

        name, cost, rarity, attack, health = random.choice(creatures)
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power=None):
        spells = [
            ("Fireball", 3, "Common", "damage"),
            ("Lightning Bolt", 3, "Rare", "damage"),
            ("Healing Light", 2, "Common", "heal"),
        ]

        name, cost, rarity, effect_type = random.choice(spells)
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power=None):
        artifacts = [
            ("Mana Ring", 2, "Rare", 3, "+1 mana per turn"),
            ("Ancient Staff", 4, "Epic", 5, "Spell damage +1"),
        ]

        name, cost, rarity, durability, effect = random.choice(artifacts)
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> Dict:
        deck = []

        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])

            if choice == "creature":
                deck.append(self.create_creature())
            elif choice == "spell":
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())

        return {
            "theme": "Fantasy",
            "size": size,
            "cards": deck
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["goblin", "dragon", "elf"],
            "spells": ["fireball", "lightning", "heal"],
            "artifacts": ["ring", "staff"],
        }
