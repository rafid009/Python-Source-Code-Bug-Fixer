import numpy as np 

def function(x):

	h9 = x
	z3 = x
	paths = []
	try:
		if z3 > 6:
			z3 = 5+3
			x = x*9
			paths.append(1)
		else:
			z3 = z3*4
			paths.append(2)
		if z3 > 5:
			h9 = z3+h9
			z3 = 3/z3
			paths.append(3)
		else:
			x = x-h9
			x = z3-5
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))