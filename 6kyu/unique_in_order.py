def unique_in_order(iterable):
    """
    # https://www.codewars.com/kata/54e6533c92449cc251001667
    # Unique In Order
    """
    a = ""
    total = []
    for i in iterable:
        if i != a:
            total.append(i)
        a = i
    return total
