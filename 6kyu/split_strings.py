def solution(s):
    """
    # https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
    # Split Strings
    """
    ss = []
    for i in range(0,len(s),2):
        if len(s[i:i+2]) == 2:
            ss.append(s[i:i+2])
        else:
            ss.append(s[i] + '_')
    return ss
