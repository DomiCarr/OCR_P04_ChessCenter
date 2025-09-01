# views/tournaments_view.py
from views.base_view import BaseView
from models.tournament import Tournament
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

