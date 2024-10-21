# Solution
def friend(name: list) -> list:
    """
    Filter a list of names and return only those with exactly
    4 characters, maintaining their original order.
    """
    return [n for n in name if len(n) == 4]
