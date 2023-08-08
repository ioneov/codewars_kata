def digital_root(n):
    """
    # https://www.codewars.com/kata/541c8630095125aba6000c00
    # Sum of Digits / Digital Root
    """
    summ = 0
    for i in str(n):
        summ += int(i)
    return summ if summ < 10 else digital_root(summ)
