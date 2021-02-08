def is_number(a):
    if type(a) == int or type(a) == float:
        return True
    return False

def average(arr):
    length = len(arr)
    total = 0

    if length == 0:
        return False
    for i in range(0, length):
        if not(is_number(arr[i])):
            return False
        total += arr[i]
    
    return (total / length)
    