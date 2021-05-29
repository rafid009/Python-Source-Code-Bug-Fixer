import numpy as np 

def function(x):

	z3 = x
	c5 = 8
	paths = []
	try:
		if z3 >= 4:
			z3 = 2-z3
			paths.append(1)
		else:
			z3 = 8-z3
			paths.append(2)
		if z3 < 0:
			x = x*x
			z3 = 0*z3
			x = x/5
			paths.append(3)
		else:
			z3 = z3-z3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))