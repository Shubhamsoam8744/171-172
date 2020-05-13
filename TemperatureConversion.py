# Develop a function def celsius(f) that converts a temperature from Fahrenheit to Celsius. Here is the formula to go in the reverse direction F=C*1.8+32.
#
# Write a program using your function that asks the user for a temperature, read as a double, and converts it to Celsius. The program should run until the user enters "exit". If the user enters an invalid temperature, ask again.
#
# When the program exits print "Bye."
#
# Here is a example execution trace.
#
# Fahrenheit to Celsius Converter.
# Enter "Exit" to quit.
# Enter Temp in Fahrenheit:
# -58
# In Celsius this is -50.0
# Enter Temp in Fahrenheit:
# -40
# In Celsius this is -40.0
# Enter Temp in Fahrenheit:
# -22
# In Celsius this is -30.0
# Enter Temp in Fahrenheit:
# -4
# In Celsius this is -20.0
# Enter Temp in Fahrenheit:
# 14
# In Celsius this is -10.0
# Enter Temp in Fahrenheit:
# 15.8
# In Celsius this is -9.0
# Enter Temp in Fahrenheit:
# 32
# In Celsius this is 0.0
# Enter Temp in Fahrenheit:
# 194
# In Celsius this is 90.0
# Enter Temp in Fahrenheit:
# Bad Input
# Invalid Input. Please try again.
# Enter Temp in Fahrenheit:
# Exit
# Bye.

print('''Fahrenheit to Celsius Converter.
Enter \"Exit\" to quit.''')
temp = input('Enter Temp in Fahrenheit:\n')
while temp != 'Exit' and temp != 'exit':
    try:
        print('In Celsius this is', (float(temp) - 32)/1.8)
        temp = input('Enter Temp in Fahrenheit:\n')

    except:
        print('Invalid Input. Please try again.')
        temp = input('Enter Temp in Fahrenheit:\n')

print('Bye.')