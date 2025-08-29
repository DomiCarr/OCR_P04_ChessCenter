import random
from typing import List
from datetime import datetime

from models.tournament_round import Round
from models.player import Player
from models.match import Match
from models.tournament_player import TournamentPlayer


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
        rounds_list_dict = []  # converts rounds_list in a dict
        if self.rounds_list:
            for r in self.rounds_list:
                rounds_list_dict.append(r.to_dict())

        players_list_dict = []  # converts players_list in a dict
        if self.players_list:
            for p in self.players_list:
                players_list_dict.append(p.to_dict())

        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "ongoing_round_number": self.ongoing_round_number,
            "nb_of_rounds": self.nb_of_rounds,
            "rounds_list": rounds_list_dict,
            "players_list": players_list_dict
        }

    def start_tournament(self):
        if self.start_date:
            return None
        self.ongoing_round_number = 1
        self.start_date = datetime.now()

    def start_round(self, round_number):
        # Sort the players :shuffle for round 1, sort by score for others
        players_sorted = self.sort_players(round_number)

        # Round name =. Tournament Name + "Round" + round_number
        round_name = f"{self.name} - Round {round_number}"

        # start the round for this tournament
        round = Round(name=round_name,
                      start_date=datetime.now(),
                      matches_list=[]
                      )

        # create the matches for this round
        self.create_matches(round, players_sorted)

    def sort_players(self, round_number: int) -> List["Player"]:
        """Sort the players :shuffle for round 1, sort by score for others"""
        if not self.players_list:
            return []

        if round_number == 1:
            random.shuffle(self.players_list)
        else:
            self.players_list.sort(key=lambda p: p.score, reverse=True)
        return self.players_list

    def create_matches(self, round: "Round", players_sorted: list["Player"]) -> None:
        for i in range(0, len(players_sorted) - 1, 2):
            p1 = players_sorted[i]
            p2 = players_sorted[i+1]

            # Randomly assign the color to the players
            colors_choice = [("white", "black"), ("black", "white")]
            color1, color2 = random.choice(colors_choice)

            # create a match
            match = Match(player_1=p1,
                          color_1=color1,
                          score_1=0,
                          player_2=p2,
                          color_2=color2,
                          score_2=0
                          )

            # Add the match to the rounds matches list
            round.matches_list.append(match)

