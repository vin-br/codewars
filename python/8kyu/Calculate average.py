# Solution 1
import numpy as np


def find_average_1(numbers: list):
    """Calculates the average of a list of numbers.

    Returns 0 for empty lists.
    """
    return np.mean(numbers)


# Solution 2
def find_average_2(numbers: list):
    """Calculates the average of a list of numbers.

    Returns 0 for empty lists.
    """
    return sum(numbers) / len(numbers) if numbers else 0
