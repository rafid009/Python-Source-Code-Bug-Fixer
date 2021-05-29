import numpy as np 

def function(x):

	c6 = x
	z0 = x
	x = x
	paths = []
	try:
		if x > 4:
			x = c6+5
			x = 3-x
			z0 = z0/x
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if x > 8:
			c6 = 3-c6
			c6 = 8-c6
			paths.append(3)
		else:
			c6 = 7-c6
			x = x*4
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