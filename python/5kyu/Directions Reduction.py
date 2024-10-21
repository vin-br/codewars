# Solution 1
def dirReduc_1(directions):
    """
    Simplifies a series of directional movements.

    Given a list of directions ("NORTH", "SOUTH", "EAST", "WEST"),
    the function removes any unnecessary movements that
    directly cancel each other out.

    The output is a reduced list of directions.
    """
    i = 0
    while i < len(directions) - 1 and len(directions) > 1:
        if (
            directions[i] == "NORTH"
            and directions[i + 1] == "SOUTH"
            or directions[i] == "SOUTH"
            and directions[i + 1] == "NORTH"
            or directions[i] == "WEST"
            and directions[i + 1] == "EAST"
            or directions[i] == "EAST"
            and directions[i + 1] == "WEST"
        ):
            directions.pop(i)
            directions.pop(i)
            i = 0
        else:
            i += 1

    return directions


# Solution 2
opposite = {"NORTH": "SOUTH", "EAST": "WEST", "SOUTH": "NORTH", "WEST": "EAST"}


def dirReduc_2(plan):
    """
    Simplifies a series of directional movements.

    Given a list of directions ("NORTH", "SOUTH", "EAST", "WEST"),
    the function removes any unnecessary movements that
    directly cancel each other out.

    The output is a reduced list of directions.
    """
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
