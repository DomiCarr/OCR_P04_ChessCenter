""" Players """

import json
from config import PLAYERS_FILE_PATH
from .player import Player


class Players:
    def __init__(self):
        self.players = []
        self.file_path = PLAYERS_FILE_PATH
        self.load_players()

    def load_players(self):
        """Load all players from the JSON file into self.players."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                players_data = json.load(f)
                for pdata in players_data:
                    self.players.append(Player(**pdata))
        except (FileNotFoundError, json.JSONDecodeError):
            self.players = []

    def add_player(self, player: Player):
        """Add a new player to the list and save to JSON."""
        self.players.append(player)
        self.save_players()

    def save_players(self):
        """Save the current list of players to the JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(
                [p.to_dict() for p in self.players],
                f,
                ensure_ascii=False, indent=4
            )

    def list_players(self):
        """Return a list of all players."""
        return self.players

    def player_exists(self, national_id) -> bool:
        """Check if a player with the given national_id exists."""
        return any(player.national_id == national_id for player in self.players)

    def update_player(self, updated_player: Player):
        """Update a player in the list if it exists and save the changes to JSON."""
        for player_index, player in enumerate(self.players):
            if player.national_id == updated_player.national_id:
                self.players[player_index] = updated_player
                self.save_players()
                return True
        return False  # Player not found

    def get_player_by_id(self, national_id: str) -> Player | None:
        """Return a Player object by national_id, or None if not found."""
        for player in self.players:
            if player.national_id == national_id:
                return player
        return None
