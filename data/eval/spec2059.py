import numpy as np 

def function(x):

	z0 = 6
	s8 = 3
	paths = []
	try:
		if z0 >= 1:
			x = 4*4
			paths.append(1)
		else:
			z0 = z0*3
			x = 5-z0
			paths.append(2)
		if s8 >= 7:
			s8 = 4-s8
			z0 = 1-9
			paths.append(3)
		else:
			s8 = x/s8
			x = 3-x
			z0 = 7-z0
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