# Solution
def cakes(recipe: dict, available: dict) -> int:
    """
    Takes a recipe as a dict() and available ingredients dict().
    Returns the maximum number of cakes (integer) that can be made.
    """
    n_cakes = []
    quantity = 0

    for unique_key in recipe.keys() or available.keys():
        if unique_key in recipe.keys() and unique_key not in available.keys():
            return 0

    for key in recipe.keys() & available.keys():
        quantity = available.get(key) // recipe.get(key)
        n_cakes.append(quantity)

    return min(n_cakes)
