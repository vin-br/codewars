# Solution
def count_sheep(n: int) -> str:
    """
    Generates a string that counts sheep for sleep.
    """
    return "" if n == 0 else "".join(f"{i + 1} sheep..." for i in range(n))
