import sys
from typing import Optional
from datetime import datetime

try:
    from pydantic import (
        BaseModel,
        Field,
        StrictInt,
        ValidationError
    )
except ImportError as e:
    print(f"Error: {e} - To install it, use: pip install pydantic")
    sys.exit(1)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: StrictInt = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")

    def print_station(data: SpaceStation) -> None:
        if data.is_operational:
            status = "Operational"
        else:
            status = "Not operational"
        print("========================================")
        print("Valid station created:")
        print(f"ID: {data.station_id}")
        print(f"Name: {data.name}")
        print(f"Crew: {data.crew_size} people")
        print(f"Power: {data.power_level}%")
        print(f"Oxygen: {data.oxygen_level}%")
        print(f"Status: {status}\n")
        print("========================================")

    try:
        iss = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 5, 29, 14, 30, 00),
            is_operational=True,
            notes="Dangerous station!There are aliens, be careful..."
        )
        print_station(iss)
        big_beer = SpaceStation(
            station_id="ISS002",
            name="big_beer",
            crew_size=21,
            power_level=52.24,
            oxygen_level=42.45,
            last_maintenance=datetime(2026, 5, 29, 14, 30, 00),
            is_operational=True,
            notes="Some paradisiac planets in this galatic location."
        )
        print_station(big_beer)
    except ValidationError as e:
        message = e.errors()[0].get("msg", "")
        if message.startswith("Value error, "):
            message = message[len("Value error, "):]
        print(f"Expected validation error:\n{message}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
