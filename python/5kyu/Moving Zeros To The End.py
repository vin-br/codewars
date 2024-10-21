# Solution 1
def move_zeros_1(lst: list) -> list:
    """Moves all of the zeros to the end,
    keeping the order of the other elements."""
    for number in lst:
        if number == 0:
            lst.remove(number)
            lst.append(number)
    return lst


# Solution 2
def move_zeros_2(lst: list) -> list:
    """Moves all of the zeros to the end,
    keeping the order of the other elements."""
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]
