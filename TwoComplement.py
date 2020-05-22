# One popular method to store negative numbers in Binary is Two's Complement.
#
# To convert a positive number to Two's Complement requires two steps.
#
# Fit all bits (1 to 0 and 0 to 1)
# Add one to the result
# As an 8-Bit Number
#
# 8 = 00001000
#
# Step 1: Flip All bits
#
# 11110111
#
# Step 2: Add 1
#
# 11110111 + 1 = 11111000
#
# Remember the number of bits does not change. If a 1 is carried to the end of the number it is dropped.
#
# Write a function twoscomp(num) that takes a string of 0s and 1s. The function will return a string with the Two's Complement version of the binary number.
#
# Create an interface that asks the users for a binary number and prints the Two's Complement version. Remember to wrap your interface with if name=="main": so ZyBooks can test your function.
#
# Welcome to Two's Complement Creator
# Enter a Binary Value:
# 11111111
# In Two's Complement:
# 00000001

def twoscomp(num):
    num = num.replace('1', '2')
    num = num.replace('0', '1')
    num = num.replace('2', '0')
    comp = str(bin(int(num, 2) + 1)).replace("0b", "")
    comp = '0' * (8 - len(comp)) + comp
    return comp[len(comp) - 8:]


if __name__ == '__main__':
    print('Welcome to Two\'s Complement Creator')
    binValue = input('Enter a Binary Value:\n')
    print('In Two\'s Complement:\n' + twoscomp(binValue))
