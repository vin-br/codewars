# Solution 1
def remove_smallest_1(lst: list) -> list:
    """Returns a new list with the smallest value removed."""
    return [elem for indx, elem in enumerate(lst) if indx != lst.index(min(lst))]


# Solution 2
def remove_smallest_2(lst: list) -> list:
    """Returns a new list with the smallest value removed."""
    return [elem for n, elem in enumerate(lst) if n != lst.index(min(lst))]
