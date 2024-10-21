# Solution
def valid_parentheses(s: str) -> True:
    """
    Determines if the order of parentheses in the input string is valid.
    Returns True if valid, otherwise False.

    Constraints:
    - Length of input string is between 0 and 100.
    - Input may include any ASCII characters and can be empty.
    - Only () are considered as parentheses.
    """
    # Removing all characters between parentheses in the string
    s = "".join(c for c in s if c in "()")

    # Replacing sets of two parentheses by nothing at all
    while "()" in s:
        s = s.replace("()", "")

    # Returning True if the string is empty, else it's false
    return True if s == "" else False
