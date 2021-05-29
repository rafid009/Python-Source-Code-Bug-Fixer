import numpy as np 

def function(x):

	z5 = x
	c4 = 2
	paths = []
	try:
		if x >= 6:
			c4 = 1*8
			z5 = 9+z5
			c4 = 6+8
			paths.append(1)
		else:
			c4 = x/8
			x = 5*x
			x = x/z5
			paths.append(2)
		if z5 < 0:
			x = z5*c4
			x = x-z5
			paths.append(3)
		else:
			c4 = c4+2
			x = x-8
			z5 = 9/8
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))