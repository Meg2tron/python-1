# note python doesn't support increament (++) and decrement (--) operators

from __future__ import division # interger division was not there in python 2.7

def addition(number1, number2):
    return number1 + number2

def multiplication(number1, number2):
    return number1 * number2

# this will return floating number
def default_division(number1, number2):
    return number1 / number2

# this will divide and then converts into interger
def int_division(number1, number2):
    # special operator of python
    return number1 //  number2

def subtract(number1, number2):
    return number1 - number2

def remainder(number1, number2):
    return number1 % number2

def  exponential(number1, number2):
    # special operator of python
    return number1 ** number2
