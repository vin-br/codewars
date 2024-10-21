# Solution
def product_fib(prod: int) -> int:
    """
    Given an integer prod, find two consecutive Fibonacci
    numbers F(n) and F(n+1) such that F(n) * F(n+1) = prod.
    Return a tuple [F(n), F(n+1), True] if found, or
    [F(n), F(n+1), False] if the product is not equal but
    the next product is greater than prod.
    """
    fib1, fib2 = 0, 1
    while prod > fib1 * fib2:
        fib1, fib2 = fib2, fib1 + fib2
    return [fib1, fib2, prod == fib1 * fib2]
