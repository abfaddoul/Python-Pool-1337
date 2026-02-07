# alchemy/grimoire/validator.py


def validate_ingredients(ingredients: str) -> str:
    valid_tokens = ("fire", "water", "earth", "air")
    text = ingredients.lower()

    if any(tok in text for tok in valid_tokens):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
