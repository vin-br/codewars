# Solution
def bouncing_ball(h, bounce, window):
    """
    Calculates how many times a ball dropped from a height h bounces
    past a window located at a height of 'window' meters.
    """
    if not (h >= 0 and (bounce >= 0 and bounce < 1) and window < h):
        return -1
    else:
        return 1 if h < window else 2 + bouncing_ball((h * bounce), bounce, window)
