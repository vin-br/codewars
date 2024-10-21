# Solution
from math import sqrt


def is_square(n: int) -> bool:
    """Determines if a given integer is a perfect square."""
    return n >= 0 and sqrt(n) % 1 == 0
