# Solution
def sierpinski(n):
    """Generates the nth iteration of Sierpinski's Gasket fractal.

    The fractal consists of 'L' and whitespace characters. Each
    character is separated by a space. The first few iterations
    are as follows:

    Iteration 0:   L
    Iteration 1:   L
                   L L
    Iteration 2:   L
                   L L
                   L   L
                   L L L L
    Iteration 3:   L
                   L L
                   L   L
                   L L L L
                   L       L
                   L L     L L
                   L   L   L   L
                   L L L L L L L L
    """
    res = "L\n"
    l = [1]
    n = 2**n - 1
    for _ in range(n):
        nl = [1] + [l[j] + l[j - 1] for j in range(1, len(l))] + [1]
        l = nl
        res += " ".join("L" if i % 2 == 1 else " " for i in nl) + "\n"

    return res.strip()
