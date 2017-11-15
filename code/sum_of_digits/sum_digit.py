from __future__ import division

def sum_digits(number):
    # preventing infinite loop
    if number < 1: return 0

    count = 0
    while number!=0:
        count += 1
        number //= 10
    return count
