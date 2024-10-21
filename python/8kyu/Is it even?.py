# Solution
def is_even(n: int) -> bool:
    """
    Check if a number n is even.

    Returns True if n is an even integer, False otherwise.
    Floats with a non-zero decimal part are considered UNeven.
    """
    return n % 2 == 0
