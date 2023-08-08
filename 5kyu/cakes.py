def cakes(recipe, available):
    """
    # https://www.codewars.com/kata/525c65e51bf619685c000059
    # Pete, the baker
    """
    total = []
    for k,v in recipe.items():
        if k not in available.keys():
            return 0
    for k,v in recipe.items():
        total.append(int(available[k] / v))
    return min(total)
