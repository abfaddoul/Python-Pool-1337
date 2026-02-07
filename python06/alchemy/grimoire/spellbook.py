# alchemy/grimoire/spellbook.py


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients  # late import

    result = validate_ingredients(ingredients)

    if result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
