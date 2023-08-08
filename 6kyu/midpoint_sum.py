def midpoint_sum(ints):
    """
    # https://www.codewars.com/kata/54d3bb4dfc75996c1c000c6d
    # Midpoint Sum
    """
    for i in range(1, len(ints) - 1):
        if sum(ints[:i]) == sum(ints[i+1:]):
            print(sum(ints[:i]), sum(ints[i+1:]))
            return i
