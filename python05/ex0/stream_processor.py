#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    Abstract base class that defines a common interface
    for all data processors.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Data processor specialized for numeric data.
    """

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return all(isinstance(value, (int, float)) for value in data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")

        total = sum(data)
        average = total / len(data)

        result = (
            f"Processed {len(data)} numeric values, "
            f"sum={total}, avg={average}"
        )
        return self.format_output(result)


class TextProcessor(DataProcessor):
    """
    Data processor specialized for text data.
    """

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")

        char_count = len(data)
        word_count = len(data.split())

        result = (
            f"Processed text: {char_count} characters, "
            f"{word_count} words"
        )
        return self.format_output(result)


class LogProcessor(DataProcessor):
    """
    Data processor specialized for log entries.
    """

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return any(level in data for level in ("INFO", "WARNING", "ERROR"))

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")

        if "ERROR" in data:
            level = "ERROR"
        elif "WARNING" in data:
            level = "WARNING"
        else:
            level = "INFO"

        message = data.split(":", 1)[-1].strip()

        result = f"[ALERT] {level} level detected: {message}"
        return self.format_output(result)


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors = [
        ("Numeric", NumericProcessor(), [1, 2, 3, 4, 5]),
        ("Text", TextProcessor(), "Hello Nexus World"),
        ("Log", LogProcessor(), "ERROR: Connection timeout"),
    ]

    for name, processor, data in processors:
        print(f"Initializing {name} Processor...")
        print(f"Processing data: {data!r}")

        if processor.validate(data):
            print(f"Validation: {name} data verified")

        print(processor.process(data))
        print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    demo = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello Nexus"),
        (LogProcessor(), "INFO: System ready"),
    ]

    i = 0

    while i < len(demo):
        processor, data = demo[i]
        result = processor.process(data)
        result = result[8:]
        print(f"Result {i + 1}: {result}")
        i += 1
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
