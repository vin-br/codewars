# Solution
def zeros(n: int) -> int:
    """
    Calculates the number of trailing zeros in a factorial of a given number.
    """
    count = 0
    power_of_5 = 5
    while n // power_of_5 > 0:
        count += n // power_of_5
        power_of_5 *= 5
    return count
