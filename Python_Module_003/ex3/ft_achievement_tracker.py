#!/usr/bin/env python3
import random


class Player:
    def __init__(self, name: str, achievement: set[str]) -> None:
        self.name = name
        self.achievement = achievement

    def show_player(self) -> None:
        print(f"Player {self.name}: {self.achievement}")


def gen_player_achievements(achievement_list: list[str]) -> set[str]:
    num_to_assign = random.randint(1, len(achievements_list))
    selected_achievements = random.sample(achievements_list, num_to_assign)
    return set(selected_achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    achievements_list: list[str] = [
        "Master Explorer",
        "Strategist",
        "Untouchable",
        "Unstoppable",
        "Survivor",
        "Speed Runner",
        "Treasure Hunter",
        "World Savior",
        "Collector Supreme",
        "Boss Slayer",
        "Sharp mind",
        "Crafting Genius",
        "First Steps",
    ]
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players: list[Player] = []
    for n in names:
        achievements = gen_player_achievements(achievements_list)
        players = players + [Player(n, achievements)]
    for p in players:
        p.show_player()
    print(f"\nAll distinct achievements: {set(achievements_list)}\n")
    if players:
        common: set[str] = set(players[0].achievement)
        for p in players[1:]:
            common = common.intersection(p.achievement)
        print(f"Common achievements: {common}\n")

    for p in players:
        others: set[str] = set()
        for other in players:
            if other is not p:
                others = others.union(other.achievement)
        unique: set[str] = p.achievement - others
        print(f"Only {p.name} has: {unique}")
