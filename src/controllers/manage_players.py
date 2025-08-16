from models.player import Player
from models.players import Players

# load the players_bdd from the JSON file
players_bdd = Players()

# Create a new player instance
new_player = Player(325, 'Sebastian', 'Bach', '31/03/1865')
print("Adding new player:", new_player.to_dict())

# Add the player to the list and save to the JSON file
players_bdd.add_player(new_player)
print("Current list of players:", [p.to_dict() for p in players_bdd.players])
