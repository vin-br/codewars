# Solution 1
def likes_1(names: list) -> str:
    """
    Generates a like message based on the number of people who liked an item.

    Given a list of names, returns a formatted string indicating how many
    people liked the item. The output varies based on the number of names.
    """
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


# Solution 2
def likes_2(names: list) -> str:
    """
    Generates a like message based on the number of people who liked an item.

    Given a list of names, returns a formatted string indicating how many
    people liked the item. The output varies based on the number of names.
    """
    match names:
        case []:
            return "no one likes this"
        case [a]:
            return f"{a} likes this"
        case [a, b]:
            return f"{a} and {b} like this"
        case [a, b, c]:
            return f"{a}, {b} and {c} like this"
        case [a, b, *rest]:
            return f"{a}, {b} and {len(rest)} others like this"
