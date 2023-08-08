def isbn_converter(isbn):
    """
    # https://www.codewars.com/kata/61ce25e92ca4fb000f689fb0
    # Convert ISBN-10 to ISBN-13
    """
    isbn = '978-' + isbn[0:-2] + '-'
    ss = []
    for i in range(len(isbn.replace('-',''))):
        if i % 2 != 0:
            ss.append(int(isbn.replace('-','')[i])*3)
        else:
            ss.append(int(isbn.replace('-','')[i]))
    if sum(ss) % 10 == 0:
        isbn += '0'
    else:
        isbn += str(10-(sum(ss) % 10))

    return isbn
