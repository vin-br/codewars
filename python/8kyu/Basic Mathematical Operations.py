# Solution
def basic_op(operator, value1, value2):
    """
    Perform basic arithmetic operations.

    This function takes an operation as a string/character and two numbers,
    and returns the result of applying the operation on the two numbers.

    Example:
    - ('+', 4, 7) returns 11
    - ('-', 15, 18) returns -3
    """
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
