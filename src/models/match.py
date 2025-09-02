from models.player import Player


class Match:
    def __init__(self,
                 player_1,
                 color_1,
                 score_1,
                 player_2,
                 color_2,
                 score_2):
        self.match = ([player_1, color_1, score_1],
                      [player_2, color_2, score_2])

    def to_dict(self):
        return {
            "match": [
                [self.match[0][0].to_dict(),
                 self.match[0][1],
                 self.match[0][2]],
                [self.match[1][0].to_dict(),
                 self.match[1][1],
                 self.match[1][2]]
            ]
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild a Match object from a JSON dictionary."""
        match_data = data.get("match", [])

        player_1 = Player.from_dict(match_data[0][0])
        color_1 = match_data[0][1]
        score_1 = match_data[0][2]

        player_2 = Player.from_dict(match_data[1][0])
        color_2 = match_data[1][1]
        score_2 = match_data[1][2]

        return cls(
                 player_1,
                 color_1,
                 score_1,
                 player_2,
                 color_2,
                 score_2
                 )

    def update_match_scores(self, score1: float, score2: float):
        """update match score for both players"""
        self.match[0][2] = score1
        self.match[1][2] = score2
