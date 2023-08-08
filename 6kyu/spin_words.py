def spin_words(sentence):
    """
    # https://www.codewars.com/kata/5264d2b162488dc400000001
    # Stop gninnipS My sdroW!
    """
    ss = []
    for i in sentence.split():
        if len(i) >= 5:
            ss.append(i[::-1])
        else:
            ss.append(i)

    return ' '.join(ss)
