# In this exercise part, you will practice with the built in list data type.
#
# Follow the below steps in order.
#
# Create an empty list
# Ask the user for five float values, append each to the list
# Print the list
# Print the min value using the built in min command
# Print the max value using the built in max command
# Print the length of the list using the built in len command
# Print the total of all values in the list using the built in sum command
# Print the Average of the list (total / number items)
# Your program should match the layout below.
#
# Enter first number:
# 9
# Enter second number:
# 8.7
# Enter third number:
# 12
# Enter fourth number:
# 1000.9
# Enter fifth number:
# 15
# The list is [9.0, 8.7, 12.0, 1000.9, 15.0]
# Min Value: 8.7
# Max Value: 1000.9
# Length of List: 5
# Total all values: 1045.6
# Average: 209.11999999999998

practiceList = []
practiceList.append(float(input('Enter first number:\n')))
practiceList.append(float(input('Enter second number:\n')))
practiceList.append(float(input('Enter third number:\n')))
practiceList.append(float(input('Enter fourth number:\n')))
practiceList.append(float(input('Enter fifth number:\n')))

print('The list is', practiceList)
print('Min Value:', min(practiceList))
print('Max Value:', max(practiceList))
print('Length of List:', len(practiceList))
print('Total all values:', sum(practiceList))
print('Average:', (sum(practiceList)/len(practiceList)))
