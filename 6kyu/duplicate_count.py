def duplicate_count(text):
    """
    # https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
    # Counting Duplicates
    """
    b = []
    text = list(text.lower())
    for a in set(text):
        if text.count(a) > 1:
            b.append(a)
    return len(b)
