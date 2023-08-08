def make_readable(s):
    """
    # https://www.codewars.com/kata/52685f7382004e774f0001f7
    # Human Readable Time
    """
    hours = s // 3600
    minutes = (s - hours * 3600) // 60
    seconds = (s - hours * 3600 - minutes * 60)
    return '{:02}:{:02}:{:02}'.format(hours,minutes,seconds)

def make_readable2(s):
    hours = s // 3600
    minutes = (s - hours * 3600) // 60
    seconds = (s - hours * 3600 - minutes * 60)
    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if seconds < 10:
        seconds = '0' + str(seconds)

    return '{}:{}:{}'.format(hours,minutes,seconds)
