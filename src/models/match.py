from models.player import Player


class Match:
    def __init__(self, player_1, color_1, score_1,
                 player_2, color_2, score_2):
        self.player_1 = player_1
        self.color_1 = color_1
        self.score_1 = score_1

        self.player_2 = player_2
        self.color_2 = color_2
        self.score_2 = score_2

    def to_dict(self):
        return {
            "player_1": self.player_1.to_dict(),
            "color_1": self.color_1,
            "score_1": self.score_1,
            "player_2": self.player_2.to_dict(),
            "color_2": self.color_2,
            "score_2": self.score_2
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Player.from_dict(data["player_1"]),
            data["color_1"],
            data["score_1"],
            Player.from_dict(data["player_2"]),
            data["color_2"],
            data["score_2"]
        )

    def update_match_scores(self, score1: float, score2: float):
        self.score_1 = score1
        self.score_2 = score2
