import numpy as np 

def function(x):

	z5 = 8
	c9 = x
	paths = []
	try:
		if z5 >= 9:
			z5 = z5/x
			z5 = z5/z5
			z5 = 4-x
			paths.append(1)
		else:
			z5 = 7-8
			z5 = x/c9
			paths.append(2)
		if x < 8:
			x = z5/c9
			paths.append(3)
		else:
			z5 = c9-x
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