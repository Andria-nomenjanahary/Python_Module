#!/usr/bin/env python3
class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    capitalized = plant_name.capitalize()
    if plant_name != capitalized or (plant_name >= "0" and plant_name <= "9"):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name.capitalize()}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except (PlantError, AttributeError) as e:
        print(f"Caught PlantError: {e}")
        print(".. ending test and returning to main")
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    array = ["Strawberry", "Lettuce", "Avocat", "Rose", "Tulip"]
    test_watering_system(array)

    print("Testing invalid plants...")
    array1 = ["Strawberry", "lettuce", "Avocat", "Rose", "Tulip"]
    test_watering_system(array1)
    print("Cleanup always happens, even with errors!")
