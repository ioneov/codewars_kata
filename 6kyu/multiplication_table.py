def multiplication_table(size):
    """
    # https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08
    # Multiplication table
    """
    ss = []
    for i in range(1,size+1):
        s = []
        for j in range(1,size+1):
            s.append(j*i)
        ss.append(s)
    return ss
