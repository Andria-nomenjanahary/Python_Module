#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, ages: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.ages = ages
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.ages += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.ages} days old")

    def growth(self, days: int) -> None:
        init_height = self.height
        for i in range(1, days + 1):
            print(f"=== Days {i} ===")
            if i > 1:
                self.grow()
                self.age()
            self.show()
        growth = self.height - init_height
        print(f"Growth this week {round(growth)}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30, 0.8)
    rose.growth(7)
