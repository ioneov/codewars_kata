def to_weird_case(string):
    """
    # https://www.codewars.com/kata/52b757663a95b11b3d00062d
    # WeIrD StRiNg CaSe
    """
    ss = []
    for x in string.split():
        s = []
        for i in range(len(x)):
            if i % 2 == 0:
                s.append(x[i].upper())
            else:
                s.append(x[i].lower())
        ss.append(''.join(s))
    return ' '.join(ss)
