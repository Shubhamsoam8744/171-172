# Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.
#
# Write a program that takes a string and integer as input, and outputs a sentence using those items as below. The program repeats until the input string is quit.
#
# Ex: If the input is:
#
# apples 5
# shoes 2
# quit 0
# the output is:
#
# Eating 5 apples a day keeps the doctor away.
# Eating 2 shoes a day keeps the doctor away.
# Note: This is a lab from a previous chapter that now requires the use of a loop.

inp = input()
inputList = inp.split()

word = inputList[0]
num = inputList[1]
printString = []
while word != 'quit':
    printString.append('Eating ' + str(num) + ' ' + str(word) + ' a day keeps the doctor away.')
    inp = input()
    inputList = inp.split()

    word = inputList[0]
    num = inputList[1]

for i in printString:
    print(i)
