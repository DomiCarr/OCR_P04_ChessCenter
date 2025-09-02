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
        print("\n=== Tournaments List ===")
        for t in tournaments:
            print(
                f"- {t.name} at {t.location}, "
                f"{t.description}, {len(t.players_list)} players"
            )

    def display_tournament_details(self, tournament: "Tournament"):
        """Display the tournament details"""
        print("\ ------ Tournament Details ------ ")
        print(f"Name:  {tournament.name}")
        print(f"Location:  {tournament.location}")
        print(f"Description:  {tournament.description}")
        print(f"Start date:  {tournament.start_date}")
        print(f"Ongoing round:  {tournament.ongoing_round_number}")
        print("\ ------ Registered Players ------ ")
        players: list[Player] = tournament.players_list
        for player in players:
            print(f" - {player.national_id} {player.first_name} {player.last_name}")

    def ask_match_results(self) -> List[tuple[str, float, str, float]] | None:
        """Ask the match results"""
        items = [results.strip() for results in
                 input(
                        "Enter match results (nid1, score 1, nid2, score 2: "
                        ).strip().split(',')]
        print("items: ", items)
        print("len items: ", len(items))
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
