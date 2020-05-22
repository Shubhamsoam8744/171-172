# In this exercise, we will implement binary addition. You must implement the actual rules of binary addition.
#
# When adding Binary numbers, each column has three inputs and two outputs.
#
# The inputs are
#
# c = Carry From Last Column (Initially 0)
#
# a = Current Bit of First Number
#
# b = Current Bit of Second Number
#
# The outputs are
#
# o = Carry for next Column
#
# r = Bit of Result Number
#
# There are a total of 8 possible cases for each column.
#
# c + a + b = or
#
# 0 + 0 + 0 = 00
#
# 0 + 0 + 1 = 01
#
# 0 + 1 + 0 = 01
#
# 0 + 1 + 1 = 10
#
# 1 + 0 + 0 = 01
#
# 1 + 0 + 1 = 10
#
# 1 + 1 + 0 = 10
#
# 1 + 1 + 1 = 11
#
# If we want to add 4 (0100) and 5 (0101) then we need to do 4 additions.
#
# c + a + b = or
#
# 0 + 0 + 1 = 01
#
# 0 + 0 + 0 = 00
#
# 0 + 1 + 1 = 10
#
# 1 + 0 + 0 = 01
#
# The return is 1001. If the last carry value is 1, this is called an overflow. If this happens the carry is truncated because there are no more bits to fit it.
#
# Copy your getStr(question) function from part B for use here.
#
# Implement binarySum(X,Y) that computes the sum of two binary strings. You may assume both inputs are strings containing only the characters "0" and "1". You do not need to error check this.
#
# The two input strings must have the same length. If they have different lengths, return "Cannot Add!".
#
# Add the number using the binary logic described above. You may not convert the numbers to/from integers. You must use the logic for binary addition describe above in your function.
#
# Develop a main function that asks the user for two binary numbers and prints their sum. Repeat until the user tells you to exit.
#
# Welcome to Binary Adder
# Enter exit to quit at any time.
# Enter first Binary Value:
# 0100
# Enter Second Binary Value:
# 0101
# Sum: 1001
# Enter first Binary Value:
# 11111110
# Enter Second Binary Value:
# 00000101
# Sum: 00000011
# Enter first Binary Value:
# 0100
# Enter Second Binary Value:
# 11111
# Sum: Cannot Add!
# Enter first Binary Value:
# 01001110
# Enter Second Binary Value:
# 01011011
# Sum: 10101001
# Enter first Binary Value:
# 0010011010010001
# Enter Second Binary Value:
# 0000010010110001
# Sum: 0010101101000010
# Enter first Binary Value:
# exit

if __name__ == '__main__':
    print('Welcome to Binary Adder')
    print('Enter exit to quit at any time.')
    usrInput1 = input('Enter first Binary Value:\n')
    usrInput2 = input('Enter Second Binary Value:\n')
    while not (usrInput1 in ['exit', 'Exit']):
        if len(usrInput1) != len(usrInput2):
            print('Sum: Cannot Add!')
        else:
            sum = str(bin(int(usrInput1, 2) + int(usrInput2, 2))).replace("0b", "")
            if len(sum) > len(usrInput1):
                print('Sum:', sum[len(sum) - len(usrInput1):])
            else:
                print('Sum:', sum)
        usrInput1 = input('Enter first Binary Value:\n')
        if usrInput1 not in ['exit', 'Exit']:
            usrInput2 = input('Enter Second Binary Value:\n')
