#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


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
            items = data if isinstance(data, list) else [data]
            for item in items:
                self.count += 1
                self.storage.append((self.count, str(item)))
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
            items = data if isinstance(data, list) else [data]
            for item in items:
                self.count += 1
                self.storage.append((self.count, str(item)))
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
        if isinstance(data, list):
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
            items = data if isinstance(data, list) else [data]
            self.count += len(items)
            for item in items:
                level = item.get("log_level", "UNKNOWN")
                msg = item.get("log_message", "")
                formatted_string = f"{level}: {msg}"
                self.storage.append((self.count, formatted_string))
        except ValueError as e:
            print(e)


class DataStream:
    def __init__(self) -> None:
        self.storage: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.storage.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.storage:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        if not self.storage:
            print("No processor found, no data\n")
            return
        print("== DataStream statistics ==")
        labels: dict[str, str] = {
            "NumericProcessor": "Numeric Processor",
            "TextProcessor": "Text Processor",
            "LogProcessor": "Log Processor",
        }
        for proc in self.storage:
            label = labels.get(type(proc).__name__, type(proc).__name__)
            print(
                f"{label}: total {proc.count} items processed, "
                f"remaining {len(proc.storage)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        pass

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

