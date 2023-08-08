def sort_array(source_array):
    """
    # https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
    # Sort the odd
    """
    ss = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            ss.append(source_array[i])
    ss = sorted(ss)
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            ss.insert(i, source_array[i])
    return ss
