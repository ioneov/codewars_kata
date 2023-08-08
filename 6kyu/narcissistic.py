def narcissistic(value):
    """
    # https://www.codewars.com/kata/5287e858c6b5a9678200083c
    # Does my number look big in this?
    """
    if value < 10:
        return True
    else:
        s = list(str(value))
        summ = 0
        for i in s:
            summ += int(i) ** len(s)

    return summ == value

def narcissistic2( value ):
    if value < 10:
        return True
    else:
        s = list(str(value))
        summ = 0
        for i in s:
            summ += int(i) ** len(s)

    return True if summ == value else False
