#! /usr/bin/env python3
from functools import wraps
from typing import Callable, Any
import time


def spell_timer(
        func: Callable[[Any, Any], Any]
        ) -> Callable[[Any], Any]:
    @wraps(func)
    def timer(*args, **kwargs):
        print(f"Casting {func.__name__}")
        start= time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return timer

    
def power_validator(min_power: int) -> Callable[[Any], Any]:
    def decorator(
            func: Callable[[Any], Any]
            ) -> Callable[[Any], Any]:
        @wraps(func)
        def validator(*args, **kwargs) -> Callable[[Any], Any] :
            power = kwargs.get('power') if 'power' in kwargs \
    else (args[2] if len(args) > 2 else None)
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return validator
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Any], Any]:
    def decorator(
            func: Callable[[Any], Any]
            ) -> Callable[[Any], Any]:
        @wraps(func)
        def retry(*args, **kwargs) -> str:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(
                        f"Spell failed, retrying... (attempt {i}/"
                        f"{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return retry
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name}\
 with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    @spell_timer
    def merlin_spell(spell: Any):
        return f"{spell} cast!"

    print(f"Result: {merlin_spell("Fireball")}\n")

    print("Testing power validator...")
    @power_validator(min_power=5)
    def test(value: int) -> str:
        return f"OK"

    print(f"Result: {test(4)}\n")

    print("Testing retrying spell...")
    @retry_spell(max_attempts=8)
    def test(n: int) -> str:
        if n <= 5:
            raise Exception()
        return "Waaaaaaagh spelled !"

    print(test(1))
    print(test(6))

    
    print("\nTesting MageGuild...")
    groups = MageGuild()

    print(groups.validate_mage_name("yvon"))
    print(groups.validate_mage_name("yv"))
    print(groups.cast_spell("yvon", power=15))
