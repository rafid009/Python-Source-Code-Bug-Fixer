import numpy as np 

def function(x):

	h0 = 4
	z3 = 6
	paths = []
	try:
		if h0 >= 3:
			x = 6*x
			paths.append(1)
		else:
			z3 = 6+x
			x = 1-x
			paths.append(2)
		if x >= 7:
			h0 = 1-h0
			x = 9/x
			paths.append(3)
		else:
			x = x/8
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