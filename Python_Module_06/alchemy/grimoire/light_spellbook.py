from . import light_validator


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    check = light_validator.validate_ingredients(ingredients)
    if "VALID" in check:
        return (f"Spell recorded: {spell_name}: ({check})")
    return (f"Spell rejected: {spell_name}: ({check})")
