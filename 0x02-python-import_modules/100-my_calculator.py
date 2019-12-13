#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    from sys import argv

    argc = len(argv) - 1
    operators = ["+", "-", "*", "/"]
    func = [add, sub, mul, div]
    a = int(argv[1])
    b = int(argv[3])

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i, operator in enumerate(operators):
        if argv[2] == operator:
            print("{} {} {} = {}".format(a, operator, b, func[i](a, b)))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and / ")
    exit(1)
