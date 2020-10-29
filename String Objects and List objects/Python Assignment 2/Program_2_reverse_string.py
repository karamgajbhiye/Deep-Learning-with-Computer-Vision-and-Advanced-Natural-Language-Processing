'''2. Write a Python program to reverse a word after accepting the input from the user.
Input word: ineuron
Output: norueni'''

word1 = input("Enter word: ")
def reverse(word):
    word = "".join(reversed(word))
    return word

print("The original word  is : ",word1, end="\n")

print("The reversed word is : ",reverse(word1),end="\n")


'''output = word1[::-1]
print("The original word  is : ",word1, end="\n")

print("The reversed word is : ",output,end="\n")'''
