def comp(array1, array2):
    """
    # https://www.codewars.com/kata/550498447451fbbd7600041c
    # Are they the "same"?
    """
    if array1 is None or array2 is None:
        return False
    ss = [x ** 2 for x in sorted(array1)]
    return True if sorted(array2) == sorted(ss) else False
