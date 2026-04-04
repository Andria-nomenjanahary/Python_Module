#!/usr/bin/env python3
class Plant:
    class Statistic:
        def __init__(self) -> None:
            self._count_func_show = 0
            self._count_func_age = 0
            self._count_func_grow = 0

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
        self.statistic = Plant.Statistic()

    def grow(self, days: int) -> None:
        self.statistic._count_func_grow += 1
        self._height = days * self.growth_rate

    def age(self, days: int) -> None:
        self.statistic._count_func_age += 1
        self._age += days

    def show(self, check: str | None = None) -> None:
        self.statistic._count_func_show += 1
        if check == "Anonymous":
            print("=== Anonymous")
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def show_statistic(self) -> None:
        print(f"[statistics for {self.name}]")
        print(
            f"Stats: {self.statistic._count_func_grow} grow,"
            f" {self.statistic._count_func_age} age,"
            f" {self.statistic._count_func_show} show"
        )

    @staticmethod
    def check_age(days: int) -> bool:
        return days > 356

    @classmethod
    def anonymous_plant(
        cls,
        name: str = "Unknown name",
        height: float = 0.0,
        age: int = 0,
        growth_rate: float = 0.0,
    ) -> "Plant":
        return cls(name, height, age, growth_rate)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        color: str,
        growth_rate: float,
    ) -> None:
        super().__init__(name, height, ages, growth_rate)
        self.color = color
        self.state = "has not bloom yet"

    def show(self, check: str | None = None) -> None:
        if check == "Flower":
            print("=== Flower")
        elif check == "Seeds":
            print("=== Seed")
        super().show()
        print(f" Color: {self.color}")
        print(f" {self.name} {self.state}")

    def growth_bloom(self, days: int) -> None:
        print("[asking the rose to grow and bloom]")
        self.grow(days)
        super().show()
        print(f" Color: {self.color}")
        self.state = "blooming"
        print(f" {self.name} is {self.state} beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        trunk_diameter: int,
        growth_rate: float,
    ) -> None:
        super().__init__(name, height, ages, growth_rate)
        self.trunk_diameter = trunk_diameter
        self._count_shade = 0

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        self._count_shade += 1
        print(
            f"Tree {self.name} now produces a shade of {self._height:.1f}cm"
            f" long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self, check: str | None = None) -> None:
        print("=== Tree")
        super().show(check)
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def show_statistic(self) -> None:
        super().show_statistic()
        print(f" {self._count_shade} shade")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        color: str,
        seed: int,
        growth_rate: float,
    ) -> None:
        super().__init__(name, height, ages, color, growth_rate)
        self.seeds = 0

    def show(self, check: str | None = None) -> None:
        super().show(check)
        print(f" Seeds: {self.seeds}")

    def grow(self, days: int) -> None:
        self.statistic._count_func_grow += 1
        self._height += days * self.growth_rate

    def grow_age_bloom(self, days: int) -> None:
        print("[make sunflower grow, age and bloom]")
        self.age(20)
        self.grow(20)
        self.seeds = 42
        self.show()


def show_statistic(obj: Plant) -> None:
    obj.show_statistic()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()
    rose = Flower("Rose", 12, 23, "Red", 0.5)
    rose.show("Flower")
    rose.show_statistic()
    rose.growth_bloom(46)
    show_statistic(rose)
    print()
    oak = Tree("Oak", 100, 365, 12, 0.1)
    oak.show()
    oak.show_statistic()
    oak.produce_shade()
    show_statistic(oak)
    print()
    sunflower = Seed("Sunflower", 80, 45, "yellow", 0, 1.5)
    sunflower.show("Seeds")
    sunflower.grow_age_bloom(20)
    show_statistic(sunflower)
    print()
    tulip = Plant.anonymous_plant(height=12, age=2, growth_rate=0.1)
    tulip.show("Anonymous")
    show_statistic(tulip)
