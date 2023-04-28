def invert(s):
    try:
        s = s[::-1]
    except TypeError:
        s = ''
    return s