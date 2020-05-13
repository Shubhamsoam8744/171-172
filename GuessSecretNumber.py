# Think of a number between 0 and 100. How could be make a computer guess the number?
#
# The simplest method is to just guess every value. This is a poor method. In real life, you would never use this solution.
#
# If someone had a number you were trying to guess, you would gain information with every failed guess.
#
# In our guessing game, when the guess is incorrect the person with the secret number will say "higher" or "lower". This gives the other player information about where to guess next. (You can also play with "hotter" or "colder" but that algorithm is a bit harder.)
#
# Here is a basic layout of the higher/lower algorithm. Implement it in Python.
#
# Set three values low=0, high=101, guess=50
# While you have not guess correctly
# Ask the user if it is correct, higher, or lower
# If the secret number is lower than the guess set high=guess and your next guess is (guess-low)//2+low
# If the secret number is higher than the guess set low=guess and your next guess is (high-guess)//2+guess
# If the input was not valid, say "I did not understand." and make the same guess again.
# Your output should match the below example.
#
# Hello.
# Pick a secret number between 0 and 100.
# Is your secret number 50
# Enter yes/higher/lower:
# lower
# Next is 25
# Is your secret number 25
# Enter yes/higher/lower:
# higher
# Next is 37
# Is your secret number 37
# Enter yes/higher/lower:
# lower
# Next is 31
# Is your secret number 31
# Enter yes/higher/lower:
# lower
# Next is 28
# Is your secret number 28
# Enter yes/higher/lower:
# lower
# Next is 26
# Is your secret number 26
# Enter yes/higher/lower:
# higher
# Next is 27
# Is your secret number 27
# Enter yes/higher/lower:
# yes
# Great!

high = 101
low = 0
guess = 50
print('Hello.')
print('Pick a secret number between 0 and 100.')
print('Is your secret number', guess)
ans = input('Enter yes/higher/lower:\n')
while True:
    if ans == 'lower':
        high = guess
        guess = (guess-low)//2 + low
        print('Next is', guess)
        print('Is your secret number', guess)
        ans = input('Enter yes/higher/lower:\n')
    elif ans == 'higher':
        low = guess
        guess = (high - guess) // 2 + low
        print('Next is', guess)
        print('Is your secret number', guess)
        ans = input('Enter yes/higher/lower:\n')
    elif ans == 'yes':
        print('Great!')
        break
    else:
        print('I did not understand.')
        print('Is your secret number', guess)
        ans = input('Enter yes/higher/lower:\n')