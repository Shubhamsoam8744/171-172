# We will draw a recursively defined picture in this program.
#
# Create a function def fractal(length, spaces). This function will print out a certain number of stars * and spaces.
#
# If length is 1 print out the number of spaces given followed by 1 star.
# If the length is greater than one do the following:
# Print the fractal pattern with half the length and the same number of spaces.
# Print the number of spaces given followed by length stars.
# Print the fractal pattern with half the length and spaces+(length//2) spaces in front of it.
# Once your function works, prompt the user for an integer x and execute fractal(x,0). You will not receive credit if your function is not recursive.
#
# If the input is not an integer > 0, ask again. Your program should exit after successfully drawing a Fractal.
#
# You may create any additional functions you want to complete this assignment. Only the fractal function must be recursive.
#
# Example 1
#
# Fractal Generator
# Enter an integer > 0:
# Cats
# Enter an integer > 0:
# 3
# *
# ***
#  *
# Example 2
#
# Fractal Generator
# Enter an integer > 0:
# 8
# *
# **
#  *
# ****
#   *
#   **
#    *
# ********
#     *
#     **
#      *
#     ****
#       *
#       **
#        *


def fractal(length, spaces):
    if length == 1:
        print(' ' * spaces + '*')
    else:
        fractal(length // 2, spaces)
        print(' ' * spaces + '*' * length)
        fractal(length // 2, spaces + (length//2))


if __name__ == '__main__':
    print('Fractal Generator')
    try:
        num = int(input('Enter an integer > 0:\n'))
    except:
        num = int(input('Enter an integer > 0:\n'))
    fractal(num, 0)
