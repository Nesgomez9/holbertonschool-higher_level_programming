#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {} is {}"
if number > 0:
    n = number % 10
else:
    n = number % -10
print(str.format(number, n), end = '')
if n == 0:
    print(" and is 0")
elif n > 5:
    print(" and is greater than 5")
else:
    print(" and is less than 6 and not 0")
