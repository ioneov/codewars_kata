def parse_IPv6(iPv6):
    """
    # https://www.codewars.com/kata/5f5bc8a04e485f002d85b303
    # Weird IPv6 hex string parsing
    """

    b = []
    iPv6 = iPv6.split(iPv6[4])

    for i in range(8):
        a = sum([int(i, 16) for i in iPv6[i]])
        b.append(a)

    return ''.join(str(i) for i in b)
