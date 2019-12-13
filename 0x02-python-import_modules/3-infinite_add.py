#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    try:
        result = sum([int(x) for x in argv[1:]])
        print("{}".format(result))
    except ValueError:
        print("Please enter a number")
