def count(string):
    """
    # https://www.codewars.com/kata/52efefcbcdf57161d4000091
    # Count characters in your string
    """
    ss = {x:0 for x in set(string)}
    for k,v in ss.items():
        ss[k] = string.count(k)
    return ss
