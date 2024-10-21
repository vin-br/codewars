# Solution
def array_diff(a: list, b: list) -> list:
    """Removes all elements in list a that are present in list b."""
    return [c for c in a if c not in b]
