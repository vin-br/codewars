# Solution
def find_uniq(arr: list) -> float:
    """
    Given an array of numbers where all but one are the same,
    return the unique number.
    """
    return [n for n in set(arr) if arr.count(n) == 1][0]
