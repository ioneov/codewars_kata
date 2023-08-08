def xo(s):
    """
    # https://www.codewars.com/kata/55908aad6620c066bc00002a
    # Exes and Ohs
    """
    count_x = 0
    count_o = 0

    list_s = list(s)
    for i in list_s:
        if i == 'x' or i == 'X':
            count_x += 1
        if i == 'o' or i == 'O':
            count_o += 1

    if count_o == count_x:
        return True
    else:
        return False
