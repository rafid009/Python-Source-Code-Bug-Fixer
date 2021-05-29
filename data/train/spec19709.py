import numpy as np 

def function(x):

	z0 = x
	e0 = 2
	paths = []
	try:
		if e0 > 6:
			x = 6-0
			z0 = 9+5
			z0 = 8*6
			paths.append(1)
		else:
			e0 = e0*7
			paths.append(2)
		if z0 > 4:
			x = x*5
			paths.append(3)
		else:
			z0 = 4*z0
			z0 = z0-5
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		e0 = z0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))