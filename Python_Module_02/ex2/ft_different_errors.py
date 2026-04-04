#!/usr/bin/env python3
def test_error_types(operation_number: int) -> None:
    try:
        print(f"Testing operation {operation_number}...")
        garden_operations(operation_number)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as z:
        print(f"Caught ZeroDivisionError: {z}")
    except FileNotFoundError as f:
        print(f"Caught FileNotFoundError: {f}")
    except TypeError as t:
        print(f"Caught TypeError: {t}")


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("zyx")
    elif operation_number == 1:
        798 / 0
    elif operation_number == 2:
        open("Unknown.txt")
    elif operation_number == 3:
        "Bonjour ceci est un text" + 42
    else:
        print("Operation completed successfully\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    for i in [0, 1, 2, 3, 4]:
        test_error_types(i)
    print("All error types tested successfully!")
