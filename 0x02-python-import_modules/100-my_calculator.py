#!/usr/bin/python3

import sys
import calculator_1

"""Handle basic operations."""
if len(sys.argv) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

try:
    func = getattr(calculator_1, operator)
    result = func(a, b)
    print(f"{a} {operator} {b} = {result}")
except AttributeError:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
