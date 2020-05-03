# In this question, you will use the skills you practiced in previous parts of the lab.
#
# There are twelve Zodiac signs in Western Astrology. We are going to use these signs to write a program that tricks people into thinking it can predict the future.
#
# The twelve signs are given below. Depending on the year, these can shift slightly. We will ignore this fact. Act like these dates are always true.
#
# Aries (March 21 to April 19)
# Taurus (April 20 to May 20)
# Gemini (May 21 to June 20)
# Cancer (June 21 to July 22)
# Leo (July 23 to August 22)
# Virgo (August 23 to September 22)
# Libra (September 23 to October 22)
# Scorpio (October 23 to November 21)
# Sagittarius (November 22 to December 21)
# Capricorn (December 22 to January 19)
# Aquarius (January 20 to February 18)
# Pisces (February 19 to March 20)
# Ask for four inputs, the person's name, their birth month (as an integer), their birth day (as an integer), and their birth year (as an integer). Use a Try/Except to check if the values given are really integers. If not, set them to be 0.
#
# Next, use if statements to determine the person's Zodiac sign. If the dates given do not fall into any of the above, assign the person the Zodiac sign Ophiuchus.
#
# Finally, predict the sign of the person the user will marry. Make a list will all the Zodiac signs (except Ophiuchus). Put the Zodiac signs in the list in the same order they are listed above. Set the seed for the random number generator according the below formula
#
# s = year*1000000+month*10000+day*100+len(name)
# random.seed(s)
# Shuffle the list of Zodiac signs and display the one at the first index (position L[0] for list L).
#
# Your output should be styled to match the below example.
#
# Welcome to The Fortune Teller of the Snake
# Enter your Name:
# Pretend Man
# Enter Birth Month (1-12):
# 9
# Enter Birth Day (1-31):
# 1
# Enter Birth Year (XXXX):
# 1979
# Name: Pretend Man
# Born: 9 / 1 / 1979
# Zodiac: Virgo
# You will marry a Cancer

import random

def whichZodiac(day, month):
    astro_sign = ''
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    else:
        astro_sign = 'Ophiuchus'

    return astro_sign


zodiacList = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
print('Welcome to The Fortune Teller of the Snake')
userName = input('Enter your Name:\n')
try:
    month = int(input('Enter Birth Month (1-12):\n'))
except:
    month = 0
try:
    day = int(input('Enter Birth Day (1-31):\n'))
except:
    day = 0
try:
    year = int(input('Enter Birth Year (XXXX):\n'))
except:
    year = 0

s = year * 1000000 + month * 10000 + day * 100 + len(userName)
random.seed(s)

print('Name:', userName)
print('Born:', month, '/', day, '/', year)
print('Zodiac:', whichZodiac(day, month))
random.shuffle(zodiacList)
print('You will marry a', zodiacList[0])
