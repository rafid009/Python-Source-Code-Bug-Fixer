import numpy as np 

def function(x):

	z0 = 3
	x7 = x
	paths = []
	try:
		if x > 7:
			z0 = 1/z0
			x7 = z0/x7
			x7 = x7/x7
			paths.append(1)
		else:
			x = 1*9
			paths.append(2)
		if x >= 4:
			z0 = z0+z0
			x7 = 4-x7
			paths.append(3)
		else:
			z0 = z0*2
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		z0 = x7**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))