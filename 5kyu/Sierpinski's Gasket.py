# Description:

# Write a function that takes an integer n and returns the nth iteration of the fractal known as Sierpinski's Gasket.

# Here are the first few iterations. The fractal is composed entirely of L and white-space characters; each character has one space between it and the next (or a newline).
# 0

# L

# 1

# L
# L L

# 2

# L
# L L
# L   L
# L L L L

# 3

# L
# L L
# L   L
# L L L L
# L       L
# L L     L L
# L   L   L   L
# L L L L L L L L


def sierpinski(n):
    res = "L\n"
    l = [1]
    n = 2 ** n - 1
    for _ in range(n):
        nl = [1] + [l[j] + l[j - 1] for j in range(1, len(l))] + [1]
        l = nl
        res += " ".join("L" if i % 2 == 1 else " " for i in nl) + "\n"

    return res.strip()