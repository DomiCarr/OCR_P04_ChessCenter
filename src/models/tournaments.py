""" Tournaments """

# Standard library
import json
from datetime import datetime

# Project modules
from config import TOURNAMENTS_FILE_PATH
from models.tournament import Tournament
from models.tournament_round import Round
from models.player import Player
from models.match import Match



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
                    """ DEPLACER LE REFACTORING DANS L'OBJET PLAYER """
                    # rebuild players_list
                    if pdata.get("players_list"):
                        pdata["players_list"] = [Player(**p) for p in pdata["players_list"]]

                    # Convert dates from ISO strings to datetime
                    if pdata.get("start_date"):
                        from datetime import datetime
                        pdata["start_date"] = datetime.fromisoformat(pdata["start_date"])
                    if pdata.get("end_date"):
                        pdata["end_date"] = datetime.fromisoformat(pdata["end_date"])

                # --- Rebuild rounds_list ---
                rounds_list = []
                if pdata.get("rounds_list"):
                    for rdata in pdata["rounds_list"]:

                        # Convert round datetime fields
                        if rdata.get("start_datetime"):
                            rdata["start_datetime"] = datetime.fromisoformat(rdata["start_datetime"])
                        if rdata.get("end_datetime"):
                            rdata["end_datetime"] = datetime.fromisoformat(rdata["end_datetime"])

                        # Rebuild matches_list inside the round
                        matches_list = []
                        if rdata.get("matches_list"):
                            for mdata in rdata["matches_list"]:
                                # Each match stores players + color + score
                                p1 = 0
                                p2 = 0

                                match = Match(
                                    player_1=p1.player, color_1=mdata["match"][0][1], score_1=mdata["match"][0][2],
                                    player_2=p2.player, color_2=mdata["match"][1][1], score_2=mdata["match"][1][2],
                                )
                                matches_list.append(match)

                        # Inject rebuilt matches into the round
                        rdata["matches_list"] = matches_list
                        rounds_list.append(Round(**rdata))

                # Replace rounds_list with the rebuilt one
                pdata["rounds_list"] = rounds_list

                # --- Build the Tournament object ---
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
