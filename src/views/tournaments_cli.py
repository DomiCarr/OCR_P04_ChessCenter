"""Player - Click commands"""

import click
from models.tournament import Tournament
from models.tournaments import Tournaments

@click.command()
@click.option("--name", prompt="name")
@click.option("--location", prompt="location")
@click.option("--description", prompt="description")

def add_tournament(name, location, description):
    """Add a new player via CLI."""
    tournament_bdd = Tournaments()
    new_tournament = Tournament(name, location, description)

    if tournament_bdd.tournament_exists(name):
        click.echo("Tournament already exists.")
    else:
        tournament_bdd.add_tournament(new_tournament)
        click.echo("Tournament added successfully!")
