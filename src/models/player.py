"""models/player.py"""

from datetime import datetime, date


class Player:
    def __init__(self, national_id: str,
                 first_name: str,
                 last_name: str,
                 birth_date: date | None,
                 elo: int = 1200):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.elo = int(elo)

    def to_dict(self) -> dict:
        """Convert player object to dictionary for JSON saving."""
        return {
            "national_id": self.national_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat()
            if self.birth_date else None,
            "elo": int(self.elo)
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild a Player object from a JSON dictionary."""

        birth_date_json = data.get("birth_date")
        birth_date_obj = (
            datetime.fromisoformat(birth_date_json).date()
            if birth_date_json else None
        )
        elo_value = data.get("elo", 1200)

        return cls(
            national_id=data.get("national_id", ""),
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            birth_date=birth_date_obj,
            elo=int(elo_value)
        )
