def is_pangram(s):
    """
    # https://www.codewars.com/kata/545cedaa9943f7fe7b000048
    # Detect Pangram
    """
    a = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    s = s.lower()
    for i in a:
        if i in s:
            count += 1
    return True if count == 26 else False
