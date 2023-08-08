import re
def valid_phone_number(phone_number):
    """
    # https://www.codewars.com/kata/525f47c79f2f25a4db000025
    # Valid Phone Number
    """
    re_number = r'^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$'
    return True if re.findall(re_number, phone_number) else False
