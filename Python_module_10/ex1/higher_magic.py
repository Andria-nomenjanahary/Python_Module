#! /usr/bin/env python3
from typing import Callable


def attack(target: str, power: int) -> str:
    return f"Attack destroys {target} with a {power}% of power!"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def is_rainny(target: str, power: str) -> bool:
    return power == "rainny" and target == "village"


def spell_weather(target: str, power: str) -> str:
    return f"Spell weather touches {target} with a {power} day!"


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    def combine(target: str, power: int) -> tuple[str, str]:
        fact1 = spell1(target, power)
        fact2 = spell2(target, power)
        return [fact1, fact2]
    return combine


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
        ) -> Callable[[str, int], str]:
    def amplified_spell(
            target: str,
            power: int
            ) -> str:
        result = power * multiplier
        return base_spell(target, result)
    return amplified_spell


def conditional_caster(
        condition: Callable[[str, str], bool],
        spell: Callable[[str, str], str]
        ) -> Callable[[str, str], str]:
    def check(
            target: str,
            power: str
            ) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return check


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    return lambda target, power: [s(target, power) for s in spells]


if __name__ == "__main__":
    report_0 = spell_combiner(attack, heal)
    print("\nTesting spell combiner...")
    lists_0 = report_0("house", 40)
    print(f"Combined spell result: {lists_0[0]}, {lists_0[1]}\n")

    report_1 = power_amplifier(attack, 4)
    print(f"{report_1("village", 40)}\n")

    report_2 = conditional_caster(is_rainny, spell_weather)
    print(f"{report_2("village", "rainny")}\n")

    print("Testing list of spells")
    report_3 = spell_sequence([attack, heal])
    lists = report_3("landscape", 2)
    for r in lists:
        print(f"- {r}")
