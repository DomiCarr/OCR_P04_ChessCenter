class Tournament:

    def __init__(self,
                 name,
                 location,
                 start_date,
                 end_date,
                 ongoing_round_number,
                 rounds_list,
                 players_list,
                 description,
                 nb_of_rounds=4):

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_of_rounds = nb_of_rounds
        self.ongoing_round_number = ongoing_round_number
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description

