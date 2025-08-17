"""manage_players - Controller for player CLI"""

import click
from views.players_cli import add_player
from views.players_cli import list_players


@click.group()
def mycommands():
    """CLI for managing players."""
    pass


# Attach commands from views
mycommands.add_command(add_player)
mycommands.add_command(list_players)
