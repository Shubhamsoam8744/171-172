# Write a program that reads in the amount of a check from input as a float.
# Convert that value to an integer number of cents.
# Finally, print out how to cash the check in twenties, fives, ones, quarters, dimes, nickels, and pennies.

print("Enter Check Value as a decimal:")
amt = float(input())
print("Twenties:", int(amt//20))
amt = amt % 20
print("Tens:", int(amt//10))
amt = amt % 10
print("Fives:", int(amt//5))
amt = amt % 5
print("Ones:", int(amt//1))
amt = amt % 1
print("Quarters:", int(amt//0.25))
amt = amt % 0.25
print("Dimes:", int(amt//0.1))
amt = amt % 0.1
print("Nickels:", int(amt//0.05))
amt = amt % 0.05
print("Pennies:", int(amt//0.01))