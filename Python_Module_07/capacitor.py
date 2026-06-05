#! /usr/bin/python3
from ex1.factory import HealingCreatureFactory, \
        TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def create(factory: HealingCreatureFactory | TransformCreatureFactory) -> None:

    print(" base:")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    if isinstance(base_creature, HealCapability):
        print(base_creature.heal())
    if isinstance(base_creature, TransformCapability):
        print(base_creature.transform())
        print(base_creature.attack())
        print(base_creature.revert())

    print(" evolved:")
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    if isinstance(evolved_creature, HealCapability):
        print(evolved_creature.heal())
    if isinstance(evolved_creature, TransformCapability):
        print(evolved_creature.transform())
        print(evolved_creature.attack())
        print(evolved_creature.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    healing_creature = HealingCreatureFactory()
    create(healing_creature)
    print()

    print("Testing Creature with transform capability")
    transform_creature = TransformCreatureFactory()
    create(transform_creature)
