# Solution 1
def high_and_low_1(numbers: str) -> str:
    """
    Takes a string of space-separated numbers.
    Returns a string with the highest and lowest numbers.
    """
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))


# Solution 2
def high_and_low_2(numbers: str) -> str:
    """
    Takes a string of space-separated numbers.
    Returns a string with the highest and lowest numbers.
    """
    s_n = ""
    i = 0
    c = ""
    while c != " " and i < len(numbers):
        c = numbers[i]
        s_n += c
        i += 1

    min, max = int(s_n), int(s_n)
    s_n = ""
    # "-3 22 1"
    for k in range(i, len(numbers)):
        c = numbers[k]
        if k + 1 >= len(numbers):
            end_c = True
        elif numbers[k + 1] == " ":
            end_c = True
        else:
            end_c = False

        if end_c:
            s_n += c

            n = int(s_n)
            if n > max:
                max = n
            if n < min:
                min = n
            s_n = ""
        elif c != " ":
            s_n += c

    return str(max) + " " + str(min)
