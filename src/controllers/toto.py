def create_matches(self,
                   tournament_round: "TournamentRound",
                   players_sorted: list["Player"]) -> None:
    """
    Create matches for the given round.
    - Players are paired consecutively by score (ELO as tie-break).
    - If a pair has already played, search next available player.
    - Randomly assign colors.
    - Handle odd number of players (last player gets no match).
    """
    unpaired = players_sorted.copy()
    matches = []

    while len(unpaired) > 1:
        p1 = unpaired[0]
        opponent = self._find_valid_opponent(p1, unpaired[1:])

        # Random color assignment
        colors_choice = [("white", "black"), ("black", "white")]
        color1, color2 = random.choice(colors_choice)

        match = Match(
            player_1=p1,
            color_1=color1,
            score_1=0,
            player_2=opponent,
            color_2=color2,
            score_2=0
        )
        matches.append(match)

        # Remove paired players
        unpaired.remove(p1)
        unpaired.remove(opponent)

    # If odd number of players, one remains without opponent
    if unpaired:
        bye_player = unpaired[0]
        match = Match(
            player_1=bye_player,
            color_1="white",
            score_1=1.0,  # Free point
            player_2=None,
            color_2=None,
            score_2=0.0
        )
        matches.append(match)

    tournament_round.matches_list.extend(matches)
