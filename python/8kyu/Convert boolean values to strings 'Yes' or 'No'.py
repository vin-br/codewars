# Solution
def bool_to_word(boolean: bool) -> str:
    """
    Convert a boolean value to a string.
    Returns "Yes" for True and "No" for False.
    """
    if boolean is True:
        return "Yes"
    else:
        return "No"
