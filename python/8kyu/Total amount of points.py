# Solution
def points(games):
    """
    Calculates the total points for a football team based on match results.
    """
    score = 0
    return sum(
        score + 3 if g[0] > g[2] else (score + 1 if g[0] == g[2] else score)
        for g in games
    )
