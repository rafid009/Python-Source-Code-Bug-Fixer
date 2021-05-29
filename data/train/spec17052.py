import numpy as np 

def function(x):

	z3 = 6
	c6 = 3
	paths = []
	try:
		if z3 <= 6:
			z3 = 3-x
			x = 4*7
			paths.append(1)
		else:
			c6 = 0-c6
			paths.append(2)
		if z3 < 7:
			c6 = c6+z3
			z3 = 3*z3
			paths.append(3)
		else:
			z3 = z3-6
			x = x-x
			z3 = z3/6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))