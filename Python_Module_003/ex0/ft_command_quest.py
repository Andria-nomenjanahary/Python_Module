#!/usr/bin/env python3
import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    i = 1
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print("Total arguments: 1")
        return
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
    while i < len(sys.argv):
        print(f"Argumant {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
