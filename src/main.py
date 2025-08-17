"""Application entry point."""
from controllers.init_app import init_app
from controllers.manage_players import mycommands


if __name__ == "__main__":
    init_app()       # Ensure directories exist
    mycommands()     # Launch CLI
