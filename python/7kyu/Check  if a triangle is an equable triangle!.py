# Solution
import math


def equable_triangle(a: int, b: int, c: int) -> bool:
    """Verify if a triangle is equable."""
    if a > (b + c) or b > (a + c) or c > (a + b):
        return False

    perimeter = a + b + c
    half_perimeter = perimeter / 2
    area = math.sqrt(
        half_perimeter
        * (half_perimeter - a)
        * (half_perimeter - b)
        * (half_perimeter - c)
    )
    return area == perimeter
