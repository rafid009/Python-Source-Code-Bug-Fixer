import numpy as np 

def function(x):

	n8 = x
	z3 = x
	paths = []
	try:
		if z3 > 9:
			x = x/x
			paths.append(1)
		else:
			x = 6-2
			paths.append(2)
		if x >= 1:
			x = 7-z3
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		n8 = z3**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))