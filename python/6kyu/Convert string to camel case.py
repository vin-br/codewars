# Solution 1
import re


def to_camel_case_1(text: str) -> str:
    """
    Convert dash/underscore delimited words into camel case.
    The first word is capitalized if it was originally
    capitalized. Subsequent words are always capitalized.
    """
    modified_str = re.sub("[-]", "_", text).split("_")
    return modified_str[0] + "".join(i.capitalize() for i in modified_str[1:])


# Solution 2
def to_camel_case_2(text: str) -> str:
    """
    Convert dash/underscore delimited words into camel case.
    The first word is capitalized if it was originally
    capitalized. Subsequent words are always capitalized.
    """
    return text[:1] + text.title()[1:].replace("_", "").replace("-", "")
