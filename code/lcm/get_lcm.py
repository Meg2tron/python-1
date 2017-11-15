def get_lcm(num1,num2):
    if num1 == 0 or num2 == 0: return 0

    greater = num1
    if num2 > num1:
        greater = num2

    for x in range(greater, num1 *num2):
        if x % num1 == 0 and x % num2 == 0:
            return x

    return num1 * num2
