#!/usr/bin/env python3
class Plant:
    def __init__(
        self, name: str, height: float, ages: int, growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.ages = ages
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.ages} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Rose = Plant("Rose", 25, 30, 0.6)
    print("Created: ", end="")
    Rose.show()
    Oak = Plant("Oak", 200, 365, 0.1)
    print("Created: ", end="")
    Oak.show()
    Cactus = Plant("Cactus", 5, 90, 0.1)
    print("Created: ", end="")
    Cactus.show()
    Sunflower = Plant("Sunflower", 80, 45, 0.8)
    print("Created: ", end="")
    Sunflower.show()
    Fern = Plant("Fern", 15, 120, 0.3)
    print("Created: ", end="")
    Fern.show()
