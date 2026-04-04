#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    number: int = int(temp_str)
    if number < 0:
        raise ValueError(f"{number}°C is too cold for plants (min 0°C)")
    elif number > 40:
        raise ValueError(f"{number}°C is too hot for plants (max 40°C)")
    else:
        return number


def test_temperature(temp_str: str) -> None:
    try:
        new_temp: int = input_temperature(temp_str)
        print(f"Temperature is now {new_temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    tempature = "10"
    test_temperature(tempature)
    tempature = "2abc5"
    test_temperature(tempature)
    tempature = "-50"
    test_temperature(tempature)
    tempature = "150"
    test_temperature(tempature)
    print("All tests completed - program didn't crash!")
