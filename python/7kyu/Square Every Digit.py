# Solution 1
def square_digits_1(num: int) -> int:
    """Squares every digit of a number and concatenates them."""
    words = list(str(num))
    result, tmp = "", ""
    for word in words:
        tmp = int(word) ** 2
        result = result + str(tmp)
    return int(result)


# Solution 2
def square_digits_2(num: int) -> int:
    """Squares every digit of a number and concatenates them."""
    return int("".join(str(int(i) ** 2) for i in str(num)))
