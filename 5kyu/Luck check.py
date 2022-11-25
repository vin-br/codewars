# Description:

# In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:

# 003111    #             3 = 1 + 1 + 1
# 813372    #     8 + 1 + 3 = 3 + 7 + 2
# 17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
# 56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6

# Such tickets were either eaten after being used or collected for bragging rights.

# Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal representation of a lucky ticket number, or false/False for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.

# Solution
def luck_check(s):
    if s.isdigit() != True: RaiseError
    else:
        new_s = [*s]
        digits = [int(i) for i in new_s if i.isdigit()]
        digits_len = len(digits)
        half_len = digits_len // 2
        sum1, sum2 = 0, 0
        
        if digits_len % 2 == 0:
            sum1, sum2 = sum(digits[:half_len]), sum(digits[half_len:])
        else : 
            sum1, sum2 = sum(digits[:half_len]), sum(digits[half_len+1:])

        return sum1 == sum2