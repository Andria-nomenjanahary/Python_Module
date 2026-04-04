#!/usr/bin/env python3
import math


def get_input(prompt: str) -> tuple[float, float, float] | None:
    user_input: str = input(prompt)

    if user_input.count(",") != 2:
        print("Invalid syntax")
        return None

    segments: list[str] = user_input.split(",")
    float_numbers: tuple[float, ...] = ()

    for segment in segments:
        cleaned: str = segment.strip()
        try:
            float_numbers += (float(cleaned),)
        except ValueError as e:
            print(f"Error on parameter '{cleaned}': {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    if len(float_numbers) == 3:
        return (float_numbers[0], float_numbers[1], float_numbers[2])

    print("Invalid syntax")
    return None


def position(label: str) -> tuple[float, float, float]:
    if label == "first" or label == "second":
        print(f"Get a {label} set of coordinates")
    coords = get_input("Enter new coordinates as floats in format 'x,y,z': ")
    if coords is None:
        return position(label)

    if label == "first":
        print(f"Got a first tuple: {coords}")
        print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
        dist_to_center = math.sqrt(
            (coords[0]) ** 2 + (coords[1] ** 2) + (coords[2] ** 2)
        )
        print(f"Distance to center: {round(dist_to_center, 4)}")
    return coords


def get_player_pos() -> None:
    first_set = position("first")
    second_set = position("second")
    dist_to_center = math.sqrt(
        (second_set[0] - first_set[0]) ** 2
        + (second_set[1] - first_set[1]) ** 2
        + (second_set[2] - first_set[2]) ** 2
    )
    print(
        "Distance between the 2 sets of coordinates:"
        f" {round(dist_to_center, 4)}"
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    get_player_pos()
