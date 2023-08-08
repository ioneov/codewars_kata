def order(sentence):
    """
    # https://www.codewars.com/kata/55c45be3b2079eccff00010f
    # Your order, please
    """
    ss = []
    for i in range(9+1):
        for j in sentence.split():
            if str(i) in j:
                ss.append(j)

    return ' '.join(ss)
