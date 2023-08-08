def rot13(message):
    """
    # https://www.codewars.com/kata/530e15517bc88ac656000716
    # Rot13
    """
    s = str.maketrans(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')
    return message.translate(s)
