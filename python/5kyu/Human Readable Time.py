# Solution 1
def make_readable_1(s: int) -> str:
    """
    Converts a non-negative integer (seconds) into a
    human-readable time format (HH:MM:SS).

    - HH: hours (00-99), padded to 2 digits.
    - MM: minutes (00-59), padded to 2 digits.
    - SS: seconds (00-59), padded to 2 digits.
    """
    remainder = s
    hour = int(remainder // (60 * 60))
    remainder = remainder % (60 * 60)
    minute = int(remainder // 60)
    second = int(remainder % 60)

    return "%02d:%02d:%02d" % (hour, minute, second)


# Solution 2
def make_readable_2(s: int) -> str:
    """
    Converts a non-negative integer (seconds) into a
    human-readable time format (HH:MM:SS).

    - HH: hours (00-99), padded to 2 digits.
    - MM: minutes (00-59), padded to 2 digits.
    - SS: seconds (00-59), padded to 2 digits.
    """
    return "{:02}:{:02}:{:02}".format(s // 3600, s // 60 % 60, s % 60)
