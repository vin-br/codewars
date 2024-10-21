# Solution 1
def is_triangle_1(a: int, b: int, c: int) -> bool:
    """
    Checks if the integers can represent the lengths of the sides of a triangle
    """
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        return False
    else:
        return True


# Solution 2
def is_triangle(a: int, b: int, c: int) -> bool:
    """
    Checks if the integers can represent the lengths of the sides of a triangle
    """
    return (a < b + c) and (b < a + c) and (c < a + b)
