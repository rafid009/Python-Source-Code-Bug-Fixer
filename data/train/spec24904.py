import numpy as np 

def function(x):

	c7 = x
	z3 = 2
	paths = []
	try:
		if c7 < 8:
			c7 = 6-c7
			x = c7+0
			x = 5-9
			paths.append(1)
		else:
			c7 = 5/c7
			c7 = 9+6
			paths.append(2)
		if z3 <= 4:
			c7 = 7-c7
			z3 = z3/5
			paths.append(3)
		else:
			x = x*x
			c7 = c7-c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))