# Solution
def powers_of_two(n: int) -> list:
    """Returns a list of all the powers of 2 with the exponent from 0 to n."""
    return [2**i for i in range(n + 1)]
