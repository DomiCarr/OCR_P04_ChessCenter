""" models/player.py """

from datetime import datetime, date


class Player:
    def __init__(self, national_id: str,
                 first_name: str,
                 last_name: str,
                 birth_date: date | None):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def to_dict(self) -> dict:
        """Convert object to dictionary for JSON saving."""
        return {
            "national_id": self.national_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat()
            if self.birth_date else None
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild object from a JSON dictionary."""

        birth_date_json = data.get("birth_date")
        birth_date_obj = (
            datetime.fromisoformat(birth_date_json).date()
            if birth_date_json else None
        )

        return cls(
            national_id=data.get("national_id", ""),
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            birth_date=birth_date_obj
        )
