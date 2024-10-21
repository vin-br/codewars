def to_alternating_case(s: str) -> str:
    """Changes the casing of each letter in a string."""
    return "".join(
        letter.lower() if letter == letter.upper() else letter.upper() for letter in s
    )
