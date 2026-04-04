#!/usr/bin/env python3
class Plant:
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

    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


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

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        super().show()
        print(f" Color: {self.color}")
        self.state = "blooming"
        print(f" {self.name} is {self.state} beautifully!\n")

    def show(self) -> None:
        print("=== Flower")
        super().show()
        print(f" Color: {self.color}")
        print(f" {self.name} {self.state}")


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

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self._height:.1f}cm"
            f" long and {self.trunk_diameter:.1f}cm wide.\n"
        )

    def show(self) -> None:
        print("=== Tree")
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        harvest_season: str,
        nutritional_value: str,
        growth_rate: float,
    ) -> None:
        super().__init__(name, height, ages, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        print("=== Vegetable")
        super().show()
        print(f"Harvets season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def growth(self, days: int) -> None:
        self._age += days
        self._height = days * self.growth_rate
        self.nutritional_value += days
        print(f"[make {self.name} grow and age for {days} days]")
        super().show()
        print(f" Harvets season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "Red", 0.6)
    rose.show()
    rose.bloom()

    oak = Tree("Oak", 78, 33, 20, 0.3)
    oak.show()
    oak.produce_shade()

    carrot = Vegetable("Carrot", 5, 10, "April", "vitamin A", 2.35)
    carrot.show()
    carrot.growth(20)
