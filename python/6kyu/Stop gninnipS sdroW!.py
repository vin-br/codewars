# Solution
def spin_words(sentence: str) -> str:
    """
    Given a string of one or more words, return the same string
    with words of five or more letters reversed. Only letters
    and spaces will be present, and spaces appear only when
    there are multiple words.
    """
    return " ".join(
        [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    )
