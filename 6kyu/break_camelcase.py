def solution(s):
    """
    # https://www.codewars.com/kata/5208f99aee097e6552000148
    # Break camelCase
    """
    ss = []
    for i in s:
        if i.isupper():
            ss.append(' ' + i)
        else:
            ss.append(i)
    return ''.join(ss)
