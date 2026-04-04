#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        number = input_temperature(temp_str)
        print(f"Temperature is now {number}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    tempature = "-10"
    test_temperature(tempature)
    tempature = "2abc5"
    test_temperature(tempature)
    print("All tests completed - program didn't crash!")
