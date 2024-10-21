# Solution
def find_it(seq: list) -> list:
    """
    Returns the integer that appears an odd number of times.
    """
    return [n for n in set(seq) if seq.count(n) % 2 != 0][0]
