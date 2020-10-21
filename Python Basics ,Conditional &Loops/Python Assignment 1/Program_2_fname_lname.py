'''2. Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.'''

print('Enter First name')
first_name = input()
print('Enter Last name')
last_name = input()
print('Your name printed in the the reverse order with a space between first name and last name')
print('\n')
print('{} {}'.format(first_name[::-1],last_name[::-1]))
#2nd solution
#print(first_name[::-1],'',last_name[::-1])