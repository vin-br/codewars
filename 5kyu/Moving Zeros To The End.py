# Description:

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


# Solution 1
def move_zeros(lst):
    for number in lst :
        if number == 0:
            lst.remove(number)
            lst.append(number)
    return lst

# Solution 2
def move_zeros(lst):
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]