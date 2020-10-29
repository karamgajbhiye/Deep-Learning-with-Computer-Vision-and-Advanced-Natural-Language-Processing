'''1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.'''

new_lst = []
def filter_long_words(lst,n):
    for i in lst:
        if len(i)>n:
            new_lst.append(i)
    return new_lst

# or using list comprehension
'''def filter_long_words(lst,n):
    return [i for i in lst if len(i)>n]'''

lst = input("Please input the list of words: ").split()
n = int(input('Please input an integer n : '))
print('Integer n : ', n)
print('Orginal list',lst)


#print(filter_long_words(['hello','karam','para','564544'],4))
print('List after filter -  list of words that are longer than n : ',filter_long_words(lst,n))
