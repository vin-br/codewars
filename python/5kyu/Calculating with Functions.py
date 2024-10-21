"""
Create functions for numbers 0 to 9 and for operations
plus, minus, times, and divided_by. Each function should
allow performing calculations where the outer function
represents the left operand and the inner function
represents the right operand. The result of division
should be an integer.
"""


# Solution
def zero(number=""):
    if number == "":
        return "0"
    else:
        return eval("0" + number)


def one(number=""):
    if number == "":
        return "1"
    else:
        return eval("1" + number)


def two(number=""):
    if number == "":
        return "2"
    else:
        return eval("2" + number)


def three(number=""):
    if number == "":
        return "3"
    else:
        return eval("3" + number)


def four(number=""):
    if number == "":
        return "4"
    else:
        return eval("4" + number)


def five(number=""):
    if number == "":
        return "5"
    else:
        return eval("5" + number)


def six(number=""):
    if number == "":
        return "6"
    else:
        return eval("6" + number)


def seven(number=""):
    if number == "":
        return "7"
    else:
        return eval("7" + number)


def eight(number=""):
    if number == "":
        return "8"
    else:
        return eval("8" + number)


def nine(number=""):
    if number == "":
        return "9"
    else:
        return eval("9" + number)


def plus(number):
    number.replace("plus", "+")
    return f" + {number}"


def minus(number):
    number.replace("minus", "-")
    return f" - {number}"


def times(number):
    number.replace("times", "*")
    return f" * {number}"


def divided_by(number):
    number.replace("divided_by", "//")
    return f" // {number}"
