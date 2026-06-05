from abc import ABC, abstractmethod
from .creatures import Creatures, Flameling, Aquabub, Torragon, Pyrodon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creatures:
        ...

    @abstractmethod
    def create_evolved(self) -> Creatures:
        ...


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creatures:
        return Torragon("Torragon", "Water")


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creatures:
        return Pyrodon("Pyrodon", "Fire/flying")
