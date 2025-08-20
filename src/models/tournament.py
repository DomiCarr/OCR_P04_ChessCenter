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

