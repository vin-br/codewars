# Solution
def quarter_of(month: int) -> int:
    """Return the quarter of the year for a given month (1-12)."""
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4
