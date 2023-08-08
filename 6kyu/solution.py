def solution(number):
    """
    # https://www.codewars.com/kata/514b92a657cdc65150000006
    # Multiples of 3 or 5
    """
    summ = 0
    for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ
