# The earth does not orbit the sun in exactly 365 days. This means that the Gregorian Calendar would shift if every year had 365 days. To account for this, we add a leap day to some years. This keeps the calendar on track. For example, December is always in the winter.
#
# Write a program that asks the user for a year and determines if the year is a leap year or not.
#
# The algorithm to determine a leap year is as follows:
#
# If the year is not divisible by 4 then it is a common year
# else if the year is not divisible by 100 then it is a leap year
# else if the year is not divisible by 400 then it is a common year
# otherwise it is a leap year.
# Enter a year:
# 2012
# The year 2012 is a leap year.
# Enter a year:
# 1997
# The year 1997 is not a leap year.

def isLeapYear(num):
    result = True
    if num % 4 != 0:
        result = False
    elif num % 100 != 0:
        result = True
    elif num % 400 != 0:
        result = False
    return result


year = int(input('Enter a year:\n'))

if isLeapYear(year):
    print('The year', year, 'is a leap year.')
else:
    print('The year', year, 'is not a leap year.')
