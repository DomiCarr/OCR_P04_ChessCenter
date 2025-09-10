"""views/main_menu_view.py"""

from views.base_view import BaseView


class MainMenuView(BaseView):
    """Controller view for the main menu"""

    def display_menu(self):
        """Print the main menu options"""
        print("\n=== Main Menu ===")
        print("1. List the players")
        print("2. Add a player")
        print("3. List the tournaments")
        print("4. Add a tournament")
        print("5. Display a tournament details")
        print("6. Register players to a tournament")
        print("7. List tournament registered players")
        print("8. Start tournament")
        print("9. Enter match results")
        print("91. List tournament ranked players")
        print("0. Exit")

    def ask_menu_option(self) -> str:
        """Ask the user a menu option"""
        return input("Select an option: ").strip()
