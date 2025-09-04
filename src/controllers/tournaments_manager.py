# controllers/tournaments_manager.py

from models.base import compute_elo
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
        current_tournament.start_round(current_tournament.ongoing_round_number)
        self.tournaments.update_tournament(current_tournament)
        self.view.display_message(
            f"Round {current_tournament.ongoing_round_number} of '{name}' started."
        )

    def update_match_results(self):
        """Update the tournament with the match results"""

        name = self.view.ask_tournament_name()
        current_tournament = self.tournaments.get_tournament_by_name(name)

        if not current_tournament:
            self.view.display_message(f"Tournament '{name}' not found.")
            return  # tournament not found

        # Display ongoing round matches
        ongoing_round = current_tournament.rounds_list[
            current_tournament.ongoing_round_number - 1
        ]
        self.view.display_round_matches(ongoing_round)

        # Ask match results
        match_results = self.view.ask_match_results()
        if not match_results:
            return

        # compute and update players elo
        self.update_players_elo(match_results)

        # Save updated tournament and display the new results
        ongoing_round.update_match_results([match_results])
        self.tournaments.update_tournament(current_tournament)
        self.view.display_round_matches(ongoing_round)

        # Check if round is finished
        if not ongoing_round.round_has_remaining_ongoing_matches():
            # If last round, close tournament
            if current_tournament.ongoing_round_number >= current_tournament.nb_of_rounds:
                current_tournament.close_tournament()
                self.tournaments.update_tournament(current_tournament)
                self.view.display_tournament_winner(current_tournament)
            else:
                # Start next round
                current_tournament.ongoing_round_number += 1
                current_tournament.start_round(current_tournament.ongoing_round_number)
                self.tournaments.update_tournament(current_tournament)
                self.view.display_round_start(current_tournament)

    def update_players_elo(self, match_results: tuple):
        """update ELO for both players match with debug prints"""
        print("=== update_players_elo START ===")
        print(f"match_results: {match_results}")

        player1 = match_results[0][0]
        player2 = match_results[1][0]
        score1 = match_results[0][1]
        score2 = match_results[1][1]

        print(f"player1 object: {player1}")
        print(f"player2 object: {player2}")
        print(f"score1: {score1}")
        print(f"score2: {score2}")
        print(f"player1 current elo: {player1.elo}")
        print(f"player2 current elo: {player2.elo}")

        new_elo_p1, new_elo_p2 = compute_elo(
            player1_current_elo=player1.elo,
            player2_current_elo=player2.elo,
            player1_score=score1,
            player2_score=score2
        )

        print(f"new_elo_p1: {new_elo_p1}")
        print(f"new_elo_p2: {new_elo_p2}")

        # Update ELO
        player1.elo = new_elo_p1
        player2.elo = new_elo_p2

        print(f"player1 updated elo: {player1.elo}")
        print(f"player2 updated elo: {player2.elo}")

        # Save players
        self.players.update_player(player1)
        self.players.update_player(player2)

        print("=== update_players_elo END ===")

    def find_valid_opponent(self,
                            player: "Player",
                            opponents: list["Player"],
                            current_tournament: Tournament) -> "Player" | None:
        """
        Find the first valid opponent for the given player among candidates.
        Return None if no valid opponent is found.
        """
        print("find_valid_opponent - start")
        print("find_valid_opponent - player:", player)
        print("find_valid_opponent - opponents:", opponents)
        print("find_valid_opponent - current_tournament:", current_tournament.name)

        for idx, opponent in enumerate(opponents, start=1):
            print(f"find_valid_opponent - checking opponent {idx}:", opponent)
            played_before = current_tournament.players_played_together(
                player.national_id, opponent.national_id)
            print(f"find_valid_opponent - player {player.national_id} vs opponent {opponent.national_id} - played_before:", played_before)

            if not played_before:
                print(f"find_valid_opponent - valid opponent found:", opponent)
                return opponent

        print("find_valid_opponent - no valid opponent found")
        return None

