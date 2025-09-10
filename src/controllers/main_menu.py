""" controllers/main_menu.py """
from views.main_menu_view import MainMenuView


class MainMenu:
    """Main menu of the program"""
    def __init__(self,
                 players_manager,
                 tournaments_manager):
        self.players_manager = players_manager
        self.tournaments_manager = tournaments_manager
        self.view = MainMenuView()

    def show_menu(self):
        """Display the main menu and handle user input."""
        while True:
            self.view.display_menu()
            choice = self.view.ask_menu_option()
            self.handle_choice(choice)

    def handle_choice(self, choice: str):
        """Route user choice to the correct controller action."""
        if choice == "1":
            self.players_manager.list_players()
        elif choice == "2":
            self.players_manager.add_player()
        elif choice == "3":
            self.tournaments_manager.list_tournaments()
        elif choice == "4":
            self.tournaments_manager.add_tournament()
        elif choice == "5":
            self.tournaments_manager.display_tournament()
        elif choice == "6":
            self.tournaments_manager.register_tournament_players()
        elif choice == "7":
            self.tournaments_manager.display_tournament_players()
        elif choice == "8":
            self.tournaments_manager.start_tournament()
        elif choice == "9":
            self.tournaments_manager.update_match_results()
        elif choice == "91":
            self.tournaments_manager.display_tournament_ranked_players()
        elif choice == "0":
            self.view.display_message("Exiting...")
            exit(0)
        else:
            self.view.display_message("Invalid choice. Try again.")
