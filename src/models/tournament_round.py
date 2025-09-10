""" models/tournament_round.py """

from datetime import datetime
from models.match import Match
from typing import List


class TournamentRound:

    def __init__(self,
                 name,
                 start_datetime,
                 end_datetime,
                 matches_list: List[Match]):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches_list = matches_list or []

    def to_dict(self):
        """Convert object to dictionary for JSON saving."""
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
        """rebuild object from a JSON dictionary"""
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

    def update_match_results(self, match_result: tuple[str, float, str, float]):
        """Update scores for a single match identified by players' national IDs."""
        nid1, score1, nid2, score2 = match_result
        for match in self.matches_list:
            nids = [match.player_1.national_id]
            if match.player_2:
                nids.append(match.player_2.national_id)

            if (nid1 in nids) and (nid2 in nids):
                match.score_1 = score1
                match.score_2 = score2
                break

    def round_has_remaining_ongoing_matches(self) -> bool:
        """Return true if at least one match has score 0-0"""
        for match in self.matches_list:
            if match.score_1 + match.score_2 == 0:
                return True
        return False
