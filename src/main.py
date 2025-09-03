"""main.py - Application entry point."""

from controllers.init_app import init_app
from controllers.main_menu import MainMenu
from controllers.players_manager import PlayersManager
from controllers.tournaments_manager import TournamentsManager

if __name__ == "__main__":
    # Initialize directories and files
    init_app()

    # instanciate models
    players_manager = PlayersManager()
    tournaments_manager = TournamentsManager()

    # Launch the main menu
    main_menu = MainMenu(players_manager, tournaments_manager)
    main_menu.show_menu()     # Launch CLI



    """
    main: separer l'instaciation des modeles
    main_menu :




    """

