# Solution
def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    """Sums a sequence of integers defined by 3 non-negative values."""
    return sum([i for i in range(begin_number, end_number + 1, step)])
