"""
Description

Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""

# Solution 1
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


# Solution 2
import numpy as np


def find_average(numbers):
    return np.mean(numbers)
