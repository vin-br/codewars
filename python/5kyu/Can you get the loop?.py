# Solution
def loop_size(node):
    """
    Calculates the length of the loop in a linked list.
    Returns the length of the loop.
    """
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
