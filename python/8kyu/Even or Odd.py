# Solution 1
def even_or_odd_1(number: int) -> str:
    """Return 'Even' for even numbers and 'Odd' for odd numbers."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Solution 2
def even_or_odd_2(number: int) -> str:
    """Return 'Even' for even numbers and 'Odd' for odd numbers."""
    return "Even" if number % 2 == 0 else "Odd"
