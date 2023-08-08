def create_phone_number(n):
    """
    # https://www.codewars.com/kata/525f50e3b73515a6db000b83
    # Create Phone Number
    """
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)

def create_phone_number2(n):
    n.insert(0,'(')
    n.insert(4,')')
    n.insert(5,' ')
    n.insert(9,'-')
    return ''.join(str(i) for i in n)
