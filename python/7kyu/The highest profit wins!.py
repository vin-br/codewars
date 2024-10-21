# Solution 1
def min_max_1(lst: list) -> list:
    """Given a list of numbers, return a list containing the
    minimum and maximum values from the input list."""
    lst = min(lst), max(lst)
    return list(lst)


# Solution 2
def min_max_2(lst: list) -> list:
    """Given a list of numbers, return a list containing the
    minimum and maximum values from the input list."""
    return [min(lst), max(lst)]
