# Description:

# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

# Solution 1
import numpy as np

def positive_sum(array):
    arr = np.array(array)
    arr[arr < 0] = 0
    return sum(arr)

# Solution 2
def positive_sum(array):
    return sum(i for i in array if i > 0)