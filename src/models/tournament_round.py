from datetime import datetime
from models.match import Match


class TournamentRound:

    def __init__(self,
                 name,
                 start_datetime,
                 end_datetime,
                 matches_list):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches_list = matches_list or []

    def to_dict(self):
        matches_list_dict = []
        if self.matches_list:
            for match in self.matches_list:
                matches_list_dict.append(match.to_dict())

        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat()
            if self.start_datetime else None,
            "end_datetime": self.end_datetime.isoformat()
            if self.end_datetime else None,
            "matches_list": matches_list_dict
        }

    @classmethod
    def from_dict(cls, data: dict):
        """rebuild TournamentRound object from a JSON dictionary"""
        round_name = data.get("name", "")

        # Convert JSON ISO 8601 strings into datetime objects
        round_start_datetime = (datetime.fromisoformat(data["start_datetime"])
                                if data.get("start_datetime") else None)
        round_end_datetime = (datetime.fromisoformat(data["end_datetime"])
                              if data.get("end_datetime") else None)

        # Rebuild matches
        round_matches_list = []
        for match_data in data.get("matches_list", []):
            round_matches_list.append(Match.from_dict(match_data))

        return cls(
            name=round_name,
            start_datetime=round_start_datetime,
            end_datetime=round_end_datetime,
            matches_list=round_matches_list
        )
