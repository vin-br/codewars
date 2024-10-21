def find_short(s: str) -> int:
    """Returns the length of the shortest word of a string."""
    return min(len(word) for word in s.split())
