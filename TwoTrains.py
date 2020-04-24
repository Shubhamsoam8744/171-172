# This problem follows a basic pattern. The values will be replaced by variables in the below question.
#
# Train A, traveling X miles per hour, leaves place1 heading toward place2, total miles away. At the same time Train B, traveling Y mph, leaves place2 heading toward place1. When do the two trains meet? How far are they from each city?
#
# In this lab, you will write a problem that solves this problem. Then you will never have to do it by hand again.
#
# When the meet is determined by
#
# time in hours = (total miles)/(X mph+Y mph)
#
# The distance from place1 is time*X.
#
# The distance from place2 is time*Y.
#
# You may assume that X, Y, and total will be integer values. The results should be given as decimal numbers rounded to 2 digits.
#
# The command round(val, digits) should be used to round. Do not use format to round.
#
# Your program should look like the below example. The solution to the Dr. Math example is given below.

print("Solve the Two Trains Problem.")
print("Enter First Speed:")
fspeed = int(input())
print("Enter First Place:")
fplace = input()
print("Enter Second Speed:")
sspeed = int(input())
print("Enter Second Place:")
splace = input()
print("Enter total distance:")
tot_dist = int(input())
print('Word Problem')
print('Train A, traveling', fspeed, 'miles per hour, leaves', fplace, 'heading toward', splace, ',', tot_dist, 'miles away. At the same time Train B, traveling', sspeed, 'mph, leaves', splace, 'heading toward', fplace, '.', 'When do the two trains meet? How far are they from each city?')
print('Answers')
time2meet = tot_dist/(fspeed + sspeed)
print('They meet after', round(time2meet, 2), 'hours.')
dista = time2meet*fspeed
distb = time2meet*sspeed
print('Train A is', round(dista, 2), 'miles from', fplace)
print('Train B is', round(distb, 2), 'miles from', splace)