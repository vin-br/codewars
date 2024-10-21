# Solution 1
def fake_bin_1(x: str) -> str:
    """
    Replace digits in a string: '0' for digits < 5,
    '1' for digits >= 5. The input string is never empty.
    """
    return (
        x.replace("1", "0")
        .replace("2", "0")
        .replace("3", "0")
        .replace("4", "0")
        .replace("5", "1")
        .replace("6", "1")
        .replace("7", "1")
        .replace("8", "1")
        .replace("9", "1")
    )


# Solution 2
def fake_bin_2(s: str) -> str:
    """
    Replace digits in a string: '0' for digits < 5,
    '1' for digits >= 5. The input string is never empty.
    """
    return s.translate(s.maketrans("0123456789", "0000011111"))
