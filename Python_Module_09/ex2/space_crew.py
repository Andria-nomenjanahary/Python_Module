import sys
from datetime import datetime
from enum import Enum

try:
    from pydantic import (
        BaseModel,
        Field,
        StrictInt,
        model_validator,
        ValidationError
    )
except ImportError as e:
    print(f"Error: {e} - To install it, use: pip install pydantic")
    sys.exit(1)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: StrictInt = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: StrictInt = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: StrictInt = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_mission(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        senior_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        has_senior = any(member.rank in senior_ranks for member in self.crew)
        if not has_senior:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% \
        experienced crew (5+ years)"
                )

        for person in self.crew:
            if not person.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")

    def print_log(data: SpaceMission) -> None:
        print("========================================")
        print("Valid mission created:")
        print(f"Name: {data.mission_name}")
        print(f"ID: {data.mission_id}")
        print(f"Destination: {data.destination}")
        print(f"Duration days: {data.duration_days} days")
        print(f"Budget:  ${data.budget_millions}M")
        print(f"Crew size: {len(data.crew)}")
        print("Crew members:")
        for member in data.crew:
            print(
                f"- {member.name} ({member.rank.value}) - "
                f"{member.specialization}"
            )
        print("\n========================================")

    try:
        mission_1 = SpaceMission(
            mission_id="MSN-001",
            mission_name="Artemis Deep Horizon",
            destination="Mars",
            launch_date=datetime(2027, 6, 15, 9, 0, 0),
            duration_days=520,
            budget_millions=4500.0,
            mission_status="planned",
            crew=[
                CrewMember(
                    member_id="CM-001",
                    name="Elena Vasquez",
                    rank=Rank.CAPTAIN,
                    age=42,
                    specialization="Aerospace Engineering",
                    years_experience=18,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM-002",
                    name="James Okafor",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Astrobiology",
                    years_experience=10,
                    is_active=True
                ),
            ]
        )
        print_log(mission_1)

        mission_2 = SpaceMission(
            mission_id="MSN-002",
            mission_name="Lunar Base Alpha",
            destination="Moon",
            launch_date=datetime(2026, 11, 3, 14, 30, 0),
            duration_days=90,
            budget_millions=850.5,
            mission_status="planned",
            crew=[
                CrewMember(
                    member_id="CM-010",
                    name="Yuki Tanaka",
                    rank=Rank.LIEUTENANT,
                    age=50,
                    specialization="Systems Navigation",
                    years_experience=25,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM-011",
                    name="Luca Ferretti",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Geology",
                    years_experience=2,
                    is_active=True
                ),
            ]
        )
        print_log(mission_2)

    except ValidationError as e:
        message = e.errors()[0].get("msg", "")
        if message.startswith("Value error, "):
            message = message[len("Value error, "):]
        print(f"Expected validation error:\n{message}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
