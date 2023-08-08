def likes(names):
    """
    # https://www.codewars.com/kata/5266876b8f4bf2da9b000362
    # Who likes it?
    """
    if not names:
        return 'no one likes this'
    else:
        if len(names) == 1:
            return '{} likes this'.format(names[0])
        elif len(names) == 2:
            return '{} and {} like this'.format(*names)
        elif len(names) == 3:
            return '{}, {} and {} like this'.format(*names)
        else:
            return '{}, {} and {} others like this'.format(*names[:2], len(names) - 2)
