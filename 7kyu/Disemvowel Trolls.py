# Description:

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

# Solution 1
import re

def disemvowel(s):
    new_s = re.sub('[aeiouAEIOU]', '', s)
    return new_s

# Solution 2
def disemvowel(string_):
    return ''.join(s for s in string_ if s not in "AaEeIiOoUu")