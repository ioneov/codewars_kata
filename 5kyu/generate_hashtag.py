def generate_hashtag(s):
    """
    # https://www.codewars.com/kata/52449b062fb80683ec000024
    # The Hashtag Generator
    """
    if len(s) == 0 or len(s) > 140:
        return False
    ss = ['#']
    s = s.strip().split()
    for i in s:
        ss.append(i.capitalize())
    return ''.join(ss)
