def convert_temp(temp, from_scale, to_scale):
    """
    # https://www.codewars.com/kata/54ce9497975ca65e1a0008c6
    # Temperature converter
    """
    if from_scale == to_scale:
        return int(temp)
    temp = convert_to_celsius(temp, from_scale)
    if to_scale == 'C':
        return temp
    elif to_scale == 'F':
        return int(temp * (9 / 5) + 32)
    elif to_scale == 'K':
        return int(temp + 273.15)
    elif to_scale == 'R':
        return int((temp + 273.15) * 9 / 5)
    elif to_scale == 'De':
        return int((100 - temp)* 1.5)
    elif to_scale == 'N':
        return int(temp * (33 /100))
    elif to_scale == 'Re':
        return int(temp * (4 / 5))
    elif to_scale == 'Ro':
        return int(temp * (21/40) + 7.5)

def convert_to_celsius(temp, from_scale):
    if from_scale == 'C':
        return temp
    else:
        if from_scale == 'F':
            return (temp - 32 ) * 5 / 9
        elif from_scale == 'K':
            return temp - 273.15
        elif from_scale == 'R':
            return (temp -491.67) * 5 / 9
        elif from_scale == 'De':
            return 100 - temp * 2 / 3
        elif from_scale == 'N':
            return temp * 100 / 33
        elif from_scale == 'Re':
            return temp * 5 / 4
        elif from_scale == 'Ro':
            return (temp - 7.5) * 40 / 21
