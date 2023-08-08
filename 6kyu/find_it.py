def find_it(seq):
    """
    # https://www.codewars.com/kata/54da5a58ea159efa38000836
    # Find the odd int
    """
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
