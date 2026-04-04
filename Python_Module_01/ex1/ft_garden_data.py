#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    cactus = Plant("Cactus", 80, 45)
    sunflower = Plant("Sunflower", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    cactus.show()
    sunflower.show()
