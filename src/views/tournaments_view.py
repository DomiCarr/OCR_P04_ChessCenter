# views/tournaments_view.py
from views.base_view import BaseView
from models.tournament import Tournament
from models.tournament_round import TournamentRound
from models.player import Player
from typing import List


class TournamentsView(BaseView):
    def ask_new_tournament_details(self) -> dict:
        """Prompt the user for details to create a tournament."""
        name = input("Tournament name: ").strip()
        location = input("Location: ").strip()
        description = input("Description: ").strip()
        return {
            "name": name,
            "location": location,
            "description": description
        }

    def ask_tournament_name(self) -> str:
        """Ask the user for a tournament name"""
        return input("Tournament name: ").strip()

    def ask_tournament_players_nids(self) -> list[str]:
        """Ask the user to enter players national ids"""
        nids = input("Enter players national ids separated by comma: ").strip()
        return [i.strip() for i in nids.split(",") if i.strip()]

    def display_tournaments(self, tournaments: List[Tournament]):
        print("----- Tournaments List --------------------------------")
        for t in tournaments:
            print(
                f"- {t.name} at {t.location}, "
                f"{t.description}, {len(t.players_list)} players"
            )

    def display_tournament_players(self, tournament: "Tournament"):
        """Display the tournament players"""
        print("----- Tournaments -------------------------------------------")
        print(f"Name:  {tournament.name}")
        print(f"Location:  {tournament.location}")
        print(f"Description:  {tournament.description}")
        print(f"Start date:  {tournament.start_date}")
        print(f"Ongoing round:  {tournament.ongoing_round_number}")
        print("----- Tournaments Registered players --------------------------------")
        players: list[Player] = tournament.players_list
        for player in players:
            print(
                f" - {player.national_id} {player.first_name}"
                f" {player.last_name}"
                )

    def display_round_matches(self,
                              current_round: TournamentRound,
                              comment="Matches list"):
        """print all matches for a round"""
        print(f" --------- {comment} ----------- ")
        for match in current_round.matches_list:
            p1 = match.player_1
            col1 = match.color_1
            score1 = match.score_1

            p2 = match.player_2
            col2 = match.color_2
            score2 = match.score_2

            print(f"{p1.national_id} {p1.first_name} {p1.last_name} "
                  f"({col1}) score: {score1} --- "
                  f"{p2.national_id} {p2.first_name} {p2.last_name} "
                  f"({col2}) score: {score2}")

    def display_tournament_rounds(self, tournament: Tournament):
        """Display all rounds of a tournament with their matches"""
        if not tournament.rounds_list:
            print("\nNo rounds available for this tournament.")
            return

        print(f"=== Rounds for tournament '{tournament.name}' ===")
        for i, current_round in enumerate(tournament.rounds_list, start=1):
            print(f"\n--- Round {i}: {current_round.name} ---")
            self.display_round_matches(current_round, comment="Matches list")

    def display_tournament_details(self, tournament: "Tournament"):
        """Display the tournament details"""
        print("----- Tournaments Details  --------------------------------")
        print(f"Name:  {tournament.name}")
        print(f"Location:  {tournament.location}")
        print(f"Description:  {tournament.description}")
        print(f"Start date:  {tournament.start_date}")
        print(f"Ongoing round:  {tournament.ongoing_round_number}")
        print("------ Registered Players ------ ")
        players: list[Player] = tournament.players_list
        for player in players:
            print(
                f" - {player.national_id} {player.first_name}"
                f"{player.last_name}"
                )

        print("------ Rounds ------ ")
        self.display_tournament_rounds(tournament)

    def ask_match_results(self) -> List[tuple[str, float, str, float]] | None:
        """Ask the match results"""
        items = [results.strip() for results in
                 input(
                        "Enter match results (nid1, score 1, nid2, score 2: "
                        ).strip().split(',')]

        if len(items) != 4:
            print(f"Results entry, must have 4 items: {items}")
            return None

        try:
            score_1 = float(items[1])
            score_2 = float(items[3])
        except ValueError:
            print(f"Scores must be numeric: {items[1]}, {items[3]}")
            return None

        nid_1 = items[0]
        nid_2 = items[2]

        return nid_1, score_1, nid_2, score_2

    def display_round_start(self, tournament: "Tournament"):
        current_round = tournament.rounds_list[tournament.ongoing_round_number - 1]
        print(f"'{current_round.name}' started  ===")

    def display_tournament_winner(self, tournament: Tournament):
        """Display the tournament winner and score"""
        winner_player, winner_score = tournament.get_tournament_winner()
        if winner_player:
            print(f"\n=== Tournament '{tournament.name}' finished ===")
            print(
                f"Winner: {winner_player.first_name} "
                f"{winner_player.last_name} "
                f"(NID: {winner_player.national_id}) "
                f"with score: {winner_score}"
            )
        else:
            print(
                f"\nTournament '{tournament.name}' finished."
                f"No winner found."
                )

    def display_players_ranking(self, tournament: Tournament):
        """Display players ranking by score (highest first)."""

        if not tournament.players_list:
            print("No players registered for this tournament.")
            return

        scores = tournament.compute_tournament_players_score(tournament.rounds_list)

        sorted_players = sorted(
            tournament.players_list,
            key=lambda p: scores.get(p.national_id, 0.0),
            reverse=True
        )

        print(f"---- Players ranking for Tournament '{tournament.name} ----")

        for idx, player in enumerate(sorted_players, start=1):
            score = scores.get(player.national_id, 0.0)
            print(
                f"({idx}. NID: {player.national_id}) "
                f"{player.first_name} {player.last_name}"
                f" - Score: {score}"
                )

