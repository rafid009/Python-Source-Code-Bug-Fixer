import numpy as np 

def function(x):

	h9 = 6
	z3 = 8
	paths = []
	try:
		if h9 > 1:
			h9 = z3+h9
			h9 = h9/h9
			z3 = 0+1
			paths.append(1)
		else:
			h9 = h9*8
			paths.append(2)
		if h9 < 1:
			h9 = h9*8
			x = h9+z3
			paths.append(3)
		else:
			h9 = h9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z3 = x**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))