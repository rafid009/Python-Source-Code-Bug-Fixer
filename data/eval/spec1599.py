import numpy as np 

def function(x):

	y0 = x
	z0 = x
	paths = []
	try:
		if y0 < 7:
			y0 = z0/y0
			paths.append(1)
		else:
			x = y0/y0
			paths.append(2)
		if x > 4:
			x = 3+y0
			x = x/y0
			y0 = 0-x
			paths.append(3)
		else:
			y0 = 1-x
			z0 = z0*y0
			z0 = z0*7
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))