# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

# Requirements:

#     There must be a function for each number from 0 ("zero") to 9 ("nine")
#     There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
#     Each calculation consist of exactly one operation and two numbers
#     The most outer function represents the left operand, the most inner function represents the right operand
#     Division should be integer division. For example, this should return 2, not 2.666666...:

# eight(divided_by(three()))


# Solution
def zero(number=''): 
    if number == "":
        return "0"
    else :
        return eval("0" + number)
    
def one(number=''):
    if number == "":
        return "1"
    else :
        return eval("1" + number)
    
def two(number=''):
    if number == "":
        return "2"
    else :
        return eval("2" + number)
    
def three(number=''):
    if number == "":
        return "3"
    else :
        return eval("3" + number)
    
def four(number=''):
    if number == "":
        return "4"
    else :
        return eval("4" + number)
        
def five(number=''):
    if number == "":
        return "5"
    else :
        return eval("5" + number)
    
def six(number=''):
    if number == "":
        return "6"
    else :
        return eval("6" + number)
        
def seven(number=''):
    if number == "":
        return "7"
    else :
        return eval("7" + number)
    
def eight(number=''):
    if number == "":
        return "8"
    else :
        return eval("8" + number)
    
def nine(number=''):
    if number == "":
        return "9"
    else :
        return eval("9" + number)

def plus(number):
    number.replace("plus", "+")
    return f' + {number}'

def minus(number):
    number.replace("minus", "-")
    return f' - {number}'
        
def times(number):
    number.replace("times", "*")
    return f' * {number}'

def divided_by(number):
    number.replace("divided_by", "//")
    return f' // {number}'