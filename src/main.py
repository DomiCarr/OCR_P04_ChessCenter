"""Application entry point."""
from controllers.manage_players import mycommands
from controllers.init_app import init_app

if __name__ == "__main__":
    init_app()       # Ensure directories exist
    mycommands()     # Launch CLI
