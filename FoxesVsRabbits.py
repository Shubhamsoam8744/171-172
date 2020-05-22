# Imagine a population of Foxes and Rabbits living in an enclosed space. Each year, some animals are born and some die. Foxes will cause some of the rabbits to die. If the number of rabbits is too small, some foxes will die from starvation.
#
# This problem can be modeled in a program.
#
# At the start of recorded time, there are a starting number of Foxes and Rabbits.
#
# For example, at year 0
#
# R[0] = 5,891 F[0] = 16
#
# After one year passes, the number of animals will change. We need to compute the birth-death amount for the year.
#
# R[1] = R[0] + Floor( R[0] * (A-B * F[0]))
#
# The number of foxes changes the number of births and deaths.
#
# A similar change in the foxes is caused by the number of rabbits.
#
# F[1] = F[0] – Floor(F[0] * (G-S * R[0]))
#
# A reasonable setting for these variables based on experimental data is.
#
# A = 0.04 B = 0.0005 G = 0.2 S = 0.00005
#
# After 1 year, the population looks like
#
# R[1] = 5891+Floor(5891 * (0.04-0.0005 * 16)) = 6079 Rabbits
#
# F[1] = 16 – Floor(16 * (0.2-0.00005 * 5891)) = 18 Foxes
#
# Write a function bunnies(rabbits, foxes, years) that takes three inputs, the starting number of rabbits, starting number of foxes, and number of years to simulate. Return a List with two items. Put the final number of rabbits at index 0 and final number of foxes at index 1.
#
# It is impossible to have a fractional fox or rabbit. The floor function rounds down to the nearest integer.
#
# For example, bunnies(5891,16,1) will return [6079,18].
#
# Develop a user interface that askes the user for the initial number of rabbits, initial number of foxes, and number of years to run the simulation. Print out the final populations.
#
# Your function will be auto-tests. Make sure to use the if name=="main": command around your input/output so ZyBooks can test your function.
#
# An example execution trace is provided below.
#
# Welcome to Predator-Prey Model.
# Enter Initial Rabbit Population:
# 5891
# Enter Initial Fox Population:
# 16
# Enter Number of Years to Simulate:
# 99
# After 99 years there will be 6484 rabbits.
# After 99 years there will be 144 foxes.


import math


def bunnies(rabbits, foxes, years):
    A = 0.04
    B = 0.0005
    G = 0.2
    S = 0.00005
    rabbitList = []
    foxList = []
    rabbitList.append(rabbits)
    foxList.append(foxes)
    for i in range(years):
        rabbitList.append(rabbitList[i] + math.floor(rabbitList[i] * (A - B * foxList[i])))
        foxList.append(foxList[i] - math.floor(foxList[i] * (G - S * rabbitList[i])))
    result = [rabbitList[-1], foxList[-1]]
    return result


if __name__ == '__main__':
    print('Welcome to Predator-Prey Model.')
    initRabbit = int(input('Enter Initial Rabbit Population:\n'))
    initFoxes = int(input('Enter Initial Fox Population:\n'))
    initYears = int(input('Enter Number of Years to Simulate:\n'))
    data = bunnies(initRabbit, initFoxes, initYears)
    print('After', initYears, 'years there will be', data[0], 'rabbits.')
    print('After', initYears, 'years there will be', data[1], 'foxes.')
