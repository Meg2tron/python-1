
def russian_peasant(num1, num2):
    res = 0

    # iterating till num2 != 0
    while num2 > 0:
        # adding value of num1 if num2 is odd
        if num2 % 2 != 0:
            res += num1

        # bit manipulation
        num2 >>= 1    # right shift by 1 bit
        num1 <<= 1    # left shift by 1 bit

    return res
