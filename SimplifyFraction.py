# Overview: We ask the user for the numerator and denominator of a fraction and compute its simplified form.
#
# Ask the user for a fraction. The fraction should have the format Integer/Integer. You will need to parse the input on the forward slash to find the numerator and denominator. Computer the GCD Divide both by the GCD and print out the new fraction The greatest common demoninator of two integers is easy to implement recursively. You will not receive credit if your solution is not recursive.
#
# If the Denominator is 1, then only print the numerator. Do not print 5/1, just print 5.
#
# The GCD function must have the format def gcd(a,b).
#
# The gcd(a,0)=a for any integer a. For all other values in the second input, gcd(a,b)=gcd(b,a % b).
#
# Ask for fractions and simplify them until the user enters "exit" as their fraction.
#
# Example
#
# Welcome to Fraction Simplifier
# Type "exit" to quit.
# Enter Fraction (Int/Int):
# 125/55
# Simplified Fraction
# 25/11
# Enter Fraction (Int/Int):
# 8/2
# Simplified Fraction
# 4
# Enter Fraction (Int/Int):
# 27/9
# Simplified Fraction
# 3
# Enter Fraction (Int/Int):
# 76/92
# Simplified Fraction
# 19/23
# Enter Fraction (Int/Int):
# exit
# Bye.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def simplify(num, den):
    hcf = gcd(num, den)
    num //= hcf
    den //= hcf
    if den == 1:
        print('Simplified Fraction')
        print(num)
    else:
        print('Simplified Fraction')
        print(str(num) + '/' + str(den))


if __name__ == '__main__':
    print('Welcome to Fraction Simplifier')
    print('Type \"exit\" to quit.')
    fraction = input('Enter Fraction (Int/Int):\n')
    while fraction != 'exit' or fraction != 'Exit':
        fracList = fraction.split('/')
        numerator = int(fracList[0])
        denominator = int(fracList[1])
        simplify(numerator, denominator)
        fraction = input('Enter Fraction (Int/Int):\n')
        if fraction == 'exit':
            break
    print('Bye.')
