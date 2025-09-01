"""views/players_view.py"""

from models.player import Player


class PlayersView():
    def ask_new_player(self) -> dict:
        """Ask user to enter new player data."""
        print("\n=== Add New Player ===")
        national_id = input("National ID: ").strip()
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        birth_date = input("Birth date (DD/MM/YYYY): ").strip()
        return {
            "national_id": national_id,
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date
        }

    def display_players(self, players: list[Player]):
        print("\n=== Players List ===")
        for p in players:
            print(f"{p.national_id} - {p.first_name} {p.last_name} (born {p.birth_date})")

    def display_message(self, message: str):
        """Display a simple message."""
        print(message)