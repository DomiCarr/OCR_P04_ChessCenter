
import click
from models.player import Player
from models.players import Players

@click.group()
def mycommands():
    """CLI for managing players."""
    pass


@mycommands.command()
@click.option("--id", prompt="National ID", type=int)
@click.option("--first", prompt="First name")
@click.option("--last", prompt="Last name")
@click.option("--birth", prompt="Birth date")
def add_player(id, first, last, birth):
    """Add a new player via CLI."""
    players_bdd = Players()
    new_player = Player(id, first, last, birth)

    if players_bdd.player_exists(id):
        click.echo("Player already exists.")
    else:
        players_bdd.add_player(new_player)
        click.echo("Player added successfully!")
