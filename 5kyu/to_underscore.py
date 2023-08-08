def to_underscore(string):
    """
    # https://www.codewars.com/kata/529b418d533b76924600085d
    # Convert PascalCase string into snake_case
    """
    s = []
    ss = []
    string = str(string)
    for i in range(1,len(string)):
        if string[i].isupper():
            s.append(i)

    for j in range(len(string)):
        if j not in s:
            ss.append(string[j].lower())
        else:
            ss.append('_' + string[j].lower())

    return ''.join(ss)
