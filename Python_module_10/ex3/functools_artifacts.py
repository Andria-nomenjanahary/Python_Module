#! /usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    result = 0
    try:
        if operation == "add":
            result = reduce(add, spells)
        elif operation == "multiply":
            result = reduce(mul, spells)
        elif operation == "max":
            result = reduce(max, spells)
        elif operation == "min":
            result = reduce(min, spells)
        return result
    except Exception as e:
        print(e)
        return result


def base(power: int, element: str, target: str) -> str:
    return f"{element} attack on {target} with a {power}% of power"


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    wind = partial(base_enchantment, 50, "Wind")
    fire = partial(base_enchantment, 50, "Fire")
    water = partial(base_enchantment, 50, "Water")
    return {
            'wind': wind,
            'fire': fire,
            'water': water
        }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base(param: Any) -> str:
        return "Unknown spell type"

    @base.register(str)
    def _(param: str) -> str:
        return f"Enchantment: {param}"

    @base.register(int)
    def _(param: int) -> str:
        return f"Damage spell: {param} damage"

    @base.register(list)
    def _(param: list[Any]) -> str:
        for i in range(len(param)):
            i += 1
        return f"Multi-cast: {i} spells"
    return base


if __name__ == "__main__":
    print("Testing spell reducer...")
    tab = [1, 2, 3, 4, 5]
    addition = spell_reducer(tab, "add")
    multiplication = spell_reducer(tab, "multiply")
    maximum = spell_reducer(tab, "max")
    minimum = spell_reducer(tab, "min")
    unknown = spell_reducer(tab, "unknown")
    print(f"Sum: {addition}")
    print(f"Product: {multiplication}")
    print(f"Max: {maximum}")
    print(f"Min: {minimum}")
    print(f"Unknown: {unknown}")
    print()

    print("Testing partial enchanter")
    spell = partial_enchanter(base)
    print(spell['wind']("house"))
    print(spell['fire']("village"))
    print(spell['water']("dam"))
    print()

    print("Testing memoized fibonacci...")
    fib_0 = memoized_fibonacci(0)
    print(f"Fib(0): {fib_0}")
    fib_1 = memoized_fibonacci(1)
    print(f"Fib(1): {fib_1}")
    fib_10 = memoized_fibonacci(10)
    print(f"Fib(10): {fib_10}")
    fib_15 = memoized_fibonacci(15)
    print(f"Fib(15): {fib_15}")
    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("Abdacadabra"))
    print(dispatcher(["Abdacadabra", "lorem", "Mine"]))
    print(dispatcher({"key": "value"}))
