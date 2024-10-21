# Solution
def are_you_playing_banjo(name: str) -> str:
    """
    Check if the given name starts with 'R' or 'r'.
    If it does, return '{name} plays banjo'.
    Otherwise, return '{name} does not play banjo'.
    """
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
