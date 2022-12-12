"""
Description

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

# Solution
def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter == "a":
            count += 1
        elif letter == "e":
            count += 1
        elif letter == "i":
            count += 1
        elif letter == "o":
            count += 1
        elif letter == "u":
            count += 1
        else:
            pass
    return count
