import sys
from typing import Optional
from datetime import datetime
from enum import Enum


try:
    from pydantic import (
        BaseModel,
        Field,
        StrictInt,
        model_validator,
        ValidationError)
except ImportError as e:
    print(f"Error: {e} - To install it, use: pip install pydantic")
    sys.exit(1)


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: StrictInt = Field(ge=1, le=1440)
    witness_count: StrictInt = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                'Contact ID must start with "AC" (Alien Contact)')

        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError("Physical contact must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include \
            received messages")

        return self


def main() -> None:
    print("Alien Contact Log Validation")

    def print_log(data: AlienContact) -> None:
        contact_type = data.contact_type.value
        print("========================================")
        print("Valid contact report:")
        print(f"ID: {data.contact_id}")
        print(f"Type: {contact_type}")
        print(f"Location: {data.location}")
        print(f"Signal: {data.signal_strength}/10")
        print(f"Duration: {data.duration_minutes} minutes")
        print(f"Witnesses: {data.witness_count}")
        print(f"Message: '{data.message_received}'")
        print("\n========================================")
    try:
        first_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 5, 29, 14, 30, 00),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.9,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print_log(first_contact)

        second_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2026, 3, 2, 14, 30, 00),
            location="Madagascar",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.9,
            duration_minutes=5,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
        print_log(second_contact)

    except ValidationError as e:
        message = e.errors()[0].get("msg", "")
        if message.startswith("Value error, "):
            message = message[len("Value error, "):]
        print(f"Expected validation error:\n{message}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
