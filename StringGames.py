# Write a program that reads text from the user and reverses the order of every number that appears in the text.
#
# For example:
#
# Hello! The number is 17.
#
# will become
#
# Hello! The number is 71.
#
# To help with this problem, first write a function rev(text) that takes a string of text and returns the reverse.
#
# For example, rev("Oranges") would return "segnarO". You may create any addition function you need. You must create the rev function.
#
# Your program will ask for a string of text and reverse and number. A number is defined as any sequence of digits 0-9.
#
# Remember to use if name=="__main": so that ZyBooks can test your rev function.
#
# Here are two examples.
#
# Welcome to Digit Flipper
# Enter Some Text:
# Hello! The number is 17.
# Revised String:
# Hello! The number is 71.
# The input may not have any spaces at all to break up the text.
#
# Welcome to Digit Flipper
# Enter Some Text:
# a123bb456bbsdfjhskdjh987sss1928
# Revised String:
# a321bb654bbsdfjhskdjh789sss8291


def rev(text):
    return text[::-1]


def solve(text):
    newText = ""
    isNumHappening = False
    curNum = ""
    for c in text:
        if (not c.isdigit()):
            newText += rev(curNum)
            newText += c
            isNumHappening = False
            curNum = ""
        else:
            isNumHappening = True
            curNum += c
    if isNumHappening:
        newText += rev(curNum)
    return newText

if __name__ == '__main__':
    print('Welcome to Digit Flipper')
    usrText = input('Enter Some Text:\n')
    print('Revised String:\n')
    print(solve(usrText))
