""" Tournaments """

import json
from config import TOURNAMENTS_FILE_PATH
from .tournament import Tournament
from .player import Player
from .round import Round


class Tournaments:
    def __init__(self):
        self.tournaments = []
        self.file_path = TOURNAMENTS_FILE_PATH
        self.load_tournaments()

    def load_tournaments(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                tournaments_data = json.load(f)
                for pdata in tournaments_data:
                    # rebuild players
                    if pdata.get("players_list"):
                        pdata["players_list"] = [Player(**p) for p in pdata["players_list"]]
                    # rebuild rounds + matches
                    if pdata.get("rounds_list"):
                        for rdata in pdata["rounds_list"]:
                            if rdata.get("matches_list"):
                                for mdata in rdata["matches_list"]:
                                    mdata["match"] = [
                                        [Player(**mdata["match"][0][0]),
                                         mdata["match"][0][1],
                                         mdata["match"][0][2]],
                                        [Player(**mdata["match"][1][0]),
                                         mdata["match"][1][1],
                                         mdata["match"][1][2]],
                                        ]
                            rdata["matches_list"] = [Round(**rdata)]
                        pdata["rounds_list"] = [Round(**r) for r in pdata["rounds_list"]]

                    self.tournaments.append(Tournament(**pdata))
        except (FileNotFoundError, json.JSONDecodeError):
            self.tournaments = []

    def add_tournament(self, tournament: Tournament):
        """Add a new player to the list and save to JSON."""
        self.tournaments.append(tournament)
        self.save_tournaments()

    def save_tournaments(self):
        """Save the current list of tournaments to the JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tournaments], f, ensure_ascii=False, indent=4)

    def tournament_exists(self, name) -> bool:
        """Check if a tournament with the given national_id exists."""
        return any(tournament.name == name for tournament in self.tournaments)

    def get_tournament_by_name(self, name: str) -> Tournament | None:
        """Return a Tournament by is name, or None if not found."""
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament
        return None

    def update_tournament(self, updated_tournament: Tournament) -> bool:
        """Update a tournament in the list if it exists and save the changes to JSON."""
        for idx, tournament in enumerate(self.tournaments):
            if tournament.name == updated_tournament.name:
                self.tournaments[idx] = updated_tournament
                self.save_tournaments()
                return True
        return False  # Tournament not found

    def list_tournaments(self):
        """Return a list of all tournaments."""
        return self.tournaments

    """


    """

