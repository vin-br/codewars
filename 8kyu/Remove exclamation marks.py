"""
Description

Write function RemoveExclamationMarks which removes all exclamation marks from a string
"""

# Solution
def remove_exclamation_marks(text):
    return "".join(s for s in text if s not in "!")
