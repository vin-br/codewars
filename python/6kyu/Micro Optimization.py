# Solution
def digit_sum(n: int) -> int:
    """Calculates the sum of all the digits of a non-negative integer."""
    return sum([int(elem) for elem in str(n)])
