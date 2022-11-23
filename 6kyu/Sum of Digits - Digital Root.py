# Description:

# Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
# Examples

#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


# Solution 1
def digital_root(number):
    return number if number < 10 else digital_root(sum([int(digit) for digit in str(number)]))

# Solution 2
def digital_root(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
        
        if n == 0 and res > 9:
            n = res
            res = 0
            
    return res + n