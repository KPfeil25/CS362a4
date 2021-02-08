def is_number(a):
    if type(a) == int or type(a) == float:
        return True
    return False

def volume(a, b, c):
    if (not(is_number(a)) or not(is_number(b)) or not(is_number(c))):
        return False
    if (a < 0 or b < 0 or c < 0):
        return False
    return a * b * c