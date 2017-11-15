
def get_gcd(num1, num2):
    if num1 == 0 or num2 == 0:
        raise Exception("values must be non - zero")
    
    while num1 != num2:
        if num1 < num2:
            num2 -= num1
        else:
            num1 -= num2
    return num1