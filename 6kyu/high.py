def high(x):
    """
    # https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
    # Highest Scoring Word
    """
    x = x.split()
    cur_count = 0
    s = []
    for i in x:
        if counter(i) > cur_count:
            cur_count = counter(i)
            s.insert(0,i)
    return s[0]

def counter(data):
    s = 'abcdefghijklmnopqrstuvwxyz'
    count = sum([s.index(x) + 1 for x in data])
    return count
