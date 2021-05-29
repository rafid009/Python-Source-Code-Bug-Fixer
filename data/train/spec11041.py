import numpy as np 

def function(x):

	c5 = x
	z3 = 5
	paths = []
	try:
		if z3 <= 5:
			x = z3+z3
			z3 = 5/z3
			paths.append(1)
		else:
			x = 3*x
			x = x-2
			z3 = 9*z3
			paths.append(2)
		if c5 >= 5:
			z3 = x-z3
			z3 = c5/9
			paths.append(3)
		else:
			z3 = z3/z3
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))