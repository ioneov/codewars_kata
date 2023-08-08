def move_zeros(array):
    """
    # https://www.codewars.com/kata/52597aa56021e91c93000cb0
    # Moving Zeros To The End
    """
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array
