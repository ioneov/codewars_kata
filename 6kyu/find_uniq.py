def find_uniq(arr):
    """
    # https://www.codewars.com/kata/585d7d5adb20cf33cb000235
    # Find the unique number
    """
    for i in set(arr):
        if arr.count(i) == 1:
            return i
