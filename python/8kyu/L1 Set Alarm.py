# Solution
def set_alarm(employed: bool, vacation: bool) -> bool:
    """
    Determines if an alarm should be set based on employment status
    and vacation status. Returns True if employed and not on vacation;
    otherwise, returns False.
    """
    if employed is True and vacation is False:
        return True
    else:
        return False
