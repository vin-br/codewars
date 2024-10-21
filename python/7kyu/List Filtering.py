# Solution
def filter_list(lst: list) -> list:
    """Returns a list with the strings filtered out."""
    return [n for n in lst if type(n) is int]
