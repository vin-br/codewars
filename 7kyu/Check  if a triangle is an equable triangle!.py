# Description:

# A triangle is called an equable triangle if its area equals its perimeter. Return true, if it is an equable triangle, else return false. You will be provided with the length of sides of the triangle. Happy Coding!


import math

def equable_triangle(a,b,c):
    if a > (b + c) or b > (a + c) or c > (a + b):
        return False
    
    perimeter = a + b + c
    half_perimeter = perimeter / 2    
    area = math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))
    return area == perimeter