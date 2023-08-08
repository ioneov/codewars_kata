def format_duration(seconds):
    """
    # https://www.codewars.com/kata/52742f58faf5485cae000b9a
    # Human readable duration format
    """
    if seconds == 0:
        return 'now'

    MINUTE = 60
    HOUR = 3600
    DAY = 86400
    YEAR = 31536000

    ss = [0, 0, 0, 0, 0]  # [years, days, hours, minutes, seconds]

    ss[0] = seconds // YEAR  # years
    ss[1] = (seconds - ss[0] * YEAR) // DAY  # days
    ss[2] = (seconds - ss[0] * YEAR - ss[1] * DAY) // HOUR  # hours
    ss[3] = (seconds - ss[0] * YEAR - ss[1] * DAY -
             ss[2] * HOUR) // MINUTE  # minutes
    ss[4] = (seconds - ss[0] * YEAR - ss[1] * DAY -
             ss[2] * HOUR - ss[3] * MINUTE)  # seconds

    if ss[0] != 0:
        if ss[0] == 1:
            ss[0] = str(ss[0]) + ' year'
        else:
            ss[0] = str(ss[0]) + ' years'

    if ss[1] != 0:
        if ss[1] == 1:
            ss[1] = str(ss[1]) + ' day'
        else:
            ss[1] = str(ss[1]) + ' days'

    if ss[4] != 0:
        if ss[4] == 1:
            ss[4] = str(ss[4]) + ' second'
        else:
            ss[4] = str(ss[4]) + ' seconds'

    if ss[3] != 0:
        if ss[3] == 1:
            ss[3] = str(ss[3]) + ' minute'
        else:
            ss[3] = str(ss[3]) + ' minutes'
    if ss[2] != 0:
        if ss[2] == 1:
            ss[2] = str(ss[2]) + ' hour'
        else:
            ss[2] = str(ss[2]) + ' hours'
    if ss.count(0) == 3:
        return ' and '.join([x for x in ss if x != 0])
    elif ss.count(0) == 4:
        return ''.join([x for x in ss if x != 0])
    else:
        return ' and'.join(', '.join([x for x in ss if x != 0]).rsplit(',', 1))
