#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    n = number % 10
else:
    n = number % -10
print("Last digit of {} is {}".format(number, n), end = '')
if n == 0:
    print(" and is 0")
elif n > 5:
    print(" and is greater than 5")
else:
    print(" and is less than 6 and not 0")
