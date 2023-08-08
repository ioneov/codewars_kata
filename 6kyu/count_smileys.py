import re
def count_smileys(arr):
    """
    # https://www.codewars.com/kata/583203e6eb35d7980400002a
    # Count the smiley faces!
    """
    return len(re.findall('[:;][-~]?[)D]', str(arr)))
