"""views/players_view.py"""

from views.base_view import BaseView
from models.player import Player
from datetime import datetime


class PlayersView(BaseView):
    def ask_new_player(self) -> Player:
        """Ask user to enter new player data."""
        print("\n=== Add New Player ===")
        national_id = input("National ID: ").strip()
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()

        # birth date
        while True:
            birth_date_str = input("Birth date (DD/MM/YYYY): ").strip()
            try:
                birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y").date()
                break  # Invalid date format
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        # convert to date
        return Player(
            national_id=national_id,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date
        )

    def display_players(self, players: list[Player]):
        print("\n=== Players List ===")
        for p in players:
            print(
                f"{p.national_id} - {p.first_name} {p.last_name} "
                f"(born {p.birth_date}) "
                )
