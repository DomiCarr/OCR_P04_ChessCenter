""" Tournaments """

import json
from config import TOURNAMENTS_FILE_PATH
from .tournament import Tournament


class Tournaments:
    def __init__(self):
        self.tournaments = []
        self.file_path = TOURNAMENTS_FILE_PATH
        self.load_tournaments()

    def load_tournaments(self):
        """Load all tournaments from the JSON file into self.tournaments."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                tournaments_data = json.load(f)
                for pdata in tournaments_data:
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


#    def save_tournaments(self):
#        """Sauvegarde la liste des tournois dans un fichier texte brut."""
#        with open(self.file_path, "w", encoding="utf-8") as f:
#            for tournament in self.tournaments:
#                f.write(str(tournament.to_dict()) + "\n")

    def tournament_exists(self, name) -> bool:
        """Check if a tournament with the given national_id exists."""
        return any(tournament.name == name for tournament in self.tournaments)

"""
    def list_tournaments(self):
        #Return a list of all players.
        return self.tournaments



    def update_tournament(self, updated_tournament: Tournament):
        #Update a tournament in the list if it exists and save the changes to JSON.
        for tournament_index, tournament in enumerate(self.tournaments):
            if tournament.name == updated_tournament.name:
                self.tournaments[tournament_index] = updated_tournament
                self.save_tournaments()
                return True
        return False  # Tournament not found
"""

