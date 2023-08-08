def array_diff(a, b):
    """
    # https://www.codewars.com/kata/523f5d21c841566fde000009
    # Array.diff
    """

    total = []

    if not b:
        return a
    else:
        for i in a:
            if i not in b:
                total.append(i)
        return total
