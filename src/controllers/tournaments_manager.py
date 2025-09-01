# controllers/tournaments_manager.py

from models.tournaments import Tournaments
from models.tournament import Tournament
from models.players import Players
from views.tournaments_view import TournamentsView


class TournamentsManager:
    def __init__(self):
        self.tournaments = Tournaments()
        self.players = Players()
        self.view = TournamentsView()

    def add_tournament(self):
        tournament_details = self.view.ask_new_tournament_details()
        name = tournament_details["name"]

        if self.tournaments.tournament_exists(name):
            self.view.display_message(f"Tournament '{name}' already exists.")
            return

        new_tournament = Tournament(
            name=name,
            location=tournament_details["location"],
            description=tournament_details["description"]
            )
        self.tournaments.add_tournament(new_tournament)
        self.view.display_message(f"Tournament '{name}' added successfully.")

    def register_tournament_players(self):
        """Register tournament players"""
        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)

        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return

        nids = self.view.ask_tournament_players_nids()

        for nid in nids:
            player_to_register = self.players.get_player_by_nid(nid)
            if not player_to_register:
                self.view.display_message(f"Player with ID '{nid}' not found. Skipping.")
                continue
            if player_to_register in current_tournament.players_list:
                self.view.display_message(f"Player '{nid}' already registered. Skipping.")
                continue
            current_tournament.players_list.append(player_to_register)

        self.tournaments.update_tournament(current_tournament)

    def list_tournaments(self):
        """List all tournaments"""
        tournaments_list = self.tournaments.list_tournaments()
        if not tournaments_list:
            self.view.display_message("Tournaments list is empty")
            return
        self.view.display_tournaments(tournaments_list)



