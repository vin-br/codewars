# Description:

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes

#     All numbers are valid Int32, no need to validate them.
#     There will always be at least one number in the input string.
#     Output string must be two numbers separated by a single space, and highest number is first.


# Solution 1
def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

# Solution 2
def high_and_low(numbers):
    print(numbers)
    s_n = ""
    i = 0
    c = ""
    while c != " " and i < len(numbers):
        c = numbers[i]
        s_n += c
        i += 1
    
    min, max = int(s_n), int(s_n)
    s_n = ""
    # "-3 22 1"
    for k in range(i, len(numbers)):
        c = numbers[k]
        if k + 1 >= len(numbers):
            end_c = True
        elif numbers[k+1] == " ":
            end_c = True
        else:
            end_c = False
        
        if end_c:
            s_n += c
            
            n = int(s_n)
            if n > max:
                max = n
            if n < min:
                min = n
            s_n = ""
        elif c != " ":
            s_n += c
    
    return str(max) + " " + str(min)