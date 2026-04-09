#!/usr/bin/env python3

import sys
import typing


def access_file() -> str | None:
    if len(sys.argv) < 2:
        sys.stderr.write("[STDERR] Usage: ft_ancient_text.py <file>\n")
        sys.exit(1)
    path = sys.argv[1]
    print(f"Accessing file '{path}'")
    file: typing.IO[str] | None = None
    try:
        file = open(path, "r")
        print("---\n")
        content = file.read()
        print(content)
        return path
    except FileNotFoundError as e:
        sys.stderr.write(f"Error opening file '{path}': {e}")
    except PermissionError as e:
        sys.stderr.write(f"Error opening file '{path}': {e}")
    finally:
        if file:
            file.close()
            print(f"\n---\nFile '{path}' closed.\n")
    return None


def transform_file() -> None:
    path = access_file()
    spec_char = "#"
    end_char = "\n"
    if path is not None:
        print("Transform data:")
        print("---\n")
        file_to_modif: typing.IO[str] = open(path, "r")
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

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    input_file: str = sys.stdin.readline().strip()

    if input_file is not None:
        backup_file: typing.IO[str] | None = None
        try:
            backup_file = open(input_file, "w", encoding="utf-8")
            backup_line: list[str] = [str(line) for line in modif_lines]
            print(f"Saving data to '{input_file}'")
            for new_line in backup_line:
                backup_file.write(str(new_line))
            print(f"Data saved in file '{input_file}'.")
        except PermissionError as p:
            sys.stderr.write(f"[STDERR] Error opening file '{path}': {p}")
        except FileNotFoundError:
            sys.stdout.write("Not saving data:")
        finally:
            if backup_file:
                backup_file.close()


if __name__ == "__main__":
    print("=== Cyber Archives Recovery  & Preservation ===")
    transform_file()
