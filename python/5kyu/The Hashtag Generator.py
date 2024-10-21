# Solution
def generate_hashtag(s: str) -> str:
    """
    Generates a hashtag from a given string by capitalizing the
    first letter of each word and ensuring it starts with '#'.
    Returns false if the input is empty or if the final
    hashtag exceeds 140 characters.
    """
    if len(s) == 0 or len(s) > 140:
        return False

    return "#" + "".join(w.capitalize() for w in s.split())
