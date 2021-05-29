import numpy as np 

def function(x):

	c0 = 1
	z3 = x
	paths = []
	try:
		if c0 >= 1:
			x = c0-7
			z3 = z3*c0
			paths.append(1)
		else:
			z3 = z3/z3
			c0 = c0/1
			paths.append(2)
		if x <= 1:
			z3 = 1/z3
			paths.append(3)
		else:
			c0 = 9+c0
			c0 = 8-5
			z3 = z3+4
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