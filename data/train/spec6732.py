import numpy as np 

def function(x):

	z0 = 3
	b3 = 2
	paths = []
	try:
		if x < 8:
			x = 9*x
			paths.append(1)
		else:
			b3 = 9+z0
			z0 = 6-z0
			b3 = 2-5
			paths.append(2)
		if b3 < 2:
			z0 = z0+5
			b3 = b3/3
			paths.append(3)
		else:
			z0 = z0*z0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))