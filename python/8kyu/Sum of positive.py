# Solution 1
import numpy as np


def positive_sum_1(array: list) -> int:
    """Returns the sum of all positive numbers."""
    arr = np.array(array)
    arr[arr < 0] = 0
    return sum(arr)


# Solution 2
def positive_sum_2(array: list) -> int:
    """Returns the sum of all positive numbers."""
    return sum(i for i in array if i > 0)
