# Solution 1
import re


def disemvowel_1(s: str) -> str:
    """Removes Vowels from a string."""
    new_s = re.sub("[aeiouAEIOU]", "", s)
    return new_s


# Solution 2
def disemvowel_2(text: str) -> str:
    """Removes Vowels from a string."""
    return "".join(s for s in text if s not in "AaEeIiOoUu")
