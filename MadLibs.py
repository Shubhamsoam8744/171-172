# The goal of this assignment is to create a version of game Mad Libs. Given a text file with the story, the program will ask the user to fill in the blanks. The program will then show the user the final story.
#
# Word Template Games
#
# Mad Libs are a type of word template game. A story is written with multiple blank spaces. The game has two players. One player asks the other for words to fill in the blanks. The player suggesting words does not know what the story is or what the words are for. Once all the blanks have been filled in, the story is read. Since the person suggesting the words does not know the context, this will lead to a funny but nonsensical story.
#
# An example of a real Mad Lib game is provided at the end of the instructions.
#
# The text files we are using are based on example 1 and example 2.
#
# Programming Project
#
# You will develop a python program that reads from a text file and fills in the blanks for a story.
#
# The first thing the program needs to do it ask for the text file containing the story. The program will then read the file.
#
# While the file is being read, the program will encounter words that start with a square bracket [. A word that starts with a square bracket is a blank. It needs to be filled in by the user. Between the [ and ] in the string is what type of word to ask the user for.
#
# For example, if the program encounters [verb-ending-in-ing] then it should ask "Please give a verb ending in ing". The input from the user is then read to fill in the blank.
#
# Once the entire store is complete, it will be printed out for the user.
#
# The following additional guidelines must be followed:
#
# Only print the story once all blanks have been filled in.
# If the type of word being asked for starts with a vowel ask "Please give an …"
# If the type of word being asked for does not start with a vowel as "Please give a …"
# Users may give multiple word answers.
# Your program should not crash if the file cannot be read. It should exit gracefully.
# The blank space may have punctuation, be sure this is correctly printed in the story.
# Your program must work with the three example files provided.
# If the file does not exist print and error and exit with sys.exit(0)
#
# Welcome to a fun word replacement game.
# Enter the name of the file to use:
# fake_file.txt
# Error Bad File Name
# Example Execution Trace
#
# You must exactly match the below layout.
#
# Welcome to a fun word replacement game.
# Enter the name of the file to use:
# example1.txt
# Please give a name
# Mark
# Please give a place
# Drexel
# Please give a day of the week
# Friday
# Please give a time
# noon
# Please give a verb
# eat
# Please give an animal
# raccoon
# Please give a body part
# mouth
# Here is your story:
# --------------------
# Mark is having a party! It's going to be at Drexel
# on Friday. Please make sure to show up at noon,
# or else you will be required to eat a/an raccoon
# with your mouth.
# Welcome to a fun word replacement game.
# Enter the name of the file to use:
# mad_lib.txt
# Please give an adjective
# cold
# Please give an adjective
# loser
# Please give a noun
# mountain
# Please give a noun
# moon
# Please give a plural noun
# cats
# Please give a game
# super mario 3
# Please give a plural noun
# men
# Please give a verb ending in ing
# reading
# Please give a verb ending in ing
# killing
# Please give a plural noun
# goats
# Please give a verb ending in ing
# knitting
# Please give a noun
# swamp
# Please give a plant
# spider plant
# Please give a part of the body
# leg
# Please give a place
# Texas
# Please give a verb ending in ing
# programming
# Please give an adjective
# excited
# Please give a number
# 17
# Please give a plural noun
# sandwiches
# Here is your story:
# --------------------
# A vacation is when you take a trip to some cold place
# with your loser family. Usually you go to some place
# that is near a/an mountain or up on a/an moon. A good
# vacation place is one where you can ride cats or play
# super mario 3 or go hunting for men. I like to spend
# my time reading or killing. When parent go on a vacation,
# they spend their time eating three goats a day, and fathers
# play golf, and mothers sit around knitting. Last summer,
# my little brother fell in a/an swamp and got poison spider
# plant all over his leg. My family is going to go to (the)
# Texas, and I will practice programming. Parents need
# vacations more than kids because parents are always
# very excited and because they have to work 17 hours
# every day all year making enough sandwiches to pay
# for the vacation.
import sys

print('Welcome to a fun word replacement game.')
filename = input('Enter the name of the file to use:\n')
try:
    fileStream = open(filename, 'r')
    fileContent  = fileStream.read().split()
except OSError:
    print('Error Bad File Name')
    sys.exit(0)
finalStory = []
for word in fileContent:
    if '[' in word:
        hasPunctuation = False
        if word[-1] in [',', '.']:
            hasPunctuation = True
            punctuation = word[-1]
        word = word.replace('[', '').replace(']', '').replace('.', '').replace(',', '').replace('-', ' ')
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            inputMsg = 'Please give an ' + str(word) + '\n'
        else:
            inputMsg = 'Please give a ' + str(word) + '\n'
        usrInput = input(inputMsg)
        if hasPunctuation:
            finalStory.append(usrInput + str(punctuation))
        else:
            finalStory.append(usrInput)
    else:
        finalStory.append(word)
story = ' '.join(finalStory)
print('Here is your story:')
print('--------------------')
print(story)
