# controllers/tournaments_manager.py
from typing import Optional, List
import sys

from models.tournaments import Tournaments
from models.tournament import Tournament
from models.players import Players
from models.player import Player
from views.tournaments_view import TournamentsView


class TournamentsManager:
    def __init__(self):
        self.tournaments = Tournaments()
        self.players = Players()
        self.view = TournamentsView()

    def display_tournament(self):
        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)

        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return

        self.view.display_tournament_details(current_tournament)

    def display_tournament_players(self):
        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)

        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return

        self.view.display_tournament_players(current_tournament)

    def display_tournament_ranked_players(self):
        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)

        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return

        self.view.display_players_ranking(current_tournament)

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

    def start_tournament(self):
        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)

        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return  # tournament not found

        if current_tournament.start_date:
            self.view.display_message(f"Tournament '{name}' has already started.")
            return  # Tournament already started

        # update the current tournament
        current_tournament.start_tournament()
        self.tournaments.add_tournament(current_tournament)
        self.view.display_message(f"Tournament '{name}' started.")

    def start_round(self):
        """Start a new round for a tournament"""
        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)

        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return  # tournament not found

        # Start the round (round number managed internally by the tournament)
        current_tournament.start_round()
        self.tournaments.update_tournament(current_tournament)
        self.view.display_message(
            f"Round {current_tournament.ongoing_round_number} of '{name}' started."
        )

    def update_match_results(self):
        """Update the tournament with the match results"""

        # Ask for tournament name
        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)
        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return  # tournament not found

        # Display ongoing round matches
        if not current_tournament.rounds_list:
            self.view.display_message("No rounds have been started yet.")
            return

        ongoing_round = current_tournament.rounds_list[current_tournament.ongoing_round_number - 1]

        self.view.display_round_matches(ongoing_round)

        # Ask match results
        match_results = self.view.ask_match_results()
        if not match_results:
            return

        match_results_obj = match_results

        # Save updated tournament and display the new results
        ongoing_round.update_match_results(match_results_obj)
        self.tournaments.update_tournament(current_tournament)
        self.view.display_round_matches(ongoing_round)

        # Check if round is finished
        if not ongoing_round.round_has_remaining_ongoing_matches():
            if current_tournament.ongoing_round_number >= current_tournament.nb_of_rounds:
                # Last round, close tournament
                current_tournament.close_tournament()
                self.tournaments.update_tournament(current_tournament)
                self.view.display_players_ranking(current_tournament)
                self.view.display_message(f"Tournament '{name}' closed.")
                sys.exit(0)  # Exit the application
            else:
                # Start next round
                current_tournament.start_round()
                self.tournaments.update_tournament(current_tournament)
                self.view.display_round_start(current_tournament)

