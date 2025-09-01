"""manage_players - Controller for player CLI"""

from models.player import Player
from models.players import Players
from views.players_view import PlayersView


class PlayersManager:
    def __init__(self):
        self.players_model = Players()
        self.players_view = PlayersView()

    def add_player(self):
        """Add a new player in the JSON file"""
        data = self.players_view.ask_new_player()

        # check if player already exists
        if self.players_model.player_exists(data["national_id"]):
            self.players_view.display_message("Player alrady exists")
            return

        # Create and save new player
        new_player = Player(
            national_id=data["national_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"]
        )
        self.players_model.add_player(new_player)
        self.players_view.display_message("Player added successfully.")

    def list_players(self):
        """List all players and display them via the view."""
        players = self.players_model.list_players()
        if not players:
            self.players_view.show_message("No players found.")
        else:
            self.players_view.show_players(players)