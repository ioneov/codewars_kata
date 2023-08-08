def find_missing_letter(chars):
    """
    # https://www.codewars.com/kata/5839edaa6754d6fec10000a2
    # Find the missing letter
    """
    ss = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = []
    start_pos =  ss.find(chars[0])
    for i in range(start_pos,start_pos+len(chars)+1):
        s.append(ss[i])
        for x in s:
            if x not in chars:
                return x
