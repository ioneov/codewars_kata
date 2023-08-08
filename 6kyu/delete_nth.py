def delete_nth(order,max_e):
    """
    # https://www.codewars.com/kata/554ca54ffa7d91b236000023
    # Delete occurrences of an element if it occurs more than n times
    """
    count = {i:0 for i in order}
    total = []

    for i in order:
        if count[i] < max_e:
            total.append(i)
            count[i] += 1

    return total
