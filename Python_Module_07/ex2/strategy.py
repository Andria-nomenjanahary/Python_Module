from abc import ABC, abstractmethod
from ex0.creatures import Creatures
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creatures) -> str:
        ...

    @abstractmethod
    def is_valid(self, creature: Creatures) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creatures) -> bool:
        return True

    def act(self, creature: Creatures) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f" Invalid Creature '{creature.name}'"
                " for this normal strategy"
            )
        return f"{creature.attack()}"


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creatures) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creatures) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        assert isinstance(creature, TransformCapability)
        return f"{creature.transform()}\n{creature.attack()}\n\
{creature.revert()}"


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creatures) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creatures) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy"
            )
        assert isinstance(creature, HealCapability)
        return f"{creature.attack()}\n{creature.heal()}"
