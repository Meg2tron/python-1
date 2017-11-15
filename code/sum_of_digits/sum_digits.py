from __future__ import division

def sum_of_digits(number):
    if number < 0: return None
    total = 0
    while number != 0:
        total += number%10
        number //= 10

    return total
