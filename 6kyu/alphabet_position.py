def alphabet_position(text):
    """
    # https://www.codewars.com/kata/546f922b54af40e1e90001da
    # Replace With Alphabet Position
    """
    total = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    for c in text.lower():
        if c in abc:
            total.append(str(abc.find(c) + 1))
    return ' '.join(total)
