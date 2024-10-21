# Solution 1
def find_outlier(integers_list: list) -> int:
    """
    Identifies the single outlier in an array of integers where the majority
    are either odd or even.
    """
    if len(integers_list) == 0:
        return 0
    else:
        pair_integers, odd_integers = [], []
        for n in integers_list:
            if n % 2 == 0:
                pair_integers.append(n)
            elif n % 2 == 1:
                odd_integers.append(n)
        if len(pair_integers) > 1:
            return odd_integers[0]
        elif len(odd_integers) > 1:
            return pair_integers[0]


# Solution 2
def find_outlier_2(integers: list) -> int:
    """
    Identifies the single outlier in an array of integers where the majority
    are either odd or even.
    """
    evens = []
    odds = []
    for n in integers:
        if n % 2 == 0:
            if len(odds) > 1:
                return n
            evens.append(n)
            if len(evens) > 1 and len(odds) == 1:
                return odds.pop()
        else:
            if len(evens) > 1:
                return n
            odds.append(n)
            if len(odds) > 1 and len(evens) == 1:
                return evens.pop()


# Solution 3
def find_outlier_3(integers: list) -> int:
    """
    Identifies the single outlier in an array of integers where the majority
    are either odd or even.
    """
    evens = [x for x in integers if x % 2 == 0]
    odds = [x for x in integers if x % 2 == 1]
    return evens[0] if len(evens) == 1 else odds[0]
