#! /usr/bin/python3
from ex0 import AquaFactory, FlameFactory
from ex0.factory import CreatureFactory


def create(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    base_creature1 = factory1.create_base()
    base_creature2 = factory2.create_base()
    print(base_creature1.describe())
    print(" vs.")
    print(base_creature2.describe())
    print(" fight! ")
    print(base_creature1.attack())
    print(base_creature2.attack())


if __name__ == "__main__":
    flame_creature = FlameFactory()
    aqua_creature = AquaFactory()
    print("Testing factory")
    create(flame_creature)
    print()
    print("Testing factory")
    create(aqua_creature)
    print()
    print("Testing battle")
    fight(flame_creature, aqua_creature)
