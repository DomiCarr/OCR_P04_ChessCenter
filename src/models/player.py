"""models/player.py"""


class Player:
    def __init__(self, national_id, first_name, last_name, birth_date):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def to_dict(self) -> dict:
        """Convert player object to dictionary for JSON saving."""
        return {
            "national_id": self.national_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date
        }

