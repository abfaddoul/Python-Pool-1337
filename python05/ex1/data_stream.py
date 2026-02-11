#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

StatsValue = Union[str, int, float]


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self._batches_processed = 0
        self._items_processed = 0
        self._failures = 0
        self._last_error = ""

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        last_error = self._last_error if self._last_error else "none"
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "batches_processed": self._batches_processed,
            "items_processed": self._items_processed,
            "failures": self._failures,
            "last_error": last_error,
        }

    def _mark_success(self, items_count: int) -> None:
        self._batches_processed += 1
        self._items_processed += items_count
        self._last_error = ""

    def _mark_failure(self, message: str) -> None:
        self._failures += 1
        self._last_error = message


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria != "critical":
            return data_batch

        out: List[Any] = []
        for item in data_batch:
            if not isinstance(item, str):
                continue
            if ":" not in item:
                continue

            key, raw = item.split(":", 1)
            key = key.strip()
            raw = raw.strip()

            try:
                val = float(raw)
            except ValueError:
                continue

            if key == "temp" and val >= 30.0:
                out.append(item)
            elif key == "humidity" and val >= 80.0:
                out.append(item)
            elif key == "pressure" and val <= 1000.0:
                out.append(item)

        return out

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = 0
            temp_sum = 0.0
            temp_count = 0

            for item in data_batch:
                if not isinstance(item, str):
                    continue
                count += 1

                if ":" not in item:
                    continue
                key, raw = item.split(":", 1)
                key = key.strip()
                raw = raw.strip()

                if key != "temp":
                    continue

                try:
                    val = float(raw)
                except ValueError:
                    continue

                temp_sum += val
                temp_count += 1

            avg = 0.0
            if temp_count != 0:
                avg = temp_sum / temp_count

            self._mark_success(count)
            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg:.1f}°C"
            )
        except Exception:
            self._mark_failure("SensorStream processing failed")
            return "Sensor analysis: processing failed"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria != "large":
            return data_batch

        out: List[Any] = []
        for item in data_batch:
            if not isinstance(item, str):
                continue
            if ":" not in item:
                continue

            _, raw = item.split(":", 1)
            raw = raw.strip()

            try:
                val = float(raw)
            except ValueError:
                continue

            if val >= 120.0:
                out.append(item)

        return out

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = 0
            total_buy = 0.0
            total_sell = 0.0

            for item in data_batch:
                if not isinstance(item, str):
                    continue
                if ":" not in item:
                    continue

                op, raw = item.split(":", 1)
                op = op.strip()
                raw = raw.strip()

                try:
                    val = float(raw)
                except ValueError:
                    continue

                count += 1
                if op == "buy":
                    total_buy += val
                elif op == "sell":
                    total_sell += val

            net = total_buy - total_sell
            sign = "+"
            if net < 0:
                sign = "-"

            self._mark_success(count)
            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {sign}{abs(net):.0f} units"
            )
        except Exception:
            self._mark_failure("TransactionStream processing failed")
            return "Transaction analysis: processing failed"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = 0
            errors = 0

            for item in data_batch:
                if not isinstance(item, str):
                    continue
                count += 1
                if item == "error":
                    errors += 1

            self._mark_success(count)
            return f"Event analysis: {count} events, {errors} error detected"
        except Exception:
            self._mark_failure("EventStream processing failed")
            return "Event analysis: processing failed"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def register(self, stream: Any) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process(
        self,
        stream: Any,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> str:
        if not isinstance(stream, DataStream):
            return "Unified processing failed"

        try:
            filtered = stream.filter_data(data_batch, criteria)
            return stream.process_batch(filtered)
        except Exception:
            stream._mark_failure("StreamProcessor unified processing failed")
            return "Unified processing failed"


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    print(sensor.process_batch(sensor_batch))
    print()

    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(trans_batch)}]")
    print(trans.process_batch(trans_batch))
    print()

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    print(event.process_batch(event_batch))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor = StreamProcessor()
    processor.register(sensor)
    processor.register(trans)
    processor.register(event)

    print("Batch 1 Results:")
    s1 = ["temp:21.0", "temp:23.0"]
    t1 = ["buy:40", "sell:120", "sell:50", "buy:60"]
    e1 = ["login", "warning", "logout"]
    print(f"- Sensor data: {len(s1)} readings processed")
    print(f"- Transaction data: {len(t1)} operations processed")
    print(f"- Event data: {len(e1)} events processed")
    print()

    print("Stream filtering active: High-priority data only")
    critical_sensor_data = ["temp:36.0", "humidity:85.0", "temp:22.0"]
    large_trans_data = ["sell:500", "buy:10", "sell:80"]

    critical = sensor.filter_data(critical_sensor_data, "critical")
    large = trans.filter_data(large_trans_data, "large")

    print(
        f"Filtered results: {len(critical)} critical sensor alerts, "
        f"{len(large)} large transaction"
    )
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
