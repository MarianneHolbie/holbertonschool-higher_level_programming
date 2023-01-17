#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    if sys.argv[2] == '+':
        print("{0} + {1} = {2}".format(a, b, add(int(a), int(b))))
    elif sys.argv[2] == '-':
        print("{0} - {1} = {2}".format(a, b, sub(int(a), int(b))))
    elif sys.argv[2] == '*':
        print("{0} * {1} = {2}".format(a, b, mul(int(a), int(b))))
    elif sys.argv[2] == '/':
        print("{0} / {1} = {2}".format(a, b, div(int(a), int(b))))
