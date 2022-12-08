'''Description:

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''

# Solution

def cakes(recipe, available):
    n_cakes = []
    quantity = 0
    
    # Checking if an ingredient is required in the recipe but missing from the ones available
    for unique_key in recipe.keys() or available.keys():
        if unique_key in recipe.keys() and unique_key not in available.keys():
            return 0
    
    # For available ingredients needed in the recipe, we check how many cakes we can make
    # And we store that in the variable quantity, than we add it to the list of n_cakes
    for key in recipe.keys() & available.keys():
        quantity = available.get(key) // recipe.get(key) 
        n_cakes.append(quantity)
    
    # We return the lowest number of the n_cakes list that we bake
    return min(n_cakes)