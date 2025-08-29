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