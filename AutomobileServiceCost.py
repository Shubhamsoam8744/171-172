# (1) Prompt the user for an automobile service. Output the user's input. (1 pt)
#
# Ex:
#
# Enter desired auto service:
# Oil change
# You entered: Oil change
#
# (2) Output the price of the requested service. (4 pts)
#
# Ex:
#
# Enter desired auto service:
# Oil change
# You entered: Oil change
# Cost of oil change: $35
#
# The program should support the following services (all integers):
#
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# If the user enters a service that is not listed above, then output the following error message:
#
#
# Error: Requested service is not recognized

serviceRequest = input('Enter desired auto service:\n')
if serviceRequest == 'Oil change':
    print('You entered: Oil change')
    print('Cost of oil change: $35')
elif serviceRequest == 'Tire rotation':
    print('You entered: Tire rotation')
    print('Cost of tire rotation: $19')
elif serviceRequest == 'Car wash':
    print('You entered: Car wash')
    print('Cost of car wash: $7')
else:
    print('You entered:', serviceRequest)
    print('Error: Requested service is not recognized')
