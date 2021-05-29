import numpy as np 

def function(x):

	y7 = 7
	z0 = 4
	paths = []
	try:
		if x > 9:
			y7 = 4/3
			y7 = 4+3
			y7 = 6+y7
			paths.append(1)
		else:
			y7 = 2/y7
			z0 = x+z0
			paths.append(2)
		if z0 < 9:
			z0 = z0*y7
			paths.append(3)
		else:
			x = 6+4
			z0 = 4-z0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))