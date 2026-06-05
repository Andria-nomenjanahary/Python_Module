from abc import ABC, abstractmethod


class Creatures(ABC):
    def __init__(self, name: str, typeof: str) -> None:
        self.name = name
        self.typeof = typeof

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.typeof} type Creature"


class Flameling(Creatures):
    def attack(self) -> str:
        return f"{self.name} uses Umber!"


class Pyrodon(Creatures):
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creatures):
    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creatures):
    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
