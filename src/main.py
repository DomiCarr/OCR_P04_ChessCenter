"""main.py - Application entry point."""

import os
from config import DATA_DIRECTORY_PATH

from controllers.main_menu import MainMenu
from controllers.players_manager import PlayersManager
from controllers.tournaments_manager import TournamentsManager


class Main:
    """Initialize app directories, controllers et main menu"""

    # create the data directory if not exist
    os.makedirs(DATA_DIRECTORY_PATH, exist_ok=True)

    # instanciate controllers
    players_manager = PlayersManager()
    tournaments_manager = TournamentsManager()

    # Launch the main menu
    main_menu = MainMenu(players_manager, tournaments_manager)
    main_menu.show_menu()     # Launch CLI


if __name__ == "__main__":
    # Start the program
    Main()
