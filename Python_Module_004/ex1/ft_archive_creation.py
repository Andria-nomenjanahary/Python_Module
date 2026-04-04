#!/usr/bin/env python3

import sys
from typing import IO


def access_file() -> str | None:
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
        return path
    except FileNotFoundError as f:
        print(f"Error opening file '{path}': {f}")
    except PermissionError as p:
        print(f"Error opening file '{path}': {p}")
    finally:
        if file:
            print(f"\n---\nFile '{path}' closed.\n")
            file.close()
    return None


def transform_file() -> None:
    path = access_file()
    spec_char = "#"
    end_char = "\n"
    if path is not None:
        print("Transform data:")
        print("---\n")
        file_to_modif: IO[str] = open(path, "r")
        content: str = file_to_modif.read()
        lines: list[str] = content.splitlines()
        modif_lines: list[str] = [
            line + spec_char + end_char for line in lines
        ]
        file_to_modif.close()
        for line in modif_lines:
            print(line, end="")
        print("\n---")
    else:
        return

    input_file: str = input("Enter new file name (or empty): ")

    if input_file is not None:
        backup_file: IO[str] | None = None
        try:
            backup_file = open(input_file, "w", encoding="utf-8")
            backup_line: list[str] = [str(line) for line in modif_lines]
            print(f"Saving data to '{input_file}'")
            for new_line in backup_line:
                backup_file.write(str(new_line))
            print(f"Data saved in file '{input_file}'.")
        except PermissionError as p:
            print(f"Error opening file '{path}': {p}")
        except FileNotFoundError:
            print("Not saving data:")
        finally:
            if backup_file:
                backup_file.close()


if __name__ == "__main__":
    print("=== Cyber Archives Recovery  & Preservation===")
    transform_file()
