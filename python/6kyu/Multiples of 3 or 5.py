# Solution
def solution(n: int) -> int:
    """
    Returns the sum of all multiples of 3 or 5 below n.
    If n is negative, return 0. Count multiples of both 3 and 5 only once.
    """
    if n <= 0:
        return 0

    return sum(x for x in range(1, n) if x % 3 == 0 or x % 5 == 0)
