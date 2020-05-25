# In this lab, you will experiment with opening an reading files.
#
# A file has been attached to this lab called english.txt. It contains a selection of random english words. There is one word on each line.
#
# Open the file by using the command
#
# f = open("english.txt","r")
# Ask the user for a single letter. Loop through the file and print any word that starts with that letter. Your letter match should be case insensitive. If the user enters A, you should print words that start with a.
#
# Remember to close your file once you have completed the task.
#
# You are not required to do any error checking in this part of the lab.
#
# Enter First Letter:
# A
# agouties
# amphora
# allotropy
# anguses
# auroras
# assuring
# anesthetics
# arrant
# averments
# autopsied
# anastomoses
# alpaca
# anthropoids
# addicting
# absconder
# answers
# abbe
# aggressors
# armband
# abjuratory

letter = input('Enter First Letter:\n')
with open("english.txt", 'r') as f:
    wordList = f.read().split()
    for word in wordList:
        if word[0] == letter.lower() or word[0] == letter.upper():
            print(word)
