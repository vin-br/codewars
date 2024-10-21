# Solution
def duplicate_encode(word: str) -> str:
    """
    Converts a string to a new string where each character is replaced by
    "(" if it appears only once, or ")" if it appears more than once.
    """
    word = word.lower()
    signles = {c for c in word if word.count(c) == 1}
    return "".join("(" if c in signles else ")" for c in word)
