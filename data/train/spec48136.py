import numpy as np 

def function(x):

	q8 = x
	z0 = x
	paths = []
	try:
		if q8 < 0:
			x = x-3
			z0 = 6+x
			paths.append(1)
		else:
			z0 = q8*z0
			paths.append(2)
		if z0 <= 9:
			x = 5+x
			paths.append(3)
		else:
			z0 = z0+3
			z0 = 0*6
			q8 = 6/q8
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