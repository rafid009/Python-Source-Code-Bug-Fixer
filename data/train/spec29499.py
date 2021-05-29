import numpy as np 

def function(x):

	y1 = 2
	z0 = x
	paths = []
	try:
		if y1 > 5:
			z0 = 5+z0
			z0 = z0+z0
			paths.append(1)
		else:
			z0 = 6/z0
			y1 = 8/y1
			x = x-3
			paths.append(2)
		if y1 > 4:
			z0 = z0/7
			y1 = z0*x
			z0 = z0+6
			paths.append(3)
		else:
			y1 = y1/5
			y1 = y1/7
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