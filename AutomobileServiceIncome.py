# (1) Output a menu of automotive services and the corresponding cost of each service. (2 pts)
#
# Ex:
#
# Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12
#
#
#
# (2) Prompt the user for two services from the menu. (2 pts)
#
# Ex:
#
# Select first service:
# Oil change
# Select second service:
# Car wax
#
#
#
# (3) Output an invoice for the services selected. Output the cost for each service and the total cost. (3 pts)
#
#
# Davy's auto shop invoice
#
# Service 1: Oil change, $35
# Service 2: Car wax, $12
#
# Total: $47
#
#
#
# (4) Extend the program to allow the user to enter a dash (-), which indicates no service. (3 pts)
#
# Ex:
#
# Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12
#
# Select first service:
# Tire rotation
# Select second service:
# -
#
# Davy's auto shop invoice
#
# Service 1: Tire rotation, $19
# Service 2: No service
#
# Total: $19

print('''Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12
''')

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': ''}

firstService = input('Select first service:\n')
secondService = input('Select second service:\n')

print('\nDavy\'s auto shop invoice\n')

if firstService == '-':
    print('Service 1: No service')
    print('Service 2:', secondService + ', $' + str(services[secondService]))
    print('\nTotal: $' + str(services[secondService]))
elif secondService == '-':
    print('Service 1:', firstService + ', $' + str(services[firstService]))
    print('Service 2: No service')
    print('\nTotal: $' + str(services[firstService]))
else:
    print('Service 1:', firstService + ', $' + str(services[firstService]))
    print('Service 2:', secondService + ', $' + str(services[secondService]))
    print('\nTotal: $' + str(services[firstService] + services[secondService]))
