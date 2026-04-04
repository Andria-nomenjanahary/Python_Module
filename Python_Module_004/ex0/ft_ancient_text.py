#!/usr/bin/env python3

import sys
from typing import IO


def access_file() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    path = sys.argv[1]
    print(f"Accessing file '{path}'")
    file: IO[str] | None = None
    try:
        file = open(path, "r")
        print("---\n")
        content = file.read()
        print(content)
    except FileNotFoundError as f:
        print(f"Error opening file '{path}': {f}")
    except PermissionError as p:
        print(f"Error opening file '{path}': {p}")
    finally:
        if file:
            print(f"\n---\nFile '{path}' closed")
            file.close()


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    access_file()
