# views/tournaments_view.py


class TournamentsView:
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

    def display_message(self, message: str)
        """ Display a simple message"""
        print(message)

    def display_tournaments(self, tournaments: list):
        print("\n=== Tournaments List ===")
        for t in tournaments:
            print(f"- {t.name} at {t.location}, {t.description}, {len(t.players_list)} players")
