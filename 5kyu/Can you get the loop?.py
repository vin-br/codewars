"""
Description:

You are given a node that is the beginning of a linked list. 
This list contains a dangling piece and a loop. 
Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 
and the loop size is 12.

# Use the `next' attribute to get the following node
node.next

Notes:

    do NOT mutate the nodes!
    in some cases there may be only a loop, with no dangling piece

    Thanks to shadchnev, I broke all of the methods from the Hash class.

    Don't miss dmitry's article in the discussion after you pass the Kata !!
"""


# Solution
def loop_size(node):
    turtle = node.next
    rabbit = node.next.next

    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    distance = 1
    rabbit = rabbit.next

    while turtle != rabbit:
        rabbit = rabbit.next
        distance += 1

    return distance
