"""
Description

You are given an array (which will have a length of at least 3, but could be very large)
containing integers. The array is either entirely comprised of odd integers or entirely
comprised of even integers except for a single integer N. 

Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

# Solution 1
def find_outlier(integers):
    if len(integers) == 0:
        return 0
    else:
        pair_integers, odd_integers = [], []
        for n in integers:
            if n % 2 == 0:
                pair_integers.append(n)
            elif n % 2 == 1:
                odd_integers.append(n)
        if len(pair_integers) > 1:
            return odd_integers[0]
        elif len(odd_integers) > 1:
            return pair_integers[0]


# Solution 2
def find_outlier(integers):
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
def find_outlier(integers):
    evens = [x for x in integers if x % 2 == 0]
    odds = [x for x in integers if x % 2 == 1]
    return evens[0] if len(evens) == 1 else odds[0]
