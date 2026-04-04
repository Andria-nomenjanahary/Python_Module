#!/usr/bin/env python3
import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    init_player_list: list[str] = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam',
    ]
    print(f"Initial list of players: {init_player_list}\n")

    cap_player_list = [item.capitalize() for item in init_player_list]
    print(f"New list with all names capitalized: {cap_player_list}\n")

    cap_only_player_list: list[str] = [
        item for item in init_player_list if item == item.capitalize()
    ]
    print(f"New list of capitalized names only: {cap_only_player_list}\n")

    dictionary: dict[str, int] = {
        name: random.randint(1, 1000) for name in cap_player_list
    }
    print(f"Score dict: {dictionary}\n")

    score_average = sum(dictionary.values()) / len(dictionary.values())
    print(f"Score average is {round(score_average, 2)}\n")

    high_scores: dict[str, int] = {
        player: dictionary[player]
        for player in dictionary
        if dictionary[player] > score_average
    }
    print(f"High scores: {high_scores}")
