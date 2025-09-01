class TournamentRound:

    def __init__(self,
                 name,
                 start_datetime,
                 end_datetime,
                 matches_list):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches_list = matches_list or []

    def to_dict(self):
        matches_list_dict = []
        if self.matches_list:
            for m in self.matches_list:
                matches_list_dict.append(m.to_dict())

        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat() if self.start_datetime else None,
            "end_datetime": self.end_datetime.isoformat() if self.end_datetime else None,
            "matches_list": matches_list_dict
        }


"""
renommer Round en TournamentRound
"""