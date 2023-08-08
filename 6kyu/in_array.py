def in_array(array1, array2):
    """
    # https://www.codewars.com/kata/550554fd08b86f84fe000a58
    # Which are in?
    """
    ss = []
    for i in array1:
        for j in array2:
            if i in j and i not in ss:
                ss.append(i)
    return sorted(ss)
