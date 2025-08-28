class Tournament:

    def __init__(self,
                 name: str,
                 location: str,
                 description: str,
                 start_date: str = None,
                 end_date: str = None,
                 ongoing_round_number: int = 0,
                 rounds_list: list = None,
                 players_list: list = None,
                 nb_of_rounds: int = 4):

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_of_rounds = nb_of_rounds
        self.ongoing_round_number = ongoing_round_number
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description

    def to_dict(self):
        """converts Tournament in a dict to save it as JSON"""
        rounds_list_dict = [] # converts rounds_list in a dict
        if self.rounds_list:
            for r in self.rounds_list:
                rounds_list_dict.append(r.to_dict())

        players_list_dict = [] # converts players_list in a dict
        if self.players_list:
            for p in self.players_list:
                players_list_dict.append(p.to_dict())

        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "ongoing_round_number": self.ongoing_round_number,
            "nb_of_rounds": self.nb_of_rounds,
            "rounds_list": rounds_list_dict,
            "players_list": players_list_dict
        }