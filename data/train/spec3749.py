import numpy as np 

def function(x):

	z0 = 0
	y5 = 6
	paths = []
	try:
		if z0 < 1:
			z0 = 3/x
			y5 = 2+y5
			x = 7+x
			paths.append(1)
		else:
			y5 = y5/x
			y5 = 8*y5
			paths.append(2)
		if x >= 4:
			z0 = y5-z0
			y5 = y5*x
			y5 = 1-3
			paths.append(3)
		else:
			z0 = z0-2
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		z0 = y5**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))