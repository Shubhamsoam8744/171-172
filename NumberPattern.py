# Write a recursive function called print_num_pattern() to output the following number pattern.
#
# Given a positive integer as input (Ex: 12), subtract another positive integer (Ex: 3) continually until 0 or a negative value is reached, and then continually add the second integer until the first integer is again reached.
#
# Ex. If the input is:
#
# 12
# 3
# the output is:
#
# 12 9 6 3 0 3 6 9 12

# TODO: Write recursive print_num_pattern() function

def print_num_pattern(a, b):
    if a <= 0:
        print(a, end=" ")
    else:
        print(a, end=" ")
        print_num_pattern(a - b, b)
        print(a, end=" ")


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)
