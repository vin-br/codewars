# Solution
def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    """Determine if a car can reach the nearest fuel pump."""
    return True if mpg * fuel_left >= distance_to_pump else False
