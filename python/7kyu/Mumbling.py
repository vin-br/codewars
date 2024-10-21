# Solution
def accum(text: str) -> str:
    """
    Generates a string where each letter in the input string is repeated
    according to its position and formatted with uppercase for the first
    occurrence and lowercase for the others, separated by dashes.
    """
    return "-".join([text[l].upper() + (text[l].lower() * l) for l in range(len(text))])
