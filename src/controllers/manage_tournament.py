"""
- créer le tournoi: name, location, description
-tant que le tournoi n'as pas commencé (star_date a blanc)
    ajouter les joueurs a la liste des joueurs du tournois
-lancer le tournoi :
    affecter ongoing_round = 1
    créer le round 1 : name du round = "name du tournoi + round 1"
    renseigner la datetime de début du tournoi
    créer les matchs
        mélanger la liste des joueurs aléatoirement
        associer les joueurs par paire
        mettre un score a zéro a chaque joueur
        affecter aléatoirement blanc ou noir a chaque joueur
- tant que le round n'est pas terminé (il reste des matchs avec 2 scores a zero)
    saisir le résultats d'un match à partir de la liste des matchs
    modifier le score total des journeurs pour le tournoi
- incrémenter ne numero du round : ongoing_round =+1
- tant qu'il reste des rounds à jouer (ongoing_round <= nb_of_rounds)
    Trier les joueurs par ordre de point
    Associer les joueurs par paire dans l'ordre en évitant les matchs deja joués
    mettre un score a zéro a chaque joueur
    affecter aléatoirement blanc ou noir a chaque joueur
- tant que le round n'est pas terminé (il reste des matchs avec 2 scores a zero)
    saisir le résultats d'un match à partir de la liste des matchs
    modifier le score total des journeurs pour le tournoi
- lorsque le tournoi est fini renseigner la datetime de fin
- lister les joueurs par ordre de points le gagnant en premier


1: faire les modeles
2: ajouter la logique: controller menu principal
3: Affichage du menu dans un 1er temps
4: ajouter les menus dans l'ordre
5:

"""

"""manage_players - Controller for player CLI"""

import click

# initialize the tournament
from views.tournaments_cli import add_tournament


@click.group()
def mycommands():
    """CLI for managing a tournament."""
    pass


# Attach commands from views
mycommands.add_command(add_tournament)
"""
mycommands.add_command(register_player)

mycommands.add_command(start_tournament)

mycommands.add_command(add_round)

mycommands.add_command(xxxx_tournament)
mycommands.add_command(xxxx_tournament)
mycommands.add_command(xxxx_tournament)
mycommands.add_command(xxxx_tournament)
mycommands.add_command(xxxx_tournament)

mycommands.add_command(end_tournament)

"""


