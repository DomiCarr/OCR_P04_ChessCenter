from models.player import Player


class JsonTest:
    # on créé 1 joueurs
    player = Player(325, 'Sebastian', 'Bach', '31/03/1865')
    print("on va ajouter le player: ", player)
    player.add_player_in_json()

