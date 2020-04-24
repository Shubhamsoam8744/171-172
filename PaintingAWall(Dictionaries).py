# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('{:.2f}'.format(your_value))
#
#
# (1) Prompt the user to input a wall's height and width. Calculate and output the wall's area (integer). (Submit for 2 points).
#
# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
#
# (2) Extend to also calculate and output the amount of paint in gallons needed to paint the wall (floating point). Assume a gallon of paint covers 350 square feet. Store this value in a variable. Output the amount of paint needed using the %f conversion specifier. (Submit for 2 points, so 4 points total).
#
# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
# Paint needed: 0.51 gallons
#
# (3) Extend to also calculate and output the number of 1 gallon cans needed to paint the wall. Hint: Use a math function to round up to the nearest gallon. (Submit for 2 points, so 6 points total).
#
# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
# Paint needed: 0.51 gallons
# Cans needed: 1 can(s)
#
# (4) Extend by prompting the user for a color they want to paint the walls. Calculate and output the total cost of the paint cans depending on which color is chosen. Hint: Use a dictionary to associate each paint color with its respective cost. Red paint costs $35 per gallon can, blue paint costs $25 per gallon can, and green paint costs $23 per gallon can. (Submit for 2 points, so 8 points total).
#
# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
# Paint needed: 0.51 gallons
# Cans needed: 1 can(s)
#
# Choose a color to paint the wall:
# red
# Cost of purchasing red paint: $35


import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')

# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
amountOfPaint = wall_area / 350
print('Paint needed: {:.2f} gallons'.format(amountOfPaint))

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
noOfCans = math.ceil(amountOfPaint)
print('Cans needed: {0} can(s)'.format(noOfCans))

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
wallColor = input('\nChoose a color to paint the wall:\n')
print('Cost of purchasing', wallColor, 'paint: $' + str(paint_colors[wallColor] * noOfCans))


