
def is_armstrong(number):
    # defining total
    total = 0

    # cloning number
    duplicate = number

    # looping till duplicate != 0
    while duplicate != 0:
        total += (duplicate % 10) ** 3
        duplicate //= 10

    # returns true if sum of cube of digits is equal to original number
    return total == number
