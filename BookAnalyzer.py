# This exercise is designed to give you experience looping over files and making decisions based on their contents.
#
# The program asks the user for three pieces of information.
#
# A text file to open
# A letter to search for
# A position to look in
# The program counts how many words have the given character in the correct position. For example, the previous sentence contains 5 words with 'o' in position 1.
#
# Your program must check for errors. If an error is encountered, call sys.exit(0) after printing a message.
#
# If the file cannot be opened, then print an error. (Hint: Use a try/except with OSError)
#
# Welcome to Book Analyzer v0.1
# Enter File Name to Read:
# fake_name.txt
# Error: Could Not Open File.
# Print an error if something other then a single letter is given to search for.
#
# Enter File Name to Read:
# modest.txt
# Letter to search for:
# A Bad Input
# Error: A single letter is required.
# Print an error if the third input is not a number.
#
# Welcome to Book Analyzer v0.1
# Enter File Name to Read:
# modest.txt
# Letter to search for:
# a
# Enter Position (0 for first letter):
# Two
# Error: A number is required.
# If all inputs are good, then you can read the file. Get each word out of the file and check it against the inputs. Count how many words appear with the character given in the correct location.
#
# Welcome to Book Analyzer v0.1
# Enter File Name to Read:
# modest.txt
# Letter to search for:
# h
# Enter Position (0 for first letter):
# 1
# There are 853 words with h in position 1
# You should count both the upper and lower case versions of a letter. If the user enters a, then mean count both A and a. You can use str_var.lower() to make a string lowercase.
#
# The two files are: modest.txt and poe.txt
import sys

print('Welcome to Book Analyzer v0.1')
filename = input('Enter File Name to Read:\n')
try:
    fileStream = open(filename, 'r')
except OSError:
    print('Error: Could Not Open File.')
    sys.exit(0)
letter = input('Letter to search for:\n')
if len(letter) > 1:
    print('Error: A single letter is required.')
    sys.exit(0)
try:
    pos = int(input('Enter Position (0 for first letter):\n'))
except ValueError:
    print('Error: A number is required.')
    sys.exit(0)

fileContent = fileStream.read().split()
c = 0
for word in fileContent:
    if len(word) - 1 >= pos:
        if word[pos] == letter.lower() or word[pos] == letter.upper():
            c += 1

print('There are', c, 'words with', letter, 'in position', pos)
