# Solution
def to_jaden_case(text: str) -> str:
    """
    Convert a given string to Jaden Smith's style of
    capitalization where every word is capitalized.
    """
    return " ".join([word.capitalize() for word in text.split()])
