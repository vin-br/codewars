# Solution
def count_smileys(arr: list) -> int:
    """
    Counts the number of valid smiling faces:
    - Eyes marked by ':' or ';'
    - An optional nose represented by '-' or '~'
    - A mouth marked by ')' or 'D'
    Returns 0 if the array is empty.
    """
    smileys = {
        ":)",
        ":-)",
        ":~)",
        ";)",
        ";-)",
        ";~)",
        ":D",
        ":-D",
        ":~D",
        ";D",
        ";-D",
        ";~D",
    }

    count = 0

    for element in arr:
        if element in smileys:
            count = count + 1

    return count
