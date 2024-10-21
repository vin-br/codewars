# Solution
def invert(lst: list) -> list:
    """
    Returns the opposite value.
    Each positive becomes negatives, and the negatives become positives.
    """
    return [n * -1 for n in lst]
