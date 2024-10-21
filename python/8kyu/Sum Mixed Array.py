# Solution
def sum_mix(lst: list) -> int:
    """Sums the values of the array as if all were numbers."""
    return sum([int(n) for n in lst])
