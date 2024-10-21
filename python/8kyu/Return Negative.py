# Solution
def make_negative(number: int) -> int:
    """Returns the negative version of the given number.
    If it is already negative or zero, returns it unchanged."""
    return (number * -1) if number >= 0 else number
