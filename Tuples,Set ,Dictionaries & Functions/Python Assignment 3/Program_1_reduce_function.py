'''1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()'''
from functools import reduce
def myreduce(func,lst):
    first = lst[0]
    for i in lst[1:]:
        first = func(first,i)
    return first

max_find = lambda a,b: a if (a > b) else b
lst =[41,11,42,13,55,81,14]

# using own myreduce() function
print('Answer using own myreduce() function: ',myreduce(max_find,lst))

# using built-in function reduce()
print('Answer using built-in function reduce() : ',reduce(max_find,lst))

#result
#Answer using own myreduce() function:  81
#Answer using built-in function reduce() :  81