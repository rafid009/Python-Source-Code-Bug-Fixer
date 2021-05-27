import numpy as np 

def function(x):

	h6 = x
	z3 = x
	paths = []
	try:
		if h6 > 7:
			x = x-9
			x = x/z3
			h6 = h6+z3
			paths.append(1)
		else:
			z3 = z3/2
			h6 = 2*z3
			h6 = h6*h6
			paths.append(2)
		if z3 > 9:
			h6 = 3/x
			paths.append(3)
		else:
			h6 = 0-6
			x = x*8
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))