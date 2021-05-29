import numpy as np 

def function(x):

	z5 = 4
	c3 = x
	paths = []
	try:
		if x > 0:
			c3 = 8/z5
			x = z5/c3
			c3 = z5*c3
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if c3 < 3:
			z5 = z5-z5
			c3 = c3*7
			paths.append(3)
		else:
			c3 = 6*2
			c3 = c3+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))