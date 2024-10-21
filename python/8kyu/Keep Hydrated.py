# Solution
import math


def litres(time: float) -> int:
    """Calculate the amount of water in litres drank based on cycling time
    in hours : 0.5 litres per hour, rounded down to the nearest whole number.
    """
    water = time * 0.5
    return math.trunc(water)
