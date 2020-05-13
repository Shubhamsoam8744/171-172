#
# Write a program that takes three integers as input. The three values are a starting number, stoping number, and step size. Print all values from the start number to the stop number. Increase the number by the step size.
#
# Enter Start Value:
# 1
# Enter Stop Value:
# 21
# Enter Step Value:
# 5
# Value: 1
# Value: 6
# Value: 11
# Value: 16
# Value: 21
# No error checking is required on this program. You may assume only valid inputs will be given

start = int(input('Enter Start Value:\n'))
stop = int(input('Enter Stop Value:\n'))
step = int(input('Enter Step Value:\n'))

for i in range(start, stop+1, step):
    print('Value:', i)