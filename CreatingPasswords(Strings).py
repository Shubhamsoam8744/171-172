# (1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space. (Submit for 1 point)
#
# Enter favorite color:
# yellow
# Enter pet's name:
# Daisy
# Enter a number:
# 6
# You entered: yellow Daisy 6
#
# (2) Output two passwords using a combination of the user input. Format the passwords as shown below. (Submit for 2 points, so 3 points total).
#
# Enter favorite color:
# yellow
# Enter pet's name:
# Daisy
# Enter a number:
# 6
# You entered: yellow Daisy 6
#
# First password: yellow_Daisy
# Second password: 6yellow6
#
# (3) Output the length of each password (the number of characters in the strings). (Submit for 2 points, so 5 points total).
#
# Enter favorite color:
# yellow
# Enter pet's name:
# Daisy
# Enter a number:
# 6
# You entered: yellow Daisy 6
#
# First password: yellow_Daisy
# Second password: 6yellow6
#
# Number of characters in yellow_Daisy: 12
# Number of characters in 6yellow6: 8


fav_color = input('Enter favorite color:\n')
pet_name = input('Enter pet\'s name:\n')
user_num = int(input('Enter a number:\n'))

print('You entered:', fav_color, pet_name, user_num)

first_pass = fav_color + '_' + pet_name
second_pass = str(user_num) + fav_color + str(user_num)

print('\nFirst password:', first_pass)
print('Second password:', second_pass)

print('\nNumber of characters in', first_pass + ':', len(first_pass))
print('Number of characters in', second_pass + ':', len(second_pass))

