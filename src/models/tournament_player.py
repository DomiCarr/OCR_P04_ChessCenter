"""TournamentPlayer - Associate a Player with a score in a specific tournament."""

from .player import Player


class TournamentPlayer:
    def __init__(self, player: Player):
        self.player = player
        self.score = 0

    def to_dict(self):
        return {
            "player": self.player.to_dict(),
            "score": self.score
        }




