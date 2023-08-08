def hamming_distance(a, b):
    """
    # https://www.codewars.com/kata/58a6af7e8c08b1e9c40001c1
    # Simple Fun #141: Hamming Distance

    """
    size = max(len(bin(a)[2:]),len(bin(b)[2:]))
    a = bin(a)[2:].zfill(size)
    b = bin(b)[2:].zfill(size)
    count = 0
    for i in range(size):
        if a[i] != b[i]:
            count += 1
    return count
