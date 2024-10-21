# Solution
def get_count(sentence: str) -> int:
    """Counts the number of vowels in a string."""
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
