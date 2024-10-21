# Solution
def get_grade(s1: int, s2: int, s3: int) -> str:
    """
    Calculate the average of three scores and return the letter grade.
    Assumes input scores are valid and within the range [0, 100].
    """
    score = (s1 + s2 + s3) / 3
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
