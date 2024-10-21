"""
Description

Your goal is to create a function that removes the first and last characters of
a string. You're given one parameter, the original string. You don't have to worry
with strings with less than two characters.
"""

# Solution
def remove_char(s):
    s = s[1:-1]
    return s
