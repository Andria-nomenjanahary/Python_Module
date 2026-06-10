#! /usr/bin/env python3
from typing import Callable, Any, TypedDict


class Vault_type(TypedDict):
    recall: Callable[[str], str]
    store: Callable[[str, Any], None]


def mage_counter() -> Callable[[], int]:
    count = 0

    def count_call() -> int:
        nonlocal count
        count += 1
        return count
    return count_call


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    count = initial_power

    def accumulator(data: int) -> int:
        nonlocal count
        count += data
        return count
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def factory(item_name: str) -> str:
        return enchantment_type + " " + item_name
    return factory


def memory_vault() -> Vault_type:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value
        print(f"Store '{key}' = {value}")

    def recall(key: str) -> str:
        return f"Recall '{key}': {memory.get(key, "Memory not found")}"

    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    merlin_count = mage_counter()
    witch_count = mage_counter()
    print("Testing mage counter...")
    print(f"Merlin's spell count is :{merlin_count()}")
    print(f"Merlin's spell count is :{merlin_count()}")
    print(f"Witch's spell count is: {witch_count()}\n")

    print("Testing spell accumulator...")
    base = 100
    merlin_acc = spell_accumulator(100)
    days = 20
    print(f"Base: {base}, add {days}: {merlin_acc(days)}")
    days = 30
    print(f"Base: {base}, add {days}: {merlin_acc(days)}\n")

    print("Testing enchantment factory...")
    merlin_enchantment = enchantment_factory("Abdacadabra")
    print(merlin_enchantment("solerum"))
    last_enchantment = enchantment_factory("Flaming")
    print(last_enchantment("Sword"))
    witch_enchantment = enchantment_factory("Frozen")
    print(witch_enchantment("Shield"))
    print()

    print("Testing memory vault...")
    box = memory_vault()
    box['store']('secret', 42)
    print(box['recall']('secret'))
    print(box['recall']('unknown'))
