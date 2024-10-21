# Solution
def is_isogram(word: str) -> bool:
    """Checks if a string is an isogram (no repeating letters)."""
    return len(word) == len(set(word.lower()))
