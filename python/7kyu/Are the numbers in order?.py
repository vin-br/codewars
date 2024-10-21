# Solution 1
def in_asc_order_1(arr: list) -> bool:
    """
    Check if the given array of integers is in ascending order.
    An array is considered to be in ascending order if each element is less
    than or equal to the next.

    Arrays with 0 or 1 element are considered sorted.
    """
    if len(arr) == 0 or len(arr) == 1:
        return True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False

    return True


# Solution 2
def in_asc_order_2(arr: list) -> bool:
    """
    Check if the given array of integers is in ascending order.
    An array is considered to be in ascending order if each element is less
    than or equal to the next.

    Arrays with 0 or 1 element are considered sorted.
    """
    return arr == sorted(arr)
