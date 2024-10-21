# Solution
def unique_in_order(s: str) -> list:
    """
    Returns a list of items without any elements with the same value
    next to each other and preserving the original order of elements.
    """
    lst = list(s)
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i - 1]]
