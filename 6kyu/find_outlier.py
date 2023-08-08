
def find_outlier(integers):
    """
    # https://www.codewars.com/kata/5526fc09a1bbd946250002dc
    # Find The Parity Outlier
    """
    evens = []
    odds = []

    for i in integers:
        if i % 2 > 0:
            odds.append(i)
        else:
            evens.append(i)

    if len(evens) < len(odds):
        return evens[0]
    else:
        return odds[0]
    