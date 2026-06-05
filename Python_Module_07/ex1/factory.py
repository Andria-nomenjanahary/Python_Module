from ex0.factory import CreatureFactory
from ex0.creatures import Creatures
from ex1.creatures import Sproutling, Bloomelle, \
    Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Sproutling()

    def create_evolved(self) -> Creatures:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Shiftling()

    def create_evolved(self) -> Creatures:
        return Morphagon()
