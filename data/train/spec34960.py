import numpy as np 

def function(x):

	z3 = 6
	h6 = 2
	paths = []
	try:
		if h6 >= 0:
			z3 = 2*z3
			h6 = 0-6
			x = x-z3
			paths.append(1)
		else:
			z3 = x+6
			x = 0/x
			x = z3*x
			paths.append(2)
		if x < 2:
			z3 = z3+z3
			paths.append(3)
		else:
			z3 = z3*4
			h6 = 4*1
			h6 = z3+h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))