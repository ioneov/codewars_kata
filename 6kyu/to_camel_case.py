def to_camel_case(text, deliminet=''):
    """
    # https://www.codewars.com/kata/517abf86da9663f1d2000003
    # Convert string to camel case
    """
    if len(text) == 0:
        return text
    else:
        ss = text.replace('-', ' ').replace('_', ' ').split()
        return ss[0] + ''.join([i.capitalize() for i in ss[1:]])
