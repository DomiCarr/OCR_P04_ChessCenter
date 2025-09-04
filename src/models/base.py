"""models/base.py"""


def compute_elo(player1_current_elo: int,
                player2_current_elo: int,
                player1_score: float,
                player2_score: float,
                k_factor: int = 20) -> tuple[int, int]:
    """
    Compute new Elo values for two players after a match.

    The Elo system updates a player's Elo based on the difference
    between the expected outcome and the actual outcome of a match.

    Formula:
        NewElo = CurrentElo + K * (ActualScore - ExpectedScore)
    where:
        - CurrentElo = current Elo of the player
        - K = factor controlling Elo change magnitude
        - ActualScore = actual score of the player (1.0 win, 0.5 draw, 0.0 loss)
        - ExpectedScore = expected score based on both players' current Elo
          ExpectedScorePlayer1 = 1 / (1 + 10^((player2_current_elo -
                                              player1_current_elo)/400))

    Parameters:
        player1_current_elo (int): Current Elo of player 1.
        player2_current_elo (int): Current Elo of player 2.
        player1_score (float): Score of player 1 (1.0 win, 0.5 draw, 0.0 loss).
        k_factor (int): Elo factor (default 20).

    Returns:
        tuple[int, int]: New Elo values (new_elo_player1, new_elo_player2)
    """
    print(f"player1_current_elo: {player1_current_elo}")
    print(f"player2_current_elo: {player2_current_elo}")
    print(f"player1_score: {player1_score}")
    print(f"player2_score: {player2_score}")
    print(f"k_factor: {k_factor}")

    # Expected scores for each player
    expected_score_player1 = 1 / (1 + 10 ** ((player2_current_elo -
                                              player1_current_elo) / 400))
    expected_score_player2 = 1 / (1 + 10 ** ((player1_current_elo -
                                              player2_current_elo) / 400))

    print(f"expected_score_player1: {expected_score_player1}")
    print(f"expected_score_player2: {expected_score_player2}")

    # Update Elo
    new_elo_player1 = int(round(player1_current_elo +
                                k_factor * (player1_score -
                                            expected_score_player1)))
    new_elo_player2 = int(round(player2_current_elo +
                                k_factor * (player2_score -
                                            expected_score_player2)))

    print(f"new_elo_player1: {new_elo_player1}")
    print(f"new_elo_player2: {new_elo_player2}")

    return new_elo_player1, new_elo_player2
