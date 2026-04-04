#!/usr/bin/env python3
class SecurePlant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float
    ) -> None:
        self.name = name
        if height >= 0:
            self._height = height
        else:
            print(
                f"{self.name}: Error, height can't be negative\n"
                "Height update rejected"
            )
            self._height = 0
        if age >= 0:
            self._age = age
        else:
            print(
                f"{self.name}: Error, age can't be negative\n"
                "Age update rejected"
            )
            self._age = 0
        self.growth_rate = growth_rate

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(
                f"{self.name}: Error, height can't be negative\n"
                "Height update rejected"
            )

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(
                f"{self.name}: Error, age can't be negative\n"
                "Age update rejected"
            )

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"Plant created: {self.name}: {round(self._height, 1)}cm,"
            f" {self._age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 12, 21, 0.1)
    rose.show()
    print()
    rose.set_height(45)
    rose.set_age(65)
    print()
    rose.set_height(-45)
    rose.set_age(-65)
    print()
    print(
        f"Current state: {rose.name}: {rose.get_height():.1f}cm"
        f", {rose.get_age()} days old"
    )
