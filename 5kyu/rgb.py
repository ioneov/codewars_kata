def rgb(r, g, b):
    """
    # https://www.codewars.com/kata/513e08acc600c94f01000001
    # RGB To Hex Conversion
    """
    return "{:02x}{:02x}{:02x}".format(max(0, min(r, 255)),
                                       max(0, min(g, 255)),
                                       max(0, min(b, 255))).upper()
