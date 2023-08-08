def pig_it(text):
    """
    # https://www.codewars.com/kata/520b9d2ad5c005041100000f
    # Simple Pig Latin
    """
    ss = text.split()
    haha = []
    if not ss[-1].isalpha():
        for i in ss[0:-1]:
            haha.append(''.join(i[1:] + i[0:1] + 'ay'))
        haha.append(ss[-1])
    else:
        for i in ss:
            haha.append(''.join(i[1:] + i[0:1] + 'ay'))

    return ' '.join(haha)
