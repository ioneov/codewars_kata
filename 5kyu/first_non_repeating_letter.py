def first_non_repeating_letter(string):
    """
    # https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
    # First non-repeating character
    """
    if len(string) == 1:
        return string

    ss = string[:].lower()
    for i in range(len(ss)-1):
        if ss.count(ss[i]) == 1:
            return string[i]

    return ''
