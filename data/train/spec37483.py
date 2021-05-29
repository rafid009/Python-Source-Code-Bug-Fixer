import numpy as np 

def function(x):

	z0 = x
	k2 = 2
	paths = []
	try:
		if z0 >= 6:
			k2 = k2-3
			paths.append(1)
		else:
			x = x+z0
			k2 = 9-z0
			paths.append(2)
		if k2 < 1:
			k2 = 9*x
			z0 = z0*8
			paths.append(3)
		else:
			k2 = 5/k2
			k2 = 6/x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))