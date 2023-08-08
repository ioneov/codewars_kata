def camel_case(string):
    """
    # https://www.codewars.com/kata/587731fda577b3d1b0001196
    # CamelCase Method
    """
    ss = []
    for i in string.split():
        ss.append(i.capitalize())

    return ''.join(ss)
