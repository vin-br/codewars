# Solution
def final_grade(exam: int, projects: int) -> int:
    """Calculates a student's final grade based on exam score
    and number of completed projects."""

    if exam > 90 or projects > 10:
        final_grade = 100
    elif exam > 75 and projects >= 5:
        final_grade = 90
    elif exam > 50 and projects >= 2:
        final_grade = 75
    else:
        final_grade = 0
    return final_grade
