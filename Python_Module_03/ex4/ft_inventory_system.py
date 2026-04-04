#!/usr/bin/env python3
import sys


def arg_parsing() -> dict[str, int]:
    dictionary: dict[str, int] = {}

    for arg in sys.argv[1:]:
        try:
            if arg.count(":") != 1:
                raise Exception(f"Error - invalid parameter '{arg}'")

            parts: list[str] = arg.split(":")
            key: str = parts[0]
            string_value: str = parts[1]

            has_digit: bool = False
            for char in key:
                if char.isdigit():
                    has_digit = True
                    break

            if has_digit or not key:
                raise Exception(f"Error - invalid parameter '{key}'")

            if key in dictionary:
                raise Exception(f"Redundant item {key} - discarding")

            value: int = int(string_value)
            dictionary[key] = value

        except ValueError as p:
            print(f"Quantity error for '{key}': {p}")
        except Exception as e:
            print(e)
    return dictionary


def show_dict() -> None:
    try:
        dictio = arg_parsing()
        print(f"Got inventory: {dictio}")
        items = list(dictio.keys())
        print(f"Item list: {items}")
        total_quantity = sum(list(dictio.values()))
        print(f"Total quantity of the {len(items)} items: {total_quantity}")
        for key in dictio:
            quantity: int = dictio[key]
            percentage = (quantity / total_quantity) * 100
            print(f"Item {key} represents {round(percentage, 1)}%")
        most_key: str = ""
        least_key: str = ""
        first_key = True
        for key in dictio:
            if first_key:
                most_key = key
                least_key = key
                first_key = False
                continue
            if dictio[key] > dictio[most_key]:
                most_key = key
            if dictio[key] < dictio[least_key]:
                least_key = key
        print(
            f"Item most abundant: {most_key} with quantity {dictio[most_key]}"
        )
        print(
            f"Item least abundant: {least_key} "
            f"with quantity {dictio[least_key]}"
        )
        dictio.update({"magic_item": 1})
        print(f"Updated inventory: {dictio}")
    except KeyError as e:
        print(f"Caught error as dictionary is void, the key is void:{e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    show_dict()
