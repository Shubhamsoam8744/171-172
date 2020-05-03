# When we read values using the input command, they always start as strings.
#
# If we try to convert a string to an integer or a float and the conversion fails, an error will be thrown. Specifically, a value error. We can catch this error using an except statement. The following example shows an error being caught.
#
# try:
#     x = int("Not a Number")
# except ValueError as e:
#     print("Error:",e)
# If the code is executed, it will print
#
# Error: invalid literal for int() with base 10: 'Not a Number'
# For this part of the lab, ask the user for an input and use try/except statements to determine if the data is an integer, float, or string.
#
# The interface should match the following examples.
#
# Welcome to Type Guesser
# Enter Something:
# 9
# You entered an integer!
# Value: 9
# Welcome to Type Guesser
# Enter Something:
# 12.9
# You entered a float!
# Value: 12.9
# Welcome to Type Guesser
# Enter Something:
# Oranges
# You entered a string!
# Value: Oranges
# Welcome to Type Guesser
# Enter Something:
# 12.9 Oranges
# You entered a string!
# Value: 12.9 Oranges

print('Welcome to Type Guesser')
userData = input('Enter Something:\n')

try:
    x = int(userData)
    print('You entered an integer!')
    print('Value:', x)
except:
    try:
        x = float(userData)
        print('You entered a float!')
        print('Value:', x)
    except:
        print('You entered a string!')
        print('Value:', userData)