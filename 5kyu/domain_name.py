import re

def domain_name(url):
    """
    # https://www.codewars.com/kata/514a024011ea4fb54200004b
    # Extract the domain name from a URL
    """
    s = re.split(r'h[t]{2}p[s]?:[/]{2}|\.|[w]{3}', url)
    for i in s:
        if i != '':
            return i
