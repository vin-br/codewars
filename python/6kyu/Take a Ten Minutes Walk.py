# Solution 1
def is_valid_walk_1(walk: list) -> bool:
    """
    Checks if the given walk takes exactly 10 minutes and returns to
    the starting point. Each direction is represented by a one-letter
    string (e.g., 'n', 's', 'e', 'w'). A valid walk must consist of
    10 steps and equal north-south and east-west movements.
    """
    return (
        True
        if len(walk) == 10
        and walk.count("n") == walk.count("s")
        and walk.count("e") == walk.count("w")
        else False
    )


# Solution 2
def is_valid_walk_2(walk: list) -> bool:
    """
    Checks if the given walk takes exactly 10 minutes and returns to
    the starting point. Each direction is represented by a one-letter
    string (e.g., 'n', 's', 'e', 'w'). A valid walk must consist of
    10 steps and equal north-south and east-west movements.
    """
    return (
        len(walk) == 10
        and walk.count("n") == walk.count("s")
        and walk.count("e") == walk.count("w")
    )
