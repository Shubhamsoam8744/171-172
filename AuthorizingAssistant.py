# (1) Prompt the user to enter a string of their choosing. Store the text in a string. Output the string. (1 pt)
#
# Ex:
#
# Enter a sample text:
# we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!
#
# You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!
#
# (2) Implement a print_menu() function, which has a string as a parameter, outputs a menu of user options for analyzing/editing the string, and returns the user's entered menu option and the sample text string (which can be edited inside the print_menu() function). Each option is represented by a single character.
#
# If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement the Quit menu option before implementing other options. Call print_menu() in the main section of your code. Continue to call print_menu() until the user enters q to Quit. (3 pts)
#
# Ex:
#
# MENU
# c - Number of non-whitespace characters
# w - Number of words
# f - Fix capitalization
# r - Replace punctuation
# s - Shorten spaces
# q - Quit
#
# Choose an option:
#
# (3) Implement the get_num_of_non_WS_characters() function. get_num_of_non_WS_characters() has a string parameter and returns the number of characters in the string, excluding all whitespace. Call get_num_of_non_WS_characters() in the print_menu() function. (4 pts)
#
# Ex:
#
# Number of non-whitespace characters: 181
#
# (4) Implement the get_num_of_words() function. get_num_of_words() has a string parameter and returns the number of words in the string. Hint: Words end when a space is reached except for the last word in a sentence. Call get_num_of_words() in the print_menu() function. (3 pts)
#
# Ex:
#
# Number of words: 35
#
# (5) Implement the fix_capilization() function. fix_capilization() has a string parameter and returns an updated string, where lowercase letters at the beginning of sentences are replaced with uppercase letters. fix_capilization() also returns the number of letters that have been capitalized. Call fix_capilization() in the print_menu() function, and then output the number of letters capitalized and the edited string. Hint 1: Look up and use Python functions .islower() and .upper() to complete this task. Hint 2: Create an empty string and use string concatenation to make edits to the string. (3 pts)
#
# Ex:
#
# Number of letters capitalized: 3
# Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!
#
# (6) Implement the replace_punctuation() function. replace_punctuation() has a string parameter and two keyword argument parameters exclamationCount and semicolonCount. replace_punctuation() updates the string by replacing each exclamation point (!) character with a period (.) and each semicolon (;) character with a comma (,). replace_punctuation() also counts the number of times each character is replaced and outputs those counts. Lastly, replace_punctuation() returns the updated string. Call replace_exclamation() in the print_menu() function, and then output the edited string. (3 pts)
#
# Ex:
#
# Punctuation replaced
# exclamationCount: 1
# semicolonCount: 2
# Edited text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here,  our hopes and our journeys continue.
#
# (7) Implement the shorten_space() function. shorten_space() has a string parameter and updates the string by replacing all sequences of 2 or more spaces with a single space. shorten_space() returns the string. Call shorten_space() in the print_menu() function, and then output the edited string. Hint: Look up and use Python function .isspace(). (3 pt)
#
# Ex:
#
# Edited text: we'll continue our quest in space. there will be more shuttle flights and more shuttle crews and, yes, more volunteers, more civilians, more teachers in space. nothing ends here; our hopes and our journeys continue!

def get_num_of_non_WS_characters(usrStr):
    numOfChars = len(usrStr.replace(' ', ''))
    return numOfChars


def get_num_of_words(usrStr):
    return len(usrStr.split())


def fix_capitalization(usrStr):
    num = 0
    usrStrList = []
    for c in usrStr:
        usrStrList.append(c)

    lead_char = True
    for ix, c in enumerate(usrStrList):
        if lead_char and c.isalpha():
            c = c.upper()
            num += 1
            # insert changed processed character into list
            usrStrList[ix] = c
            # set leading character flag to false
            lead_char = False
        if c in '?!.':
            lead_char = True
    newStr = ''.join(usrStrList)
    return newStr, num


def replace_punctuation(usrStr, exclamationCount = 0, semicolonCount = 0):
    # exclamationCount = 0
    # semicolonCount = 0
    usrStrList = []
    for c in usrStr:
        usrStrList.append(c)
    for i in usrStrList:
        if i == '!':
            exclamationCount += 1
        elif i == ';':
            semicolonCount += 1
    newStr = ''.join(usrStrList)
    newStr = newStr.replace('!', '.').replace(';', ',')
    print('exclamationCount:', exclamationCount)
    print('semicolonCount:', semicolonCount)
    return newStr


def shorten_space(usrStr):
    for i in range(1, 6):
        usrStr = usrStr.replace(' ' * i, ' ')
    usrStr = usrStr.replace('  ', ' ')
    return usrStr


def print_menu(usrStr):
    menuOptions = ['c', 'w', 'f', 'r', 's', 'q']
    print('''
MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit
''')
    menuOp = input('Choose an option:\n')
    while menuOp not in menuOptions:
        menuOp = input('Choose an option:')
    if menuOp == 'c':
        print('Number of non-whitespace characters:', get_num_of_non_WS_characters(usrStr))
    elif menuOp == 'w':
        print('Number of words:', get_num_of_words(usrStr))
    elif menuOp == 'f':
        newStr, num = fix_capitalization(usrStr)
        print('Number of letters capitalized:', num)
        print('Edited text:', newStr)
    elif menuOp == 'r':
        print('Punctuation replaced')
        newStr = replace_punctuation(usrStr)
        print('Edited text:', newStr)
    elif menuOp == 's':
        print('Edited text:', shorten_space(usrStr))
    return menuOp, usrStr


if __name__ == '__main__':
    sampleText = input('Enter a sample text:\n')
    print('\nYou entered:', sampleText)
    menuCh, userStr = print_menu(sampleText)
    while menuCh != 'q':
        menuCh, userStr = print_menu(sampleText)
