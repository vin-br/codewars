# Solution
def descending_order(n: int) -> int:
    """Sorts in descending order."""
    return int("".join(sorted(str(n), reverse=True)))
