from . import dark_validator


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frog", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    check = dark_validator.validate_ingredients(ingredients)
    if "VALID" in check:
        return (f"Spell recorded: {spell_name}: ({check})")
    return (f"Spell rejected: {spell_name}: ({check})")
