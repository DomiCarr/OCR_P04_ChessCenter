"""Application entry point."""
from controllers.init_app import init_app
from controllers.main_menu import MainMenu
from controllers.players_manager import PlayersManager


if __name__ == "__main__":
    init_app()       # Ensure directories exist
    players_manager = PlayersManager()
    main_menu = MainMenu(players_manager)
    main_menu.show_menu()     # Launch CLI
