# Solution
import numpy as np


def solution(array_a: list, array_b: list) -> int:
    """
    Calculates the average of the squared absolute differences
    between corresponding elements in two integer arrays of
    equal length. For each pair of elements, compute the
    square of the absolute difference and return the average.
    """
    if len(array_a) == len(array_b):
        array_c = abs(np.array(array_a) - np.array(array_b))
        square_array = np.square(array_c)
        return np.sum(square_array) / len(array_c)
    else:
        return 0
