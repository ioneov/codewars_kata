def duplicate_encode(word):
    """
    # https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
    # Duplicate Encoder
    """
    word = word.lower()
    ss = []
    for i in range(len(word)):
        if word.count(word[i]) == 1:
            ss.append('(')
        else:
            ss.append(')')
    return ''.join(ss)
