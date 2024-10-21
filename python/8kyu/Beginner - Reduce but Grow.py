# Solution
def grow(lst: list) -> int:
    """Multiplies the values together in order."""
    t = 1
    for n in lst:
        t *= n
    return t
