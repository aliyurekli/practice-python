# String Lists

word = input("Enter the value to check palindrome:")

if word == word[::-1]:
    print("%s is a palindrome" % word)
else:
    print("%s is not a palindrome" % word)