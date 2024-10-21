# Solution
def luck_check(s: str) -> bool:
    """
    Checks if a given string represents a lucky ticket number.
    Returns True if the sum of the left half of the digits equals the sum
    of the right half, ignoring the middle digit for odd-length strings.
    Raises errors for empty strings or invalid decimal inputs.
    """
    if s.isdigit() is not True:
        raise ValueError
    else:
        new_s = [*s]
        digits = [int(i) for i in new_s if i.isdigit()]
        digits_len = len(digits)
        half_len = digits_len // 2
        sum1, sum2 = 0, 0

        if digits_len % 2 == 0:
            sum1, sum2 = sum(digits[:half_len]), sum(digits[half_len:])
        else:
            sum1, sum2 = sum(digits[:half_len]), sum(digits[half_len + 1 :])

        return sum1 == sum2
