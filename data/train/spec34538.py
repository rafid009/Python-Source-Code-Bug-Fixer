import numpy as np 

def function(x):

	z3 = x
	c2 = 0
	paths = []
	try:
		if c2 > 4:
			z3 = z3+1
			paths.append(1)
		else:
			z3 = 3*c2
			paths.append(2)
		if c2 >= 7:
			c2 = z3-c2
			c2 = c2*1
			z3 = z3-c2
			paths.append(3)
		else:
			c2 = c2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))