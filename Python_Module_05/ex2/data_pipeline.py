#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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
            for item in items:
                self.count += 1
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
        for proc in self.storage:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    collected.append(proc.output())
                except IndexError:
                    break
            if collected:
                plugin.process_output(collected)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for id, value in data]
        print("CSV Output:\n" + ",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        entries = [f'"item_{id}": "{value}"' for id, value in data]
        print("{" + ", ".join(entries) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    info: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {'log_level': 'INFO', 'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]

    another_info: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            },
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]

    data = DataStream()

    print("Initialize Data Stream...")

    data.print_processors_stats()

    print("Registering Processors")
    data.register_processor(NumericProcessor())
    data.register_processor(TextProcessor())
    data.register_processor(LogProcessor())

    print(f"Send first batch of data on stream: {info}\n")
    data.process_stream(info)

    data.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    data.output_pipeline(3, CSVExportPlugin())
    print()
    data.print_processors_stats()
    print()

    print(f"Send another batch of data: {another_info}\n")
    data.process_stream(another_info)
    data.print_processors_stats()
    print()

    print("Send 5 processed data from each processor to a JSON plugin:")
    data.output_pipeline(5, JSONExportPlugin())
    print()
    data.print_processors_stats()
