#!/usr/bin/python3
for i in range(0, 8):
    for j in range(1, 10):
        if j > i:
            print("{}{}, ".format(i, j), end='')
print("89")
