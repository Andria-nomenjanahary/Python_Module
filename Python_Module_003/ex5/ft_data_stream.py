#!/usr/bin/env python3
import random
from typing import Generator


def gen_event(
    players: list[str], actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    while True:
        selected_player = random.choice(players)
        selected_action = random.choice(actions)
        yield (selected_player, selected_action)


def consume_event(
    backup: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while backup:
        selected_item: tuple[str, str] = random.choice(backup)
        remaining_items: list[tuple[str, str]] = []
        for item in backup:
            if item is not selected_item:
                remaining_items += [item]
        backup[:] = remaining_items
        yield selected_item


if __name__ == "__main__":
    player_list: list[str] = ["Alice", "Bob", "Dylan", "Charlie"]
    action_list: list[str] = [
        "swim",
        "climb",
        "run",
        "sleep",
        "eat",
        "grab",
        "move",
        "release",
    ]
    event_gen = gen_event(player_list, action_list)
    for i in range(1000):
        result: tuple[str, str] = next(event_gen)
        print(f"Event {i}: Player {result[0]} did action {result[1]}")
    backup: list[tuple[str, str]] = []
    for _ in range(11):
        new_event: tuple[str, str] = next(event_gen)
        backup = backup + [new_event]
    print(f"Built list of 11 events: {backup}")
    consumer = consume_event(backup)
    for event in consumer:
        print(f"Got even from list: {event}")
        print(f"Remains in list: {backup}")
