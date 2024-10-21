# Solution
def paperwork(n: int, m: int) -> int:
    """
    Calculate the total number of blank pages needed
    for n classmates with m pages of paperwork. If n or
    m is negative, return 0. Example:
    n=5, m=5 returns 25; n=-5, m=5 returns 0.
    """
    if n < 0 or m < 0:
        return 0
    else:
        return n * m
