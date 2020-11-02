'''1. Write a function to compute 5/0 and use try/except to catch the exceptions.'''


def zero_divisor():
    return 5/0


try:
    zero_divisor()
except ZeroDivisionError:
    print('Error : Division by zero(0).')
except :
    print('Any other exception.')