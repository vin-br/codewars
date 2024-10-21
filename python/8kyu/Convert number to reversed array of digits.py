def digitize(n: int) -> list:
    """Returns the digits of a number within an array in reverse order."""
    n = str(n)
    return [int(i) for i in n[::-1]]
