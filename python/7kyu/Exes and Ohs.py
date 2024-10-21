# Solution
def xo(s: str) -> bool:
    """Verifies if the string has an equal number of 'x' and 'o' characters"""
    if s.count("x") + s.count("X") == s.count("o") + s.count("O"):
        return True
    else:
        return False
