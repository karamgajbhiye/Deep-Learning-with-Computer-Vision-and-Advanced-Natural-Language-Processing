'''
2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
'''

def check_vowel(character):
    if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'):
        return True
    else:
        return False

character = input("Enter character: ")

print(check_vowel(character))