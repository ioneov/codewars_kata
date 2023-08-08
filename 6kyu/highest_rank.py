def highest_rank(arr):
    """
    # https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004
    # Highest Rank Number in an Array
    """
    s = {x:0 for x in set(arr)}
    for i in s:
        s[i] = arr.count(i)
    s = {k:v for k, v in s.items() if v == max(s.values())}

    return max(s.keys())
