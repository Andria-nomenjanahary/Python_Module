#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def plantcheck(name: str) -> None:
    wilting_plant = ["Tomato", "Strawberry"]
    if name in wilting_plant:
        raise PlantError(f"The {name} is wilting!")


def watercheck(volume: int) -> None:
    if volume < 2:
        raise WaterError("Not enough water in the tank!")


def check_garden(name: str, volume: int) -> None:
    print("Testing catching all garden errors...")
    if volume and name:
        try:
            plantcheck(name)
        except GardenError as e:
            print(f"Caught GardenError: {e}")

        try:
            watercheck(volume)
        except GardenError as e:
            print(f"Caught GardenError: {e}\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    name = "Tomato"
    volume = 1
    try:
        print("Testing PlantError...")
        plantcheck(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        watercheck(volume)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    check_garden(name, volume)
    print("All custom error types work correctly!")
