# Solution
def flip(direction: str, lst: list) -> list:
    """
    Takes the direction and the initial column heights.
    Returns the new arrangement of cubes after switching gravity.
    """
    return sorted(lst) if direction == "R" else sorted(lst, reverse=True)
