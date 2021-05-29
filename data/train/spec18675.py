import numpy as np 

def function(x):

	d4 = x
	z5 = x
	paths = []
	try:
		if x >= 0:
			z5 = 1-z5
			z5 = 6-z5
			paths.append(1)
		else:
			z5 = 1+6
			z5 = 8/d4
			paths.append(2)
		if x >= 3:
			x = d4+x
			x = 6-d4
			paths.append(3)
		else:
			z5 = 6*z5
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