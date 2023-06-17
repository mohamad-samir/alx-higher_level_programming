#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
	"""Print the result of the addition of all arguments."""
	import sys

	total = 0
	for arg in sys.argv[1:]:
		total += int(arg)
	print(total)
