'''1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()'''

lst =[1,2,3,4,5,6,7,8,9,10]

def myfilter(func,lst):
    first = []
    for i in lst:
        if func(i):
            first.append(i)
    return first


def even_check(num):
    if num%2 ==0:
        return True

#print(myfilter)(even_check,lst)

# using own myreduce() function
print('Answer using own myfilter() function: ',myfilter(even_check,lst))

# using built-in function reduce()
print('Answer using built-in function myfilter() : ',list(filter(even_check,lst)))