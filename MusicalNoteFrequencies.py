
# On a piano, a key has a frequency, say f0. Each higher key (black or white) has a frequency of f0 * r^n, where n is the distance (number of keys) from that key, and r is 2^(1/12).
# Given an initial key frequency, output that frequency and the next 4 higher key frequencies.
#
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4, your_value5))

import math
r = math.pow(2, (1/12))
value1 = int(input())

value2 = value1 * math.pow(r, 1)
value3 = value1 * math.pow(r, 2)
value4 = value1 * math.pow(r, 3)
value5 = value1 * math.pow(r, 4)

print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(value1, value2, value3, value4, value5))
