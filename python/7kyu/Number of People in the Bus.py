def number(bus_stops: list) -> int:
    """Calculates the number of people left on a bus after the last stop."""
    return sum(people_on - people_off for people_on, people_off in bus_stops)
