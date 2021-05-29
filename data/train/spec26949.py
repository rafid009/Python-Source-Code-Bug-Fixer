import numpy as np 

def function(x):

	z5 = 5
	g3 = 5
	paths = []
	try:
		if z5 < 8:
			z5 = z5*6
			z5 = z5/g3
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if z5 > 6:
			x = 3+x
			x = 0+g3
			paths.append(3)
		else:
			z5 = z5-z5
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