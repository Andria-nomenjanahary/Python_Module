#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        return

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            check = all(isinstance(x, (int, float)) for x in data)
            return check
        return False

    def ingest(self, data: float | int | list[float | int]) -> None:
        try:
            if not self.validate(data):
                raise ValueError(
                    f"Test invalid ingestion of string '{data}'"
                    " without prior validation:\n"
                    "Got exception: Improper numeric data"
                )
            self.count += 1
            self.storage.append((self.count, str(data)))
        except ValueError as e:
            print(e)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            check = all(isinstance(x, str) for x in data)
            return check
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]] | list[str] | str
    ) -> None:
        try:
            if not self.validate(data):
                raise ValueError(
                    f"Test invalid ingestion of string '{data}'"
                    " without prior validation:\n"
                    "Got exception: Improper numeric data"
                )
            self.count += 1
            self.storage.append((self.count, str(data)))
        except ValueError as e:
            print(e)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: dict[str, str]) -> bool:
            check = isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )
            return check

        if is_valid_dict(data):
            return True
        if isinstance(data, dict):
            verif = all(is_valid_dict(x) for x in data)
            return verif
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        try:
            if not self.validate(data):
                raise ValueError(
                    f"Test invalid ingestion of string '{data}'"
                    " without prior validation:\n"
                    "Got exception: Improper numeric data"
                )
            self.count += 1
            items = data if isinstance(data, list) else [data]

            for item in items:
                level = item.get("log_level", "UNKNOWN")
                msg = item.get("log_message", "")
                formatted_string = f"{level}: {msg}"
                self.storage.append((self.count, formatted_string))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    numericprocessor = NumericProcessor()
    textprocessor = TextProcessor()
    logprocessor = LogProcessor()

    print("Testing Numeric Processor...")
    input_one: int = 42
    input_two: str = "hello"
    input_three: str = "foo"
    input_four: list[int] = [1, 2, 3, 4, 5]
    input_five: list[str] = ["Hello", "Nexus", "World"]
    input_six = {
        "log_level": "NOTICE",
        "log_message": "Connection to server",
    }, {"log_level": "ERROR", "log_message": "Unauthorized access!!"}

    result_one = numericprocessor.validate(input_one)
    print(f"Trying to validate input '{input_one}': {result_one}")

    result_two = numericprocessor.validate(input_two)
    print(f"Trying to validate input '{input_two}': {result_two}")

    numericprocessor.ingest(input_three)

    print(f"Processing data: {input_four}")
    i = 0
    j = 1
    while i in range(len(input_four)):
        numericprocessor.ingest(input_four[i])
        j += 1
        i += 1

    print("Extracting 3 values...")
    i = 0
    while i in range(3):
        print(f"Numeric value {i}: {numericprocessor.output()[1]}")
        i += 1

    print()

    print("Testing Text Processor...")
    result_five = textprocessor.validate(input_one)
    print(f"Trying to validate input '{input_one}': {result_five}")
    print(f"Processing data: {input_five}")
    i = 0
    j = 1
    while i in range(len(input_five)):
        textprocessor.ingest(input_five[i])
        j += 1
        i += 1
    print("Extracting 1 value...")
    i = 0
    while i in range(1):
        print(f"Text value {i}: {textprocessor.output()[1]}")
        i += 1

    print()

    print("Testing Log Processor...")
    result_six = logprocessor.validate(input_one)
    print(f"Trying to validate input '{input_two}': {result_six}")
    print(f"Processing data: {list(input_six)}")
    i = 0
    while i in range(len(input_six)):
        logprocessor.ingest(input_six[i])
        i += 1
    print("Extracting 2 values...")
    i = 0
    while i in range(2):
        index, dico = logprocessor.output()
        print(f"Log entry {i}: {dico}")
        i += 1
