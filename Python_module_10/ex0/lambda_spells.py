#! /usr/bin/env python3
from typing import Any


def artifact_sorter(
        artifacts: list[dict[str, Any]]
        ) -> list[dict[str, Any]]:
    try:
        sorted_list = sorted(
            artifacts,
            key=lambda artifact: artifact['power'],
            reverse=True)
    except Exception as e:
        sorted_list = []
        print(e)
    return sorted_list


def power_filter(
        mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    try:
        filtered = list(filter(
            lambda power: power['power'] >= min_power,
            mages))
    except Exception as e:
        print(e)
        filtered = []
    return filtered


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        transformed = list(map(
            lambda spell: f"* {spell} *", spells))
    except Exception as e:
        print(e)
        transformed = []
    return transformed


def mage_stats(
        mages: list[dict[str, Any]]
        ) -> dict[str, Any]:
    try:
        powers = list(map(lambda mage: mage['power'], mages))
        max_power = max(powers)
        min_power = min(powers)
        average = round(sum(powers) / len(mages), 2)
        dict = {
            'max_power': max_power,
            'min_power': min_power,
            'average': average
        }
    except Exception as e:
        print(e)
        dict = {}

    return dict


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Crystall Orb", "power": 85},
        {"name": "Fire Staff", "power": 92}
    ]
    try:
        sorted_artifact = artifact_sorter(artifacts)
        print(
            f"{sorted_artifact[0].get('name')}"
            f" ({sorted_artifact[0].get('power')})"
            f" comes before {sorted_artifact[1].get('name')}"
            f" ({sorted_artifact[1].get('power')})"
            )
    except Exception as e:
        print(f"No parameter to compare...Error: {e}")

    spells = [
        "Abdacadabra",
        "Lorem",
        "Snobedeck",
        ]

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    for i in transformed:
        print(i, end=" ")
    print()
