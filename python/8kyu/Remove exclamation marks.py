# Solution
def remove_exclamation_marks(text: str) -> str:
    """Removes all exclamation marks from a string."""
    return "".join(s for s in text if s not in "!")
