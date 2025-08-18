"""Player - Click commands"""

import click
from models.tournament import Tournament

@click.command()
@click.option("--name", prompt="name")
@click.option("--location", prompt="location")
@click.option("--last", prompt="Last name")
def add_tournament(id, first, last, birth):
    """Add a new player via CLI."""
    players_bdd = Players()
    new_player = Player(id, first, last, birth)

    if players_bdd.player_exists(id):
        click.echo("Player already exists.")
    else:
        players_bdd.add_player(new_player)
        click.echo("Player added successfully!")

@click.command()
def list_tournaments():
    """List all players sorted by last name then first name."""
    players_bdd = Players()
    all_players = players_bdd.list_players()
    if not all_players:
        click.echo("No players found.")
    else:
        # Tri par nom puis prénom
        sorted_players = sorted(all_players, key=lambda p: (p.last_name.lower(), p.first_name.lower()))
        for player in sorted_players:
            click.echo(f"{player.national_id} - {player.first_name} {player.last_name}, {player.birth_date}")
