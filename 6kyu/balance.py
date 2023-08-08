def balance(left, right):
    """
    # https://www.codewars.com/kata/57fb44a12b53146fe1000136
    # Exclamation marks series #17: Put the exclamation marks and question 
    marks on the balance - are they balanced?
    """
    w_left = (left.count('!') * 2) + (left.count('?') * 3)
    w_right = (right.count('!') * 2) + (right.count('?') * 3)

    if w_left > w_right:
        return 'Left'
    if w_left < w_right:
        return 'Right'
    else:
        return 'Balance'
