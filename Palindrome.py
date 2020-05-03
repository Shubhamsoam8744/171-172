# A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.
#
# Ex: If the input is:
#
# bob
# the output is:
#
# bob is a palindrome
# Ex: If the input is:
#
# bobby
# the output is:
#
# bobby is not a palindrome
# Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

userString = input()
userString2 = userString.replace(' ', '')
reverseString = userString2[::-1]

if userString2 == reverseString:
    print(userString, 'is a palindrome')
else:
    print(userString, 'is not a palindrome')
