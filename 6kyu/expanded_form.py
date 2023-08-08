def expanded_form(num):
    """
    # https://www.codewars.com/kata/5842df8ccbd22792a4000245
    # Write Number in Expanded Form
    """
    if num < 11:
        return str(num)
    else:
        ss = []
        num = [x for x in str(num)[::-1]]
        for i in range(len(num)):
            if int(num[i]) != 0:
                ss.append(num[i] + i * '0')
    return ' + '.join(reversed(ss))
