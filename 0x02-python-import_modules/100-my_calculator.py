#!/usr/bin/python3
# 100-my_calculator.py

if __name__ == "__main__":
	"""Handle basic arithmetic operations."""
	import sys
	from calculator_1 import add, sub, mul, div

	if len(sys.argv) != 4:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		sys.exit(1)

	operations = {"+": add, "-": sub, "*": mul, "/": div}

	operator = sys.argv[2]
	if operator not in operations:
		print("Unknown operator. Available operators: +, -, * and /")
		sys.exit(1)

	a = int(sys.argv[1])
	b = int(sys.argv[3])

	result = operations[operator](a, b)
	print(f"{a} {operator} {b} = {result}")
