#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            user_input: str = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
            parts: list[str] = user_input.split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue

            x, y, z = (float(p.strip()) for p in parts)
            return x, y, z

        except ValueError as e:
            err_msg = str(e).split(":")[-1].strip()
            print(f"Error on parameter {err_msg}: {e}")
            continue


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: {(x1, y1, z1)}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    dist_to_center: float = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("\nGet a second set of coordinates")
    x2, y2, z2 = get_player_pos()

    dist_between: float = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )

    print(
        f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
