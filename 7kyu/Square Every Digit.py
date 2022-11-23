# Description:

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

# Solution 1
def square_digits(num):
    words = list(str(num))
    result, tmp = '', ''
    for word in words:
        tmp = (int(word)**2)
        result = result + str(tmp)
    return int(result)

# Solution 2
def square_digits(num):
    return int(''.join(str(int(i) ** 2) for i in str(num)))