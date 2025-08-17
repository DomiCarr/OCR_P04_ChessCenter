"""Player - Click commands"""

import click
from models.player import Player
from models.players import Players

@click.command()
@click.option("--id", prompt="National ID")
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

@click.command()
def list_players():
    """List all players."""
    players_bdd = Players()
    all_players = players_bdd.list_players()
    if not all_players:
        click.echo("No players found.")
    else:
        for player in all_players:
            click.echo(f"{player.national_id} - {player.first_name} {player.last_name}, {player.birth_date}")
