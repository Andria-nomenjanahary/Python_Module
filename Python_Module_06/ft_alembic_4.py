#!/usr/bin/python3
import alchemy
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
try:
    if (alchemy.create_earth()):
        raise AttributeError
except AttributeError as a:
    print(f"AttributeError: {a}. Did you mean: 'create_air'?")
