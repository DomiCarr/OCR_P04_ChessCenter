"""Player - Click commands"""

import click
from models.tournament import Tournament
from models.tournaments import Tournaments
from models.players import Players


@click.command()
@click.option("--name", prompt="name")
@click.option("--location", prompt="location")
@click.option("--description", prompt="description")
def add_tournament(name, location, description):
    """Add a new tournament via CLI."""
    tournament_bdd = Tournaments()
    new_tournament = Tournament(name, location, description)

    if tournament_bdd.tournament_exists(name):
        click.echo("Tournament already exists.")
    else:
        tournament_bdd.add_tournament(new_tournament)
        click.echo("Tournament added successfully!")


@click.command()
@click.option("--tournament_name", prompt="Tournament_name")
@click.option("--player_id", prompt="Player national id")
def register_player(tournament_name, player_id):
    """Add a player in a tournament"""
    tournaments_bdd = Tournaments()
    players_bdd = Players()

    # Check if the tournament exists
    tournament = tournaments_bdd.get_tournament_by_name(tournament_name)
    if tournament is None:
        click.echo(f"Tournament '{tournament_name}' not found.")
        return

    # Check if the player exists
    player = players_bdd.get_player_by_id(player_id)
    if player is None:
        click.echo(f"Player with ID '{player_id}' not found.")
        return

    # Check if player is already registered in this tournament
    if tournament.players_list is not None:
        for p in tournament.players_list:
            if p.national_id == player_id:
                click.echo(f"Player '{player.first_name} {player.last_name}' is already registered in this tournament.")
                return

    # Register the player
    if tournament.players_list is None:
        tournament.players_list = []
    tournament.players_list.append(player)
    tournaments_bdd.update_tournament(tournament)
    click.echo(f"Player '{player.first_name} {player.last_name}' registered successfully in tournament '{tournament_name}'.")

@click.command()
def list_tournaments():
    """List all tournaments sorted by name."""
    tournaments_bdd = Tournaments()
    all_tournaments = tournaments_bdd.list_tournaments()
    if not all_tournaments:
        click.echo("No tournament found.")
    else:
        sorted_tournaments = sorted(all_tournaments, key=lambda t: t.name.lower())
        for tournament in sorted_tournaments:
            click.echo(f"{tournament.name}")

@click.command()
@click.option("--tournament_name", prompt="Tournament_name")
def start_tournaments(tournament_name):
    """Start a tournament"""
    tournaments_bdd = Tournaments()

    # Check if the tournament exists
    tournament = tournaments_bdd.get_tournament_by_name(tournament_name)
    if tournament is None:
        click.echo(f"Tournament '{tournament_name}' not found.")
        return

    # Update start_date and ongoing round = 1
    tournament.start_tournament()
