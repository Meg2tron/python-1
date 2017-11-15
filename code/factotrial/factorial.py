def iterative(number):
    if number < 2: return 1
    factorial = 1

    # for loop in reverse order
    for x in range(number,1,-1):
        factorial *= x
    return factorial

def recursive(number):
    if number < 1: return 1
    return number * recursive(number - 1)
