# Solution 1
def digital_root_1(number):
    """
    Calculates the digital root of a non-negative integer n.

    The digital root is the iterative process of summing the digits
    until a single-digit result is obtained.
    """
    return (
        number
        if number < 10
        else digital_root_1(sum([int(digit) for digit in str(number)]))
    )


# Solution 2
def digital_root_2(n):
    """
    Calculates the digital root of a non-negative integer n.

    The digital root is the iterative process of summing the digits
    until a single-digit result is obtained.
    """
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10

        if n == 0 and res > 9:
            n = res
            res = 0

    return res + n
