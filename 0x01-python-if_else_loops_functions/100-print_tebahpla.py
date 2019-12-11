#!/usr/bin/python3
n = 122
for i in range(26):
    print("{}".format(chr(n)), end='')
    n -= 1
    if n >= 97 and n < 122:
        n -= 32
    else:
        n += 32
