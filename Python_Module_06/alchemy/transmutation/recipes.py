from ..elements import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    air = create_air()
    potion = strength_potion()
    fire = create_fire()
    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{air}' and '{potion}' mixed with '{fire}'"
    )
