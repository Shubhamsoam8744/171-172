# A prime number is a number that is only divisible by itself and one.
#
# The easiest way to test if a number is prime is to divide it by all smaller numbers. (This is not the fastest way. To get an idea of faster methods read about the Sieve of Eratosthenes )
#
# For example, if we want to find out if 7 is prime or not, we can test all smaller integers.
#
# 7%6=1
#
# 7%5=2
#
# 7%4=3
#
# 7%3=1
#
# 7%2=1
#
# None of those divided evenly. That must mean that 7 is prime.
#
# Write a program that takes an integer as input. If the input is not an integer, repeatedly ask until an integer is given.
#
# Print all prime numbers between 2 and the number given. Test every number in the range to determine if it is prime. You must test each number using the remainder method described above. Repeatedly determine the remainder by dividing the number by smaller values. If none divide evenly, you know the number is prime.
#
# This program will require two nested loops.
#
# Welcome to Prime Generator
# Enter a number:
# Goat
# Enter a number:
# 101
# 2 is a prime number.
# 3 is a prime number.
# 5 is a prime number.
# 7 is a prime number.
# 11 is a prime number.
# 13 is a prime number.
# 17 is a prime number.
# 19 is a prime number.
# 23 is a prime number.
# 29 is a prime number.
# 31 is a prime number.
# 37 is a prime number.
# 41 is a prime number.
# 43 is a prime number.
# 47 is a prime number.
# 53 is a prime number.
# 59 is a prime number.
# 61 is a prime number.
# 67 is a prime number.
# 71 is a prime number.
# 73 is a prime number.
# 79 is a prime number.
# 83 is a prime number.
# 89 is a prime number.
# 97 is a prime number.
# 101 is a prime number.

def primesList(high):
    primeList = []
    for i in range(2, high+1):
        isPrime = True
        for j in range(i-1, 1, -1):
            if i % j == 0:
                isPrime = False
        if isPrime:
            primeList.append(i)
    # print(primeList)
    return primeList


print('Welcome to Prime Generator')
num = input('Enter a number:\n')
while not num.isdigit():
    num = input('Enter a number:\n')

listOfPrimes = primesList(int(num))
for i in listOfPrimes:
    print(i, 'is a prime number.')
