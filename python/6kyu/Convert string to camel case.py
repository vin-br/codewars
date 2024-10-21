"""
Description

Complete the method/function so that it converts dash/underscore delimited words
into camel casing. The first word within the output should be capitalized only if
the original word was capitalized (known as Upper Camel Case, 
also often referred to as Pascal case). The next words should be always capitalized.

Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

# Solution 1
import re


def to_camel_case(text):
    modified_text = re.sub("[-]", "_", text).split("_")
    return modified_text[0] + "".join(i.capitalize() for i in modified_text[1:])


# Solution 2
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace("_", "").replace("-", "")
