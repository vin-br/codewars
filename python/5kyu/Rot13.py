# Solution
def rot13(message: str) -> str:
    """
    Encrypts a given string using the ROT13 cipher, which shifts
    letters by 13 positions in the alphabet. Non-letter characters
    remain unchanged.
    """
    return message.translate(
        message.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM",
        )
    )
